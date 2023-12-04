# Langchain
In VSCode install the following extensions:
1. Python environment manager
2. Python Extension Pack
3. Python Indent

Create a python virtual environment in vscode: python -m venv <env-name>  (use it as workspace)
activate <env-name> 

Now make the following installations using pip install
1. dotenv
2. langchain
3. openai==0.28.1 (existing code will crack for latest versions)
4. chromadb==0.4.15
5. streamlit
6. pypdf
7. docx2txt
8. tiktoken
9. transformers
10. torch

In .env file used to store values of the API tokens for different APIs used.

Bill Extractor App - Returns a .csv file compiling information from various bills that are uploaded.
Chatbot App - is a multidocument chatbot to which one can pose questions related to information contained in the documents uploaded. 
Image-Text App - generates a recipe that can be prepared using ingredients in the uploaded image, suing LLM and Huggingface for image to text translation; needs a huggingface API.
Newsletter App - will generate a short article compiling recent information on a given topic. Internally uses google search for information search using serperapi.


 
