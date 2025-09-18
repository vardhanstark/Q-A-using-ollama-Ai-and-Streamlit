🚀 Final Setup & Run Guide (with Versions)
1. 🐍 Create & Activate Virtual Environment
python -m venv venv


Activate it:

Windows (PowerShell)

venv\Scripts\activate


Mac/Linux

source venv/bin/activate
---------------------------------------------------------------
2. 📦 Install Python Libraries

Here’s a requirements.txt with stable versions:

streamlit==1.37.0
pandas==2.2.2
PyPDF2==3.0.1
camelot-py==0.11.0
ollama==0.1.7
langchain==0.2.14
langchain-community==0.2.12
langchain-ollama==0.1.3
faiss-cpu==1.8.0.post1


Install:

pip install -r requirements.txt
-----------------------------------------------------------------
3. 🤖 Setup Ollama

Download Ollama: https://ollama.com/download

Pull the Llama 3 model:

ollama pull llama3
-------------------------------------------------------------------
4. ▶️ Run the Streamlit App

In your project folder:

streamlit run app.py


The app will start at:
👉 http://localhost:8501
--------------------------------------------------------------------
5. 📝 How to Use

Upload PDF or Excel files.

The app extracts text and tables.

Data is chunked using langchain and stored in FAISS vector DB.

Ask your financial question in the text box.

The system queries Ollama Llama3 and gives context-based answers.
