from fastapi import FastAPI, HTTPException
from app.models import QueryRequest, QueryResponse
from app.data_loader import load_and_chunk_text
from app.search import VectorSearch
from app.logger import get_logger
from app.config import DATA_PATH

app = FastAPI(
    title="BeanOrbit Semantic Search API",
    description="Semantic search over BeanOrbit company knowledge base",
    version="1.0.0"
)

logger = get_logger()

try:
    text_chunks = load_and_chunk_text(DATA_PATH)
    search_engine = VectorSearch(text_chunks)
    logger.info("Vector database initialized successfully.")
except Exception as e:
    logger.error(f"Startup failed: {e}")
    raise

@app.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest):
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    try:
        results = search_engine.query(request.query)
        return QueryResponse(results=results)
    except Exception as e:
        logger.error(f"Search error: {e}")
        raise HTTPException(status_code=500, detail="Search failed")
