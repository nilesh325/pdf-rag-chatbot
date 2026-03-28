# 🤖 PDF RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot built with Streamlit that lets you upload a PDF and ask questions about its content using Mistral AI.

---

## 🔄 How It Works

```
┌─────────────────────────────────────────────────────────────────────┐
│                        RAG PIPELINE                                 │
└─────────────────────────────────────────────────────────────────────┘

  📄 PDF Upload
       │
       ▼
┌─────────────┐
│  PyPDF2     │  ── Extract raw text from all pages
└─────────────┘
       │
       ▼
┌─────────────────────────┐
│  RecursiveCharacter     │  ── Split text into chunks
│  TextSplitter           │     (1000 chars, 150 overlap)
└─────────────────────────┘
       │
       ▼
┌─────────────────────────┐
│  HuggingFace            │  ── Convert chunks into
│  Embeddings             │     vector representations
└─────────────────────────┘
       │
       ▼
┌─────────────┐
│  FAISS      │  ── Store vectors in
│  VectorDB   │     local vector store
└─────────────┘
       │
       │         ❓ User Question
       │               │
       ▼               ▼
┌─────────────────────────┐
│  Similarity Search      │  ── Find most relevant chunks
│  (FAISS)                │     matching the question
└─────────────────────────┘
       │
       ▼
┌─────────────────────────────────────────────────┐
│              LangGraph StateGraph               │
│                                                 │
│   ┌──────────┐          ┌──────────┐            │
│   │ retrieve │ ───────► │ answer   │            │
│   │  node   │          │  node    │            │
│   └──────────┘          └──────────┘            │
│   Loads matched         Sends docs +            │
│   docs into state       question to LLM         │
└─────────────────────────────────────────────────┘
       │
       ▼
┌─────────────┐
│  Mistral AI │  ── Generate final answer
│  (LLM)      │     based on retrieved docs
└─────────────┘
       │
       ▼
  💬 Answer displayed in Streamlit UI
```

---

## 🗂️ Project Structure

```
RAG/
├── my_chatbot.py          # Main Streamlit app
├── requirements.txt       # Python dependencies

```

---

## ⚙️ Tech Stack

| Component | Library |
|-----------|---------|
| UI | Streamlit |
| PDF Parsing | PyPDF2 |
| Text Splitting | LangChain |
| Embeddings | HuggingFace |
| Vector Store | FAISS |
| Graph Orchestration | LangGraph |
| LLM | Mistral AI |

---

## 🚀 Getting Started

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the app
```bash
streamlit run my_chatbot.py 
```

---

## 💡 Usage

1. Open the app in your browser
2. Upload a PDF file using the sidebar
3. Wait for the PDF to be processed
4. Type your question in the text input
5. Get an AI-generated answer based on your PDF content

---

## 📦 Requirements

```
streamlit
PyPDF2
langchain-text-splitters
langchain-community
langchain-mistralai
langgraph
```
md…]()

