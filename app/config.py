import os
from dotenv import load_dotenv

load_dotenv()

EMBED_BACKEND = os.getenv("EMBEDDINGS_BACKEND", "openai").lower()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_EMBED_MODEL = os.getenv("OPENAI_EMBED_MODEL", "text-embedding-3-small")
OPENAI_CHAT_MODEL = os.getenv("OPENAI_CHAT_MODEL", "gpt-4o-mini")
ENABLE_QA_LLM = bool(int(os.getenv("ENABLE_QA_LLM", "1")))

KB_DB_PATH = os.getenv("KB_DB_PATH", "./kb.sqlite")
FAISS_INDEX_PATH = os.getenv("FAISS_INDEX_PATH", "./kb.index.faiss")
EMBED_DIM = int(os.getenv("EMBED_DIM", "1536"))

CHUNK_MAX_TOKENS = int(os.getenv("CHUNK_MAX_TOKENS", "500"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "50"))