
# 📄 RAG-PDF-Chatbot using Google Gemini + LangChain

Empower your PDFs with **conversational intelligence** using Google Gemini and LangChain. This Streamlit app turns static documents into interactive, chat-ready experiences using Retrieval-Augmented Generation (RAG) powered by **Gemini embeddings** and **FAISS vector search**.


---

## 🚀 Features

- ✅ Upload multiple PDFs and chat with them in real-time
- 🧠 Uses **Google Gemini embeddings** for context-rich vectorization
- 🗂️ Stores and searches using **FAISS Vector Store**
- 🤖 RAG-style Q&A with **LangChain QA chains**
- 🔥 Built with **Streamlit** for sleek, interactive UI
- 📚 Tracks conversation history and source PDFs
- 🛡️ Graceful error handling and API validation

---

## 💡 Architecture Overview

```plaintext
PDF(s)
  ↓
Text Extraction (PyPDF2)
  ↓
Chunking (LangChain TextSplitter)
  ↓
Google Generative AI Embeddings (Gemini)
  ↓
FAISS Vector Store
  ↓
User Query → Semantic Search → RAG Chain (LangChain QA)
  ↓
Structured, Accurate Answer
```

---

## 🧰 Tech Stack

| Layer             | Tools Used                                   |
|------------------|----------------------------------------------|
| Frontend         | Streamlit                                    |
| Text Extraction  | PyPDF2                                       |
| NLP Framework    | LangChain                                    |
| Embeddings       | Google Gemini (`models/embedding-001`)       |
| LLM              | Google Gemini Chat (`gemini-2.0-flash`)      |
| Vector DB        | FAISS                                        |

---

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/Shaik-Riyaz-Ahmad/QueryQuill.git
cd QueryQuill
```

2. **Set up a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Add your Google API Key**
You can use a `.env` file or input it directly into the UI.

---

## 🧪 Running the App

```bash
streamlit run main.py
```

Then open your browser to `http://localhost:8501`

---

## 🛠 Usage Instructions

1. Upload one or more PDFs from the sidebar
2. Enter your **Google Gemini API key**
3. Ask any question related to the uploaded documents
4. Get clean, structured answers — instantly!

---

## 📁 Project Structure

```bash
├── app.py                    # Core logic: embeddings, FAISS, chain
├── main.py                   # Streamlit frontend and flow
├── requirements.txt
├── faiss_index/              # Vector store saved locally
├── README.md
```

---

## 🧠 Example Use Cases

- 📑 Academic paper assistant
- 📄 Legal document Q&A
- 📘 Book summarizer chatbot
- 🧾 Invoice explainer for non-tech clients
- 📕 AI-powered resume reader

---

## 🧠 Future Enhancements

- [ ] Multi-LLM support (OpenAI fallback)
- [ ] Chunk-based citation & source tracing
- [ ] Session memory (chat context)
- [ ] Upload via Google Drive
- [ ] PDF summarization & outline generation

---

## 🧬 Behind the Scenes (Core Logic)

### `get_pdf_etext()`
Extracts raw text from uploaded PDF(s).

### `get_text_chunks()`
Splits text into semantically consistent chunks (1000 tokens).

### `get_vetore_chunks()`
Embeds those chunks using **Gemini embeddings**, then stores them in **FAISS**.

### `get_conversational_chain()`
Sets up a structured RAG-style QA chain using LangChain's `load_qa_chain()`.

### `user_input()`
Takes user query → fetches relevant chunks → runs through chain → returns structured output.

---

## 🔐 API Key Handling

This app uses **Google Gemini API** (from [Google Generative AI](https://makersuite.google.com/app)).

> 🔑 Make sure your key has access to `models/embedding-001` and `gemini-2.0-flash`.

You can manually input the key in the Streamlit UI.

---

## 🤝 Contributing

Pull requests are welcome! Let's co-build the future of document understanding.

---

## 🧠 Author

**Shaik Riyaz Ahmad**  
AI Developer | Innovation Enthusiast | Resume-ready Project Builder  
🚀 _"Innovation is rethinking the obvious."_  

---

## ⭐️ Show Your Support

If you find this useful, drop a ⭐️ on the repo and share your feedback. Let's innovate together!

---