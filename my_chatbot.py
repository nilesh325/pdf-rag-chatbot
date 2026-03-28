import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_mistralai import ChatMistralAI
from langgraph.graph import StateGraph  

mistral_api_key = "your_mistral_api_key_here"

st.header("My Chatbot")
#Sidebar
with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader("Upload a PDF file and start asking questions", type="pdf")

#1) Upload PDF and extract text
if file is not None:
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n"],   
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )
#2) Spliting text into chunks 
    chunks = text_splitter.split_text(text)

#3)Creating embeddings 
    embeddings = HuggingFaceEmbeddings()

#4)store in vector database
    vector_store = FAISS.from_texts(chunks, embeddings)

#5)Ask questions
    user_question = st.text_input("Type your question here")

    if user_question:
#6) Similarity search in vector database
        match = vector_store.similarity_search(user_question)

        llm = ChatMistralAI(
            mistral_api_key=mistral_api_key,
            temperature=0.7,
            max_tokens=1000,
            model="mistral-tiny"
        )

#7) Create a graph to retrieve relevant chunks and generate an answer
        graph = StateGraph(dict)

        def retrieve(state):
            return {"docs": match}

        def answer(state):
            docs = state["docs"]
            response = llm.invoke(
                f"Answer the question based on these docs:\n{docs}\n\nQuestion: {user_question}"
            )
            return {"answer": response}

        graph.add_node("retrieve", retrieve)
        graph.add_node("answer", answer)
        graph.add_edge("retrieve", "answer")
        graph.set_entry_point("retrieve")
        graph.set_finish_point("answer")

        compiled = graph.compile()
        result = compiled.invoke({})
        st.write(result["answer"].content)  












    
