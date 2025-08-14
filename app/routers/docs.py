from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.ingestion_service import ingest_document
from typing import Dict

router = APIRouter(prefix="/docs", tags=["Documents"])

@router.post("/ingest", summary="Upload and ingest a document")
async def ingest_doc(file: UploadFile = File(...)) -> Dict:
    """
    Ingest a document into the knowledge base.
    Stores raw text and vector embeddings.
    """
    try:
        content = await file.read()
        filename = file.filename

        if not content.strip():
            raise HTTPException(status_code=400, detail="Empty file uploaded")

        result = ingest_document(filename, content.decode("utf-8"))
        return {"message": "Document ingested", "doc_id": result}

    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="File encoding not supported")
