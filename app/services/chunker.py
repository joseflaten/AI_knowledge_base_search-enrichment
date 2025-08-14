from typing import List

def simple_word_chunk(text: str, max_tokens: int, overlap: int) -> List[str]:
    words = text.split()
    if not words:
        return []
    chunks = []
    i = 0
    step = max(1, max_tokens - overlap)
    while i < len(words):
        chunk_words = words[i : i + max_tokens]
        chunks.append(" ".join(chunk_words))
        i += step
    return chunks