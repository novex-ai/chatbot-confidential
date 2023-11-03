from pathlib import Path
from typing import List, Union

from sanic.log import logger
from sentence_transformers import SentenceTransformer  # type: ignore

import backend_sanic


# https://huggingface.co/spaces/mteb/leaderboard
# https://huggingface.co/thenlper/gte-large
EMBEDDING_MODEL = "thenlper--gte-large"
EMBEDDING_DIMENSIONS = 1024
EMBEDDING_MAX_TOKENS = 512


_model_path = Path(Path(backend_sanic.__path__[0]).parent, "models", EMBEDDING_MODEL)

_embedding_model: SentenceTransformer = None


def strings_to_embeddings(input: Union[str, List[str]]):
    embedding_model = get_embedding_model()
    return embedding_model.encode(input, normalize_embeddings=True)


def get_embedding_model():
    global _embedding_model
    if _embedding_model is None:
        logger.info(f"loading embedding model from {_model_path=}")
        _embedding_model = SentenceTransformer(str(_model_path))
    return _embedding_model
