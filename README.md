Content Engine – AI/ML Document Comparison Tool

📄 Overview

This project builds a Content Engine that:
	•	Ingests multiple PDF documents,
	•	Generates local embeddings using sentence-transformers,
	•	Indexes content in a FAISS vector store,
	•	Provides a retrieval-based querying interface,
	•	Runs fully offline with no API dependency.

⸻

🚀 Features
	•	Multi-PDF ingestion
	•	Local embedding generation with all-MiniLM-L6-v2
	•	FAISS vector storage (to be added)
	•	Raw retrieval of relevant document chunks
	•	Streamlit UI (to be added)
	•	Optional local LLM generation (to be added)

⸻

🛠️ Tech Stack
	•	LlamaIndex
	•	Sentence-Transformers (all-MiniLM-L6-v2)
	•	FAISS
	•	Streamlit (planned)
	•	Python 3.13
 
🧑‍💻 How to Run

1. Clone the Repositorygit

clone https://github.com/yourusername/content-engine.git
cd content-engine

2. Set Up Environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt  # Or manually install packages

3. Add Your PDFs

Place your PDF documents in the /pdfs directory.

4. Run the Model Script
python3 model.py
📌 Current Status

✅ Working Retrieval Pipeline
🟡 FAISS Persistence - Next
🟡 Streamlit UI - Next
🟡 Local LLM Integration - Next

