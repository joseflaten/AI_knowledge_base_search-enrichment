from app.services.embeddings import get_embedder
from app.services.vector_store import VectorStore

# Simple dependency factories (could be wired via FastAPI Depends if desired)

def get_vs() -> VectorStore:
    return VectorStore.load_or_create()

def get_embeddings():
    return get_embedder()