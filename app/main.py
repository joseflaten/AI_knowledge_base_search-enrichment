from fastapi import FastAPI
from app.routers import health, docs, search, qa

app = FastAPI(title="Wand KB Search", version="0.1.0")

app.include_router(health.router)
app.include_router(docs.router, prefix="/api")
app.include_router(search.router, prefix="/api")
app.include_router(qa.router, prefix="/api")