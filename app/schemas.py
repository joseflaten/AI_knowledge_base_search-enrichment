from typing import List, Optional
from pydantic import BaseModel, Field

class DocumentIn(BaseModel):
    name: str = Field(..., examples=["mydoc"])
    content: str
    max_tokens: int | None = None
    overlap: int | None = None

class DocOut(BaseModel):
    doc_id: int
    inserted: bool
    chunks: int

class SearchQuery(BaseModel):
    query: str
    top_k: int = 5

class SearchHit(BaseModel):
    doc_id: int
    chunk_id: int
    score: float
    text: str

class SearchResponse(BaseModel):
    hits: List[SearchHit]

class QAQuery(BaseModel):
    question: str
    top_k: int = 5

class QAResponse(BaseModel):
    answer: str
    sources: List[SearchHit]

class CompletenessResponse(BaseModel):
    doc_id: int
    present: List[str]
    missing: List[str]