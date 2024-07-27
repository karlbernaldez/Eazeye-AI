import os
import pickle
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import CharacterTextSplitter

chunks_cache_path = "text_chunks.pkl"

def load_existing_chunks():
    if os.path.exists(chunks_cache_path):
        with open(chunks_cache_path, 'rb') as f:
            return pickle.load(f)
    return []

def save_chunks_cache(chunks):
    with open(chunks_cache_path, 'wb') as f:
        pickle.dump(chunks, f)

def extract_title(documents):
    if documents and len(documents) > 0:
        return documents[0].page_content.split('\n')[0]
    return "Unknown Title"

def process_new_document(new_document_path):
    loader = UnstructuredFileLoader(new_document_path)
    documents = loader.load()
    title = extract_title(documents)
    text_splitter = CharacterTextSplitter(separator='/n', chunk_size=1000, chunk_overlap=200)
    text_chunks = text_splitter.split_documents(documents)
    return text_chunks, title
