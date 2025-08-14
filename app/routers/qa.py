from fastapi import APIRouter, Query
from app.services.qa_service import answer_question

router = APIRouter(prefix="/qa", tags=["Question Answering"])

@router.get("/", summary="Answer questions from the knowledge base")
def qa(query: str = Query(..., description="Your question"),
       context_size: int = Query(3, ge=1, le=10)) -> dict:
    """
    Uses semantic search to retrieve relevant documents and generate an answer.
    """
    answer = answer_question(query, context_size)
    return {"question": query, "answer": answer}
