import numpy as np
from app.config import EMBED_BACKEND, OPENAI_EMBED_MODEL

_openai_client = None
_sbert_model = None

class EmbeddingsProvider:
    def embed_texts(self, texts):
        raise NotImplementedError

class OpenAIEmbeddings(EmbeddingsProvider):
    def __init__(self, model: str = OPENAI_EMBED_MODEL):
        global _openai_client
        from openai import OpenAI
        _openai_client = _openai_client or OpenAI()
        self.client = _openai_client
        self.model = model

    def embed_texts(self, texts):
        resp = self.client.embeddings.create(model=self.model, input=texts)
        vecs = [np.array(d.embedding, dtype=np.float32) for d in resp.data]
        return np.vstack(vecs)

class SBERTEmbeddings(EmbeddingsProvider):
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        global _sbert_model
        from sentence_transformers import SentenceTransformer
        _sbert_model = _sbert_model or SentenceTransformer(model_name)
        self.model = _sbert_model

    def embed_texts(self, texts):
        arr = self.model.encode(texts, batch_size=32, show_progress_bar=False, normalize_embeddings=True)
        return np.array(arr, dtype=np.float32)

def get_embedder() -> EmbeddingsProvider:
    if EMBED_BACKEND == "openai":
        return OpenAIEmbeddings()
    elif EMBED_BACKEND == "sbert":
        return SBERTEmbeddings()
    else:
        raise RuntimeError(f"Unsupported EMBEDDINGS_BACKEND={EMBED_BACKEND}")