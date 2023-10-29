import os
from pathlib import Path
from typing import List, Union

from sentence_transformers import SentenceTransformer  # type: ignore


# https://huggingface.co/spaces/mteb/leaderboard
EMBEDDING_MODEL = "BAAI/bge-large-en-v1.5"
EMBEDDING_DIMENSIONS = 1024

APP_DATA_PATH = os.environ.get("APP_DATA_PATH", "")
if not APP_DATA_PATH:
    raise Exception("APP_DATA_PATH environment variable not set")

_cache_path = Path(APP_DATA_PATH, "models")
_cache_path.mkdir(parents=True, exist_ok=True)

_embedding_model = SentenceTransformer(EMBEDDING_MODEL, cache_folder=str(_cache_path))


def strings_to_embeddings(input: Union[str, List[str]]):
    return _embedding_model.encode(input, normalize_embeddings=True)
