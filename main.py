import streamlit as st
from datetime import datetime

# Import your core functions from the main script
from app import user_input  # replace 'your_main_script' with the actual Python filename (without .py)

# Page config
st.set_page_config(page_title="📚 PDF AI Chatbot", layout="wide")

# --- Title and description
st.title("📄 PDF ChatBot using Google Gemini + LangChain")
st.markdown("Upload any PDF, ask questions, and get accurate answers extracted from your document using AI.")

# --- Sidebar for inputs
st.sidebar.header("🔧 Configuration")

# API Key Input
api_key = st.sidebar.text_input("Enter your Google API Key:", type="password")

# Model Selector
model_name = st.sidebar.selectbox("Choose the AI Model:", options=["Google AI"], index=0)

# File uploader
pdf_docs = st.sidebar.file_uploader("Upload your PDF files here:", accept_multiple_files=True, type=["pdf"])

# --- Main Interface
st.subheader("💬 Ask a question about your PDF")
user_question = st.text_input("Type your question here...")

# Initialize session state for conversation history
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

# Button to process
if st.button("Get Answer"):
    if not api_key or not pdf_docs:
        st.warning("Please provide both the API key and PDF file(s).")
    elif not user_question.strip():
        st.warning("Please enter a question.")
    else:
        user_input(
            user_question=user_question,
            model_name=model_name,
            api_key=api_key,
            pdf_docs=pdf_docs,
            conversation_history=st.session_state.conversation_history
        )

# --- Display Conversation History
if st.session_state.conversation_history:
    st.markdown("---")
    st.subheader("🧾 Conversation History")

    for idx, (question, answer, model, timestamp, pdf_name) in enumerate(reversed(st.session_state.conversation_history)):
        with st.expander(f"📌 {timestamp} - Q: {question}"):
            st.markdown(f"**Model:** {model}")
            st.markdown(f"**PDFs used:** {pdf_name}")
            st.markdown(f"**Answer:** {answer}")
