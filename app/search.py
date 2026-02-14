import faiss
import numpy as np
from app.embeddings import generate_embeddings
from app.config import TOP_K

class VectorSearch:
    def __init__(self, texts):
        self.texts = texts

        # Generate embeddings for all chunks
        self.embeddings = generate_embeddings(texts)

        # Normalize embeddings for cosine similarity
        faiss.normalize_L2(self.embeddings)

        self.dimension = self.embeddings.shape[1]

        # Use Inner Product for cosine similarity
        self.index = faiss.IndexFlatIP(self.dimension)
        self.index.add(self.embeddings)

    def query(self, query_text: str):
        # Generate embedding for query
        query_embedding = generate_embeddings([query_text])

        # Normalize query vector
        faiss.normalize_L2(query_embedding)

        # Search top K results
        scores, indices = self.index.search(query_embedding, TOP_K)

        results = []

        for idx, score in zip(indices[0], scores[0]):
            results.append({
                "score": float(score),
                "content": self.texts[idx]
            })

        return results
