from app.services.search_service import semantic_search

def answer_question(query: str, context_size: int) -> str:
    """
    A dummy Q&A function.
    Currently, just returns the preview of the most relevant document.
    """
    results = semantic_search(query, top_k=context_size)
    if not results:
        return "No relevant documents found."
    return f"Based on document '{results[0]['filename']}': {results[0]['preview']}"
