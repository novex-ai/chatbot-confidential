from typing import List

import tiktoken


# https://platform.openai.com/docs/guides/embeddings/second-generation-models
EMBEDDING_MODEL = "text-embedding-ada-002"
EMBEDDING_DIMENSIONS = 1536


_encoder = tiktoken.get_encoding(EMBEDDING_MODEL)


def encode(input: str) -> List[int]:
    return _encoder.encode(input)


def decode(input: List[int]) -> str:
    return _encoder.decode(input)
