# 📄 ChatPDF – End-to-End RAG Application with Streamlit & LangChain

ChatPDF is a **full end-to-end Retrieval-Augmented Generation (RAG) application** that allows users to upload PDF documents and ask natural language questions.  
The system retrieves relevant content from the PDF using **FAISS vector search** and generates answers using **LLMs (OpenAI or Google Gemini)**.

This project is built using the **latest LangChain Runnable API**, optimized with **Streamlit caching**, and designed to be **cost-efficient, scalable, and resume-ready**.

---

## 🔥 Why This Project?

- Demonstrates **real-world RAG architecture**
- Handles **API quota limitations** correctly
- Uses **local embeddings** to avoid cost issues
- Shows **production-level optimization**
- Ideal for **Data Scientist / ML Engineer / GenAI roles**

---

## ✨ Key Features

- 📂 Upload and process PDF documents
- 🔍 Semantic search using FAISS
- 🧠 Local HuggingFace embeddings (no API cost)
- 🤖 LLM support:
  - OpenAI GPT models
  - Google Gemini
- ⚡ Fast performance with Streamlit caching
- 🔐 Secure environment variable handling
- 🏗️ Clean, modular, maintainable code
- 💼 Resume and interview ready

---

## 🧠 End-to-End Architecture

User Uploads PDF
↓
PDF Text Extraction (pypdf)
↓
Text Chunking (CharacterTextSplitter)
↓
Local Embeddings (HuggingFace)
↓
FAISS Vector Store
↓
Retriever (Top-K Similarity Search)
↓
Prompt + Context
↓
LLM (OpenAI / Gemini)
↓
Answer Displayed in Streamlit UI


---

## 🛠️ Tech Stack

| Layer | Technology |
|-----|-----------|
Frontend | Streamlit |
LLM Orchestration | LangChain (Runnable API) |
Vector Store | FAISS |
Embeddings | HuggingFace Sentence Transformers |
LLMs | OpenAI GPT / Google Gemini |
Language | Python |

---

## 📂 Project Structure

chatpdf/
│
├── chatbot.py # Main Streamlit application
├── requirements.txt # Project dependencies
├── .gitignore # Ignored files & secrets
├── .env # API keys (not committed)
├── README.md # Project documentation
└── venv/ # Virtual environment (ignored)

---

## ⚙️ Installation (End-to-End)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/chatpdf-streamlit-langchain.git
cd chatpdf-streamlit-langchain
Create Virtual Environment (Windows)
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

📦 requirements.txt
streamlit
pypdf
python-dotenv

langchain
langchain-core
langchain-community
langchain-text-splitters

langchain-openai
langchain-google-genai

sentence-transformers
faiss-cpu

🔐 Environment Variables Setup

Create a .env file in the project root:

OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key


⚠️ Never commit .env to GitHub
(It is already ignored via .gitignore)

▶️ Run the Application
streamlit run chatbot.py


Open in browser:

http://localhost:8501

🧪 How the Application Works (Step-by-Step)

User uploads a PDF

Text is extracted using pypdf

Text is split into overlapping chunks

Chunks are embedded using local HuggingFace embeddings

FAISS indexes the embeddings

User asks a question

Relevant chunks are retrieved

LLM generates an answer using retrieved context

Answer is displayed in the UI

⚡ Performance Optimizations

Cached PDF loading (st.cache_data)

Cached text splitting

Cached FAISS vector store (st.cache_resource)

Prevents recomputation on every UI interaction

🚨 Common Issues & Fixes
❌ App is slow

✅ Fixed using Streamlit caching

❌ OpenAI / Gemini quota exceeded

✅ Local HuggingFace embeddings used

❌ LangChain import errors

✅ Migrated to latest modular LangChain packages

❌ Windows pip install errors

✅ Single-line pip command used

🧠 Design Decisions (Important)

Local embeddings → avoids billing & rate limits

Runnable API → future-proof LangChain usage

FAISS → fast similarity search

Environment-based secrets → secure & professional

📌 Resume Bullet (Use This)

Built an end-to-end ChatPDF application using Streamlit, LangChain, FAISS, and HuggingFace embeddings to enable retrieval-augmented question answering over PDF documents, optimizing performance with caching and modern Runnable architecture.

🚀 Future Enhancements

Streaming token responses

Source citations (page numbers)

Conversational memory

Multi-document support

Cloud deployment (Streamlit Cloud / Render)

📜 License

MIT License

🙌 Acknowledgements

Streamlit

LangChain

HuggingFace

FAISS


---

## ✅ FINAL RESULT

✔ Complete end-to-end documentation  
✔ Recruiter-friendly  
✔ Clear execution flow  
✔ Explains **why**, not just **how**  
✔ Professional GitHub presence

## 📸 Application Screenshots

### 🏠 Home Screen
![Home Screen](assets/front_end.png)


If you want next:
- **`DEPLOY README`** → Add deployment steps  
- **`ARCH DIAGRAM`** → Visual diagram for README  
- **`RESUME SECTION`** → Full resume project write-up  

If someone like this github repo and feels useful, stay connected.
