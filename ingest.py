import os
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# --- Configuration ---

PDF_PATH = "data/jobcv.pdf" 
DB_DIR = "chroma_db"

def build_vector_database():
    print(f" Loading document: {PDF_PATH}...")
    
    loader = PyMuPDFLoader(PDF_PATH)
    documents = loader.load()
    print(f"Loaded {len(documents)} pages.")

    # Chunk the Text
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split the document into {len(chunks)} searchable chunks.")

    # Embeddings Model
    print(" Initializing local embedding model...")
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # Save to Vector Database (ChromaDB)
    print(" Saving data to local Chroma database...")
    vector_db = Chroma.from_documents(
        documents=chunks, 
        embedding=embedding_model, 
        persist_directory=DB_DIR
    )
    
    print(" Success! Your vector database is built and ready for the AI.")

if __name__ == "__main__":
    build_vector_database()