import uuid

# Temporary in-memory storage for documents
DOCUMENT_STORE = {}

def ingest_document(filename: str, content: str) -> str:
    """
    Stores document in memory with a generated ID.
    Later, this will also create embeddings and store them in a vector DB.
    """
    doc_id = str(uuid.uuid4())
    DOCUMENT_STORE[doc_id] = {
        "filename": filename,
        "content": content
    }
    return doc_id
