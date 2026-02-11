# 🎲 Game Rules RAG Assistant
An AI-powered assistant that uses **Retrieval-Augmented Generation (RAG)** to answer complex questions about board game rules (like UNO Flip!) with 100% accuracy and source citations.

## 🚀 Features
* **Local-First AI:** Powered by **Ollama (Llama 3)** for privacy and zero cost.
* **Vector Search:** Uses **ChromaDB** to retrieve relevant rule snippets from PDF documents.
* **Source Transparency:** Every answer includes exact page references from the source manual.
* **Chat Memory:** Remembers the context of your previous questions (e.g., "What about the Dark Side?").

## 🛠️ Tech Stack
* **LLM:** Ollama (Llama 3)
* **Framework:** LangChain v0.3
* **Database:** ChromaDB (Vector Store)
* **Frontend:** Streamlit
* **Environment:** Python 3.12

## 📦 Installation
1. Install [Ollama](https://ollama.com/) and run `ollama pull llama3`.
2. Clone this repo and create a virtual environment:
   ```bash
   python3 -m venv .rag-venv
   source .rag-venv/bin/activate
   pip install -r requirements.txt

3. Initialize the database:
   python populate_database.py  

4. Run the app:
   streamlit run app.py
