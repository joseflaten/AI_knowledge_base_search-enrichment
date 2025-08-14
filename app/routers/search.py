from fastapi import APIRouter, Query
from typing import List
from app.services.search_service import semantic_search

router = APIRouter(prefix="/search", tags=["Search"])

@router.get("/", summary="Semantic search in the knowledge base")
def search(query: str = Query(..., description="Search query"),
           top_k: int = Query(5, ge=1, le=50)) -> List[dict]:
    """
    Performs semantic search over the ingested documents.
    Returns the top-k most relevant results.
    """
    results = semantic_search(query, top_k)
    return {"query": query, "results": results}
