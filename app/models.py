from pydantic import BaseModel
from typing import List

class QueryRequest(BaseModel):
    query: str

class SearchResult(BaseModel):
    score: float
    content: str

class QueryResponse(BaseModel):
    results: List[SearchResult]
