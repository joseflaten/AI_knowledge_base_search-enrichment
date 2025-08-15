from fastapi import APIRouter, Query
from typing import List
from app.services.search_service import semantic_search
from app.schemas import SearchResponse, SearchHit

router = APIRouter(prefix="/search", tags=["Search"])

@router.get("/", summary="Semantic search in the knowledge base", response_model=SearchResponse)
def search(query: str = Query(..., description="Search query"),
           top_k: int = Query(5, ge=1, le=50)) -> SearchResponse:
    """
    Performs semantic search over the ingested documents.
    Returns the top-k most relevant results.
    """
    results: List[SearchHit] = semantic_search(query, top_k)
    return SearchResponse(query=query, results=results)
