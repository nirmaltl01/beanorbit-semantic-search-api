# Semantic Search API

A FastAPI-based semantic search system using SentenceTransformers and FAISS.

## Features

- FastAPI backend
- SentenceTransformer embeddings
- FAISS vector database
- Semantic similarity search
- POST /query endpoint
- Unit tests

## Setup

### 1. Clone Repository

git clone <repo-url>
cd beanorbit-semantic-api

### 2. Create Virtual Environment

python -m venv venv
venv\Scripts\activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Run API

uvicorn app.main:app --reload

API runs at:
http://127.0.0.1:8000

Swagger docs:
http://127.0.0.1:8000/docs

### 5. Run Tests

pytest

## Docker

Build:
docker build -t semantic-api .

Run:
docker run -p 8000:8000 semantic-api

## Endpoint

POST /query

Request:
{
    "query": "your question here"
}

Response:
{
    "results": [
        {
            "score": 0.89,
            "content": "most relevant chunk"
        }
    ]
}
