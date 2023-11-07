from backend_sanic.embeddings import EMBEDDING_MAX_TOKENS

# approsimate size of a chunk of text in characters
SPLIT_TEXT_SIZE = int(EMBEDDING_MAX_TOKENS * 3.5)
SPLIT_TEXT_OVERLAP = int(EMBEDDING_MAX_TOKENS / 2)


def split_text_chunks(
    input: str,
    chunk_size: int = SPLIT_TEXT_SIZE,
    chunk_overlap: int = SPLIT_TEXT_OVERLAP,
):
    start = 0
    while start < len(input) - 1:
        end = start + chunk_size
        yield input[start:end]
        start += chunk_size - chunk_overlap
