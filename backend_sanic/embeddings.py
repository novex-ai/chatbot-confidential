import os
from pathlib import Path
from typing import List, Optional, Union

from huggingface_hub import snapshot_download  # type: ignore
from sentence_transformers import SentenceTransformer  # type: ignore


# https://huggingface.co/spaces/mteb/leaderboard
EMBEDDING_MODEL = "BAAI/bge-large-en-v1.5"
EMBEDDING_MODEL_VERSION = "0e76a14a47548a15db4aa81d7fb50dba76d5e2c6"
EMBEDDING_DIMENSIONS = 1024

APP_MODEL_CACHE_PATH = os.environ.get("APP_MODEL_CACHE_PATH", "")
if not APP_MODEL_CACHE_PATH:
    raise Exception("APP_MODEL_CACHE_PATH environment variable not set")

_cache_folder_path: Optional[Path] = None
_embedding_model: SentenceTransformer = None


def strings_to_embeddings(input: Union[str, List[str]]):
    embedding_model = get_embedding_model()
    return embedding_model.encode(input, normalize_embeddings=True)


def precache_model():
    cache_folder_path = get_cache_folder_path()
    snapshot_download(
        EMBEDDING_MODEL,
        cache_dir=str(cache_folder_path),
        library_version=EMBEDDING_MODEL_VERSION,
        library_name="cached-embedding-model",
    )


def get_embedding_model():
    global _embedding_model
    if _embedding_model is None:
        precache_model()
        cache_folder_path = get_cache_folder_path()
        _embedding_model = SentenceTransformer(
            EMBEDDING_MODEL, cache_folder=str(cache_folder_path)
        )
    return _embedding_model


def get_cache_folder_path():
    global _cache_folder_path
    if _cache_folder_path is None:
        _cache_folder_path = Path(APP_MODEL_CACHE_PATH, "models")
        _cache_folder_path.mkdir(parents=True, exist_ok=True)
    return _cache_folder_path
