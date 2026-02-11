🎲 Game Rules Assistant

The Problem: We’ve all been there midway through a heated game of UNO Flip or Monopoly, someone plays a move that feels like "cheating." You know there's a specific rule for this situation, but nobody wants to stop the game for 10 minutes to read a PDF manual. An d also some times itm can be very tricky to find the exact rule from the rulebook.


The Solution: I built the Game Rules Assistant to act as an instant, "unbiased referee." Instead of scrolling through PDFs, players can ask natural questions and get answers grounded strictly in the official documentation, complete with page citations to settle the debate instantly.


🛠️ Project Architecture 
I modularized this project to follow industry standards for AI applications, separating the data processing from the front-end interface:

app.py: The "Face" of the project. I used Streamlit to build a responsive chat interface. It manages Session State, which allows the AI to remember the context of the conversation (so you can ask follow-up questions without repeating yourself).

populate_database.py: The ingestion engine. This script automates the heavy lifting: it loads the PDFs, breaks the text into overlapping chunks (to ensure no context is lost at the edges of a page), and initializes the ChromaDB vector store.

get_embedding_function.py: A dedicated utility to ensure consistency. By centralizing the embedding logic here, I ensure that both the data ingestion and the user queries use the exact same mathematical model (nomic-embed-text), which is critical for search accuracy.

query_data.py: The brain of the RAG (Retrieval-Augmented Generation) logic. It calculates the "distance" between the user's question and the stored rule chunks to find the most relevant information before passing it to the LLM.

test_rag.py: My quality assurance tool. I implemented a testing suite to verify that the system retrieves the correct information for known tricky rules, ensuring the assistant remains reliable as the codebase grows.

🚀 Key Technical Features
Local-First Privacy: Powered by Ollama. The entire system runs on your local machine, meaning no data is sent to external APIs and the system works offline. And additionally it is free and costs you nothing.

Grounded Responses: To minimize "hallucinations," the LLM is strictly instructed only to answer using the provided context. If the answer isn't in the rules, it will say so.

Verification (Source Citations): Every response includes the exact source file and page number, allowing players to verify the rule in the actual manual if needed.

Vector Search: Unlike a simple "Ctrl+F" search, this uses Semantic Search to find answers even if the user uses different wording than the manual.

📦 Getting Started
1. Prerequisites
Install Ollama

Pull the necessary models:

ollama pull llama3

ollama pull nomic-embed-text

2. Setup & Run
Environment: python3 -m venv .rag-venv

   source .rag-venv/bin/activate
   
   pip install -r requirements.txt
   

Ingestion: Place your rulebook PDFs in the data/ folder and run: python3 populate_database.py

Launch: streamlit run app.py

📈 Future Roadmap
Hybrid Search: Adding keyword matching to improve retrieval for specific game-specific terminology.

Multi-Document Support: Improving the system's ability to distinguish between different game versions (e.g., UNO vs. UNO Flip) in the same database.

