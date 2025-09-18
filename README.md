## Q/A Finance Management System
---------------------------------------------------------------

## 1.📂 Project Structure
```
├── main.py # Main Python script
├── requirements.txt # Project dependencies
└── README.md # Project documentation
```
----------------------------------------------------------------
##2. 🤖 Setup Ollama

Download Ollama: https://ollama.com/download

Pull the Llama 3 model:

ollama pull llama3
-------------------------------------------------------------------
##3. ▶️ Run the Streamlit App

In your project folder:

streamlit run app.py


The app will start at:
👉 http://localhost:8501
--------------------------------------------------------------------
##4. 📝 How to Use

Upload PDF or Excel files.

The app extracts text and tables.

Data is chunked using langchain and stored in FAISS vector DB.

Ask your financial question in the text box.

The system queries Ollama Llama3 and gives context-based answers.
