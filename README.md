# Wand KB Search — AI-Powered Knowledge Base

A professional-grade backend that ingests documents, indexes vector embeddings, performs semantic search, Q&A with citations, 
and runs completeness checks. Built with FastAPI, SQLite, and FAISS.

## Features
- Document ingestion (text + optional file parsing)
- Chunking with overlap
- Embeddings (OpenAI or SBERT — configurable)
- FAISS vector index persisted to disk
- Semantic search with top‑K retrieval
- Q&A with citations (LLM optional fallback)
- Incremental updates via content hash
- Clear, typed API with Pydantic v2

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
cp .env.example .env  # fill OPENAI_API_KEY if using OpenAI
uvicorn app.main:app --reload --port 8000
