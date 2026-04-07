import streamlit as st
from langchain_community.llms import Ollama
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# --- THE NEW FIX IS RIGHT HERE ---
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
# ---------------------------------

from langchain_core.prompts import PromptTemplate

# --- UI Configuration ---
st.set_page_config(page_title="My AI Resume App", page_icon="🤖")
st.title("🤖 Chat with my Document")

# --- Initialize Pipeline ---
@st.cache_resource
def load_pipeline():
    # 1. Load the exact same embedding model we used in ingest.py
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # 2. Connect to our local Chroma database
    vector_db = Chroma(persist_directory="chroma_db", embedding_function=embedding_model)
    
    # 3. Create the Retriever
    retriever = vector_db.as_retriever(search_kwargs={"k": 3})
    
    # 4. Connect to the Tiny Llama Model
    llm = Ollama(model="llama3.2:1b")
    
    # 5. Build the LangChain Pipeline
    prompt = PromptTemplate.from_template(
        "Answer the question based only on the following context:\n\n{context}\n\nQuestion: {input}"
    )
    document_chain = create_stuff_documents_chain(llm, prompt)
    qa_chain = create_retrieval_chain(retriever, document_chain)
    
    return qa_chain

qa_chain = load_pipeline()

# --- Chat Interface ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask a question about the document...")

if user_input:
    # 1. Show user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # 2. Generate and show AI response
    with st.chat_message("assistant"):
        with st.spinner("Searching document and thinking..."):
            response = qa_chain.invoke({"input": user_input})
            answer = response["answer"]
            st.markdown(answer)
            
    # 3. Save to history
    st.session_state.messages.append({"role": "assistant", "content": answer})