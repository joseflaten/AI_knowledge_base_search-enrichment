from typing import List
from app.services.ingestion_service import DOCUMENT_STORE

def semantic_search(query: str, top_k: int) -> List[dict]:
    """
    A dummy search implementation.
    For now, it returns documents that contain the query string.
    """
    results = []
    for doc_id, doc in DOCUMENT_STORE.items():
        if query.lower() in doc["content"].lower():
            results.append({
                "doc_id": doc_id,
                "filename": doc["filename"],
                "preview": doc["content"][:200]  # first 200 chars
            })
    return results[:top_k]
