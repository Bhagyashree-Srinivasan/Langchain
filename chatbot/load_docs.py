from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import Docx2txtLoader
from langchain.document_loaders import TextLoader
import streamlit as st 
import os

@st.cache_data() #decorator run the funtion only once until there is a change in the value
def load_docs():
    documents = []
    for file in os.listdir('C:/Desktop/Langchain-Practice/chatbot/docs'):
        if file.endswith('.pdf'):
            pdf_path = "C:/Desktop/Langchain-Practice/chatbot/docs/" + file
            loader = PyPDFLoader(pdf_path)
            documents.extend(loader.load())
        elif file.endswith('.docx') or file.endswith('.doc'):
            doc_path = "C:/Desktop/Langchain-Practice/chatbot/docs/" + file
            loader = Docx2txtLoader(doc_path)
            documents.extend(loader.load())
        elif file.endswith('.txt'):
            text_path = "C:/Desktop/Langchain-Practice/chatbot/docs/" + file
            loader = TextLoader(text_path)
            documents.extend(loader.load())
    
    return documents
            