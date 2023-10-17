# Hackathon Legal Tech Titan
## Description

The Hackathon_Legal_Tech_Titan project seeks to transform how users engage with legal documents. With our system, users can pose specific legal inquiries, and in turn, it intelligently identifies and presents the top N most pertinent legal documents related to the query.

Beyond merely presenting these documents, we've integrated a dynamic Q&A chatbot that facilitates deeper interaction with the content. Additionally, our system offers the capability to succinctly summarize these documents, making legal research more efficient and user-friendly.

This repository serves as a **prototype** of our envisioned end solution. For the purposes of this prototype, we operate under the assumption that the document retrieval phase is already completed. The primary focus here is on the Q&A chatbot functionality and the document summarization capabilities.

--> Try the App : [HERE](https://ubs-hackathon-legal-tech-titan.streamlit.app/)

## Installation & Requirements
### Part1. Set up environment
```bash
conda create --name hackathon python=3.10.6
conda activate hackathon
pip install -r requirements.txt
```
### Part2. git clone repo
```bash
git clone https://github.com/stanFurrer/UBS_Hackathon_Legal_Tech_Titan.git
```
### Part3. Save Secret (Your OpenAI API Key)
* Found your own OpenAI API Key : [Here](https://platform.openai.com/account/api-keys)
```bash
mkdir .streamlit # Create Folder
echo OPENAI_API_KEY= <YOUR API KEY> > secrets.toml # Create Secret
```

## Running with Default Settings

1. Ensure you've activated the conda environment as mentioned above and have create your secret.
2. run the app : 
```bash
streamlit run app.py --server.port 8502
```
3. Try to load and play with : *Example_legal_doc.pdf*

## Authors
| #  | Name                 | Role                   |
|----|----------------------|------------------------|
|    | Sarah Burke          | Team Mentor            |
|    | Richard James        | Team Sponsor           |
| 1  | Banarasi Tippa       | Tech Lead              |
| 2  | Vlad Stoian          | Product Owner          |
| 5  | Olivia Monk          | Program Manager        |
| 3  | James Peter Lecard   | Automation Engineer    |
| 4  | Gioele Crispo        | ML Engineer            |
| 6  | Ilias Fotopoulos     | ML Engineer            |
| 7  | James Roy            | ML Engineer            |
| 8  | Wei Jiang            | ML Engineer            |
| 9  | Labinot Jakupi       | Full Stack  Developer  |
| 10 | Marta Mendez Perez   | ML Engineer            |
| 11 | Stan Furrer          | ML Engineer            |
| 12 | Anup Ajayan          | DevOps Engineer        |





