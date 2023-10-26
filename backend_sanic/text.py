from typing import List

from langchain.text_splitter import RecursiveCharacterTextSplitter


# TODO find a less heavy text splitter
def split_text_chunks(input: str) -> List[str]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=2048, chunk_overlap=256, length_function=len
    )
    documents = splitter.create_documents([input])
    chunks = [d.page_content for d in documents]
    return chunks
