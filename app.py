from config import OPENAI_API_KEY
import streamlit as st
from dotenv import load_dotenv
import pickle
from PyPDF2 import PdfReader
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
import os

st.set_page_config(page_title='🤗💬 PDF Chat App - GPT')

# Sidebar contents
with st.sidebar:
    st.title('Legal Documents Chat App')
    st.markdown('''
    ## About
    Prototype of our solution for the Hackathon.
    Build with : 
    - [Streamlit](https://streamlit.io/)
    - [LangChain](https://python.langchain.com/)
    - [OpenAI](https://platform.openai.com/docs/models)
    ''')
    add_vertical_space(5)
    st.write('''Legal Tech Titans. 🔥We Gonna Win🔥''')


def main():
    #Step1. Front-End
    st.header("Chat with your legal document ")
    st.markdown('''
             This app uses OpenAI's ChatGpt 3.5 model to answer questions about your PDF file.  
             ''')

    st.header("Step1. Pass your OpenAI API Key")
    v='demo'
    openai_key=st.text_input("**OPEN AI API KEY**", value=v)
    st.write("You can get your OpenAI API key from [here](https://platform.openai.com/account/api-keys)")

    #Step2. Set-up the OpenAI API Key
    if openai_key==v:
        openai_key = st.secrets["OPENAI_API_KEY"]

    os.environ["OPENAI_API_KEY"] = openai_key

    #Step3. upload a PDF file
    st.header("Step2. Upload PDF")
    pdf = st.file_uploader("**Upload your PDF**", type='pdf')

    if pdf is not None:
        # Step3.1. Read PDF
        pdf_reader = PdfReader(pdf)
        text = ""

        # Step3.2. Extract the text of all the Pages
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        # Step3.3. Split the Text Into Chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
            )
        chunks = text_splitter.split_text(text=text)

        # Step3.4. Save the Embeddings Locally.
        #  Load if Exist
        #  Create Vector Embedding. Here we Use FAISS From Facebook. 
        store_name = pdf.name[:-4]
        st.write(f'{store_name}')

        if os.path.exists(f"{store_name}.pkl"):
            with open(f"{store_name}.pkl", "rb") as f:
                VectorStore = pickle.load(f)
        else:
            embeddings = OpenAIEmbeddings()
            VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
            with open(f"{store_name}.pkl", "wb") as f:
                pickle.dump(VectorStore, f)

        # Step4. Get the Question From the User
        st.header("Step3. Ask questions about your PDF file:")
        q="Tell me about the content of the PDF"
        query = st.text_input("Questions",value=q)
        #Step5.. If Ask is triggered Compute the Similarity Search
        if st.button("Ask"):
            if openai_key=='':
                st.write('Warning: Please pass your OPEN AI API KEY on Step 1')
            else:
                #Step5.1. Retrieve the top 3 Chunks
                docs = VectorStore.similarity_search(query=query, k=3)
                #Step5.2. Load the Model
                llm = OpenAI()
                chain = load_qa_chain(llm=llm, chain_type="stuff")
                with get_openai_callback() as cb:
                    response = chain.run(input_documents=docs, question=query)
                    print(cb)
                st.header("Answer:")
                st.write(response)
                st.write('--')
                st.header("OpenAI API Usage:")
                st.text(cb)

if __name__ == '__main__':
    main()
