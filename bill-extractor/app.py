import streamlit as st 
from helper import *

def main():
    st.set_page_config(page_title = "Bill Extractor")
    st.title("Bill Extractor AI Assisstant.....🤖")
    
    #uploading bills
    pdf_files = st.file_uploader("Upload your bills in PDF format only",
                                 type=["pdf"],
                                 accept_multiple_files= True)
    
    extract_button = st.button("Extract bill data...")
    
    if extract_button:
        with st.spinner("Extracting... please wait..."):
            data_frame = create_docs(pdf_files)
            st.write(data_frame.head())
            data_frame["Amount"] = data_frame["Amount"].astype(float)
            st.write("Total bill amount: ", data_frame['Amount'].sum())
            
            #convert to csv
            convert_to_csv = data_frame.to_csv(index=False).encode("utf-8")
            
            #downloading the csv
            st.download_button(
                "Download data as CSV",
                convert_to_csv, #actual file
                "CSV_Bills.csv", #giving it a name
                "text/csv", #adding the type
                key = "download-csv" #giving it a key 
            )
        st.success("Success!!!")
        

if __name__ == '__main__':
    main()