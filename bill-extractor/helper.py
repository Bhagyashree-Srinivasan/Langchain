from langchain.llms.openai import OpenAI
from pypdf import PdfReader
import pandas as pd
import re
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType

import openai
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")

#chat  = ChatOpenAI(temperature = 0.7, model = "gpt-3.5-turbo")

#Extract info from the PDF file
def extract_info_from_pdf(pdf_doc):
    text=""
    pdf_reader = PdfReader(pdf_doc)
    for page in pdf_reader.pages:
        text += page.extract_text()
    
    return text

#extract data from text
def extracted_data(pages_data):
    template = """Extarct all the following values: Invoice ID, Description, Issue date, Unit Price, 
    Amount, Bill For, From and Terms from: {pages}
    
    Expected output: Remove any dollar symbols and output should be like {{'Invoice ID': '1001329','Description': 'water bill', 'Unit Price': '500','Issue Date': '5/4/2023','Amount': '1100.00', 'Bill For': 'james', 'From': 'excel company', 'Terms': 'pay this now'}}
    """
    
    prompt_template = PromptTemplate(input_variables=["pages"],
                                     template = template)
    
    llm = OpenAI(temperature=0.7)
    full_response = llm(prompt_template.format(pages=pages_data))
    
    return full_response

#create documents from the uploaded pdfs
def create_docs(user_pdf_list):
    df = pd.DataFrame({'Invoice ID': pd.Series(dtype='int'),
                   'Description': pd.Series(dtype='str'),
                   'Issue Date': pd.Series(dtype='str'),
	              'Unit Price': pd.Series(dtype='str'),
                   'Amount': pd.Series(dtype='int'),
                   'Bill For': pd.Series(dtype='str'),
	                'From': pd.Series(dtype='str'),
                   'Terms': pd.Series(dtype='str')
                    
                    })
    
    for filename in user_pdf_list:
        
        #print(filename)
        raw_data = extract_info_from_pdf(filename)
        #print("extracted raw data")
        #print(raw_data)
        
        llm_extracted_data = extracted_data(raw_data)
        print("llm extracted data")
        print(llm_extracted_data)
        
        pattern = r'{(.+)}' #captures 1 or more of any character, except newline
        match = re.search(pattern, llm_extracted_data, re.DOTALL) #dotall added to match \n character as well
        #print(match)
        if match:
            extracted_text = match.group(1)
            #converting the extracted text to a dictionary
            data_dict = eval('{'+extracted_text+'}')
            print(data_dict)
        else:
            print("No Match Found")
            continue
            
        df = pd.concat([df, pd.DataFrame([data_dict])], ignore_index = True)
        
        print("*************DONE*******************")
    df.head()
    return df


#def main(): 
#    f = []
#    for (dirpath, dirnames, filenames) in os.walk("./bill-extractor/data"):
#        print(filenames)
#        for i in filenames:
#            f.append(os.path.join(dirpath, i))
#    df = create_docs(f)
#    print(df)
             
#if __name__ == '__main__':
#    main()