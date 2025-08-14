from dataclasses import dataclass

@dataclass
class Document:
    id: int
    name: str
    content: str
    content_hash: str
    created_at: str

@dataclass
class Chunk:
    id: int
    doc_id: int
    chunk_index: int
    text: str