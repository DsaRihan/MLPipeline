import os
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# --- Configuration ---
# REPLACE 'your_file.pdf' with the actual name of the PDF you put in the data folder!
PDF_PATH = "data/jobcv.pdf" 
DB_DIR = "chroma_db"

def build_vector_database():
    print(f" Loading document: {PDF_PATH}...")
    
    # 1. Load the PDF
    loader = PyMuPDFLoader(PDF_PATH)
    documents = loader.load()
    print(f"Loaded {len(documents)} pages.")

    # 2. Chunk the Text
    # AI models can't read a whole book at once. We break it into 1000-character chunks.
    # The 'overlap' ensures we don't cut a sentence in half and lose context.
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split the document into {len(chunks)} searchable chunks.")

    # 3. Create the Embeddings Model
    # This downloads a tiny, incredibly fast open-source model that turns text into numbers.
    # It runs entirely locally on your Mac.
    print(" Initializing local embedding model...")
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # 4. Save to Vector Database (ChromaDB)
    # We pass our chunks and our embedding model to Chroma, and tell it to save to our hard drive.
    print(" Saving data to local Chroma database...")
    vector_db = Chroma.from_documents(
        documents=chunks, 
        embedding=embedding_model, 
        persist_directory=DB_DIR
    )
    
    print(" Success! Your vector database is built and ready for the AI.")

if __name__ == "__main__":
    build_vector_database()