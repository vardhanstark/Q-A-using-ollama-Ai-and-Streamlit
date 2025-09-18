import streamlit as st
import pandas as pd
from PyPDF2 import PdfReader
import camelot
import os
import ollama
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from streamlit import streamlit as st
#DATA PREPROCESSING -
st.title("Q/A chatbot")
#accept_multiple_files=TRUE because it upload multiple files at atime 
uploaded_files=st.file_uploader(label="upload PDF or Excel files",type=[".pdf",".xls", ".xlsx"],accept_multiple_files=True) 
all_text = ""

if uploaded_files:
    for file in uploaded_files:
        ext = file.name.split(".")[-1].lower()
        if ext == "pdf":
            st.write("PDF selected")
            reader = PdfReader(file)
            for page in reader.pages:
                all_text += page.extract_text() + "\n"
                tables = camelot.read_pdf(file, pages="all", flavor="lattice")
            for i, table in enumerate(tables):
                all_text += f"\n--- PDF Table {i+1} ---\n"
                all_text += table.df.to_string(index=False)
        elif ext in ["xls", "xlsx"]:
            st.write("Excel selected")
            xls = pd.ExcelFile(file)
            for sheet in xls.sheet_names:
                df = pd.read_excel(xls, sheet_name=sheet)
                all_text += f"\n--- Excel Sheet: {sheet} ---\n"
                all_text += df.to_string(index=False)
        else:
            st.error("Unsupported file format")
    st.subheader("Combined Data from All Files")
    st.text_area("Data", all_text, height=400)

else:
    st.info("Please upload a file to continue")
# Save to text file for a copy
with open("combined_output.txt", "w", encoding="utf-8") as f:
    f.write(all_text)

#Chunking
document_text=all_text
# Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = splitter.split_text(all_text)

print(f"Got {len(chunks)} chunks")

# Embeddings
embeddings = OllamaEmbeddings(model="llama3") 
# Vectorstore
#if chunks is because not to get error before we upload the file 
if chunks:
    vectorstore = FAISS.from_texts(chunks, embeddings)
question=st.text_input("enter the question-")
def ask_finance_question(question):
    docs = vectorstore.similarity_search(question, k=3)
    context = "\n\n".join(map(lambda d: d.page_content, docs))
    # Send to Ollama
    prompt = f"""
    You are a financial assistant. 
    Answer the following question using ONLY the context below.
    Context:
    {context}

    Question:
    {question}
    """

    response = ollama.chat(model="llama3", messages=[
        {"role": "user", "content": prompt}
    ])
    Answer=response['message']['content']  
    return Answer

if st.button('Enter'):
    answer=ask_finance_question(question)
    st.write(answer)































