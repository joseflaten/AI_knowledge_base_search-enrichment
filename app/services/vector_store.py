import os
import faiss
import numpy as np
from typing import List, Tuple
from app.config import FAISS_INDEX_PATH, EMBED_DIM

class VectorStore:
    def __init__(self, index: faiss.IndexFlatIP, ids: List[int]):
        self.index = index
        self.ids = ids  # maps FAISS position -> chunk_id

    @staticmethod
    def load_or_create():
        if os.path.exists(FAISS_INDEX_PATH):
            index = faiss.read_index(FAISS_INDEX_PATH)
            # IDs