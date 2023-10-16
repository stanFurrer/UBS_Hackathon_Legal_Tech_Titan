# UBS Hackathon Legal Tech Titan
## Description

The UBS_Hackathon_Legal_Tech_Titan project seeks to transform how users engage with legal documents. With our system, users can pose specific legal inquiries, and in turn, it intelligently identifies and presents the top N most pertinent legal documents related to the query.

Beyond merely presenting these documents, we've integrated a dynamic Q&A chatbot that facilitates deeper interaction with the content. Additionally, our system offers the capability to succinctly summarize these documents, making legal research more efficient and user-friendly.

This repository serves as a **prototype** of our envisioned end solution. For the purposes of this prototype, we operate under the assumption that the document retrieval phase is already completed. The primary focus here is on the Q&A chatbot functionality and the document summarization capabilities.

## Installation & Requirements
### Part1. Set up environment
```bash
conda create --name UBS_hackathon python=3.10.6
conda activate UBS_hackathon
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

## Authors
| #  | Name                 | Role                   | M/F | Location | Company | Organization                  |
|----|----------------------|------------------------|-----|----------|---------|-------------------------------|
|    | Sarah Burke          | Team Mentor            | F   | CH       | CS      | Digital Legal Solutions       |
|    | Richard James        | Team Sponsor           | M   | CH       | UBS     | Digital Legal Solutions       |
| 1  | Banarasi Tippa       | Tech Lead              | M   | US       | UBS     | Digital Legal Solutions       |
| 2  | Vlad Stoian          | Product Owner          | M   | LON      | UBS     | Digital Legal Solutions       |
| 5  | Olivia Monk          | Program Manager        | F   | LON      | UBS     | Digital Legal Solutions       |
| 3  | James Peter Lecard   | Automation Engineer    | M   | CH       | UBS     | Digital Legal Solutions       |
| 4  | Gioele Crispo        | ML Engineer            | M   | CH       | UBS     | Digital Legal Solutions       |
| 6  | Ilias Fotopoulos     | ML Engineer            | M   | CH       | UBS     | Digital Legal Solutions       |
| 7  | James Roy            | ML Engineer            | M   | CH       | UBS     | ADA Talent Development        |
| 8  | Wei Jiang            | ML Engineer            | F   | CH       | CS      | Credit Risk Analytics         |
| 9  | Labinot Jakupi       | Full Stack  Developer  | M   | CH       | CS      | Analytics and Marketing       |
| 10 | Marta Mendez Perez   | ML Engineer            | F   | CH       | CS      | Analytics and Marketing       |
| 11 | Stan Furrer          | ML Engineer            | M   | CH       | CS      | Credit Risk Analytics         |
| 12 | Anup Ajayan          | DevOps Engineer        | M   | US       | UBS     | Market Risk Exposure Platforms|





