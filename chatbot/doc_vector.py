import os
from dotenv import find_dotenv, load_dotenv
import openai
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.chains.question_answering import load_qa_chain
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA


load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")

#packages to install
#pip install langchain, pypdf, openai, chromadb, tiktoken, docx2txt

llm_model = "gpt-3.5-turbo"
llm = ChatOpenAI(temperature = 0.0, model = llm_model)

#load the pdf file
pf_loader = PyPDFLoader("./chatbot/data/RachelGreenCV.pdf")
documents  = pf_loader.load()

#Split the data into chunks
text_splitter = CharacterTextSplitter(
    chunk_size  = 1000,
    chunk_overlap = 200
)
docs = text_splitter.split_documents(documents)

#create vector db chromadb
vectordb = Chroma.from_documents(
    documents = docs,
    embedding = OpenAIEmbeddings(),
    persist_directory = "./chatbot/data"
)
vectordb.persist()

#RetrievalQA chain to get info from the vectorstore
qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever = vectordb.as_retriever(search_kwargs = {'k': 3}),
    return_source_documents = True
)

result = qa_chain("Who is the CV about?")
#results = qa_chain({'query':"Who is the CV about?"}) #other way of doing it 

print(result['result'])

#Here there is no memory to have a conversation linking to previous chat as well.