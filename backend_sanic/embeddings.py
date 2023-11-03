from os import environ
from pathlib import Path

from psutil import cpu_count  # type: ignore
from sanic.log import logger
import torch
from transformers import BertTokenizerFast  # type: ignore

import backend_sanic


# Constants from the performance optimization available in onnxruntime
# It needs to be done before importing onnxruntime
environ["OMP_NUM_THREADS"] = str(cpu_count(logical=True))
environ["OMP_WAIT_POLICY"] = "ACTIVE"

from onnxruntime import InferenceSession  # type: ignore # noqa


# https://huggingface.co/spaces/mteb/leaderboard
# https://huggingface.co/thenlper/gte-large
EMBEDDING_MODEL = "thenlper--gte-large/onnx"
EMBEDDING_DIMENSIONS = 1024
EMBEDDING_MAX_TOKENS = 512

_model_path = Path(
    Path(backend_sanic.__path__[0]).parent, "models", EMBEDDING_MODEL, "model.onnx"
)
_tokenizer_path = _model_path.parent

_embedding_model: InferenceSession = None
_tokenizer: BertTokenizerFast = None


def string_to_embeddings(input: str):
    embedding_model = get_embedding_model()
    tokenizer = get_tokenizer()
    model_inputs = tokenizer(
        input, return_tensors="pt", max_length=EMBEDDING_MAX_TOKENS, truncation=True
    )
    inputs_onnx = {k: v.cpu().detach().numpy() for k, v in model_inputs.items()}
    sequence = embedding_model.run(None, inputs_onnx)
    sentence_embeddings = mean_pooling(sequence, inputs_onnx["attention_mask"])
    return sentence_embeddings[0][0].numpy()


def get_embedding_model():
    global _embedding_model
    if _embedding_model is None:
        logger.info(f"loading embedding model from {_model_path=}")
        _embedding_model = InferenceSession(
            str(_model_path),
            providers=["CPUExecutionProvider"],
        )
        logger.info(f"loaded {_embedding_model=}")
    return _embedding_model


def get_tokenizer():
    global _tokenizer
    if _tokenizer is None:
        _tokenizer = BertTokenizerFast.from_pretrained(str(_tokenizer_path))
    return _tokenizer


def mean_pooling(model_output, attention_mask):
    model_output = torch.from_numpy(model_output[0])
    token_embeddings = (
        model_output  # First element of model_output contains all token embeddings
    )
    attention_mask = torch.from_numpy(attention_mask)
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size())
    sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1)
    sum_mask = torch.clamp(input_mask_expanded.sum(1), min=1e-9)
    return sum_embeddings / sum_mask, input_mask_expanded, sum_mask
