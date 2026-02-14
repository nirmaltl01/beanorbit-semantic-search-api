# BeanOrbit Semantic Search API

A production-ready semantic search backend built using FastAPI, FAISS, and transformer-based embeddings.

This API loads a company profile from a .txt file, generates vector embeddings, stores them in a vector database, and exposes a semantic search endpoint to retrieve the most relevant answers.

# Features

FastAPI backend
Loads and processes .txt data
Text chunking for improved search accuracy
Transformer-based embedding generation
FAISS vector database for similarity search
Semantic similarity search using cosine similarity
POST /query endpoint
Async API implementation
Proper error handling with HTTPException
Structured logging
Unit tests using Pytest
Docker containerization
Swagger UI documentation (/docs)
Clean modular project structure
Deployment-ready setup

# How It Works

Load the company profile from a .txt file.

Split the text into meaningful chunks.

Convert each chunk into a dense embedding vector.

Store embeddings in a FAISS vector index.

When a query is received:

Embed the query

Perform similarity search

Return the most relevant text chunk

This enables semantic search rather than keyword-based matching.

# Project Structure
beanorbit-semantic-api/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── data_loader.py
│   ├── embeddings.py
│   ├── search.py
│   ├── models.py
│   └── logger.py
│
├── data/
│   └── beanorbit_company_profile.txt
│
├── tests/
│   ├── pytest.ini
│   └── test_query.py
│
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md

# Local Setup

1. Clone the Repository
git clone <your-repo-url>
cd beanorbit-semantic-api

2. Create Virtual Environment
python -m venv venv

Activate (Windows):

    venv\Scripts\activate

Activate (Mac/Linux):

    source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Run the Application
uvicorn app.main:app --reload


API will run at:

http://127.0.0.1:8000


Swagger documentation:

http://127.0.0.1:8000/docs

API Endpoint
POST /query

Request body:

{
  "query": "What does BeanOrbit do?"
}


Response:

{
  "answer": "Most relevant text chunk..."
}


Returns the most semantically relevant answer from the document.

# Run Tests
pytest

# Docker Setup
Build Docker Image:
docker build -t semantic-api .

Run Container:
docker run -p 8000:8000 semantic-api


Access at:

http://localhost:8000

# Technical Stack

FastAPI
FAISS (Vector Database)
Sentence Transformers
Uvicorn
Pytest
Docker