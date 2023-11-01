from typing import List

from langchain.text_splitter import RecursiveCharacterTextSplitter

from backend_sanic.embeddings import EMBEDDING_MAX_TOKENS

# approsimate size of a chunk of text in characters
SPLIT_TEXT_SIZE = EMBEDDING_MAX_TOKENS * 3.5
SPLIT_TEXT_OVERLAP = EMBEDDING_MAX_TOKENS / 2


# TODO find a less heavy text splitter
def split_text_chunks(input: str) -> List[str]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=SPLIT_TEXT_SIZE,
        chunk_overlap=SPLIT_TEXT_OVERLAP,
        length_function=len,
    )
    documents = splitter.create_documents([input])
    chunks = [d.page_content for d in documents]
    return chunks
