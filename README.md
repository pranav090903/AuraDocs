# 📄 AuraDocs: Intelligent Document Intelligence Platform

**AuraDocs** is a next-generation Retrieval-Augmented Generation (RAG) platform that transforms static PDF documents into interactive, searchable knowledge bases. Powered by the Mistral-7B architecture and high-performance vector retrieval, AuraDocs provides instant, context-aware answers with a premium, user-centric interface.

---

## 🚀 Key Features

### 1. **Ultra-Fast Vector Search (FAISS)**
Unlike traditional keyword search, AuraDocs uses **FAISS (Facebook AI Similarity Search)** to understand the semantic meaning of your documents. It doesn't just look for words; it looks for *ideas*.

### 2. **Mistral-7B Conversational Core**
Leveraging the `Mistral-7B-Instruct-v0.2` via Hugging Face Inference API, AuraDocs provides high-reasoning capabilities, ensuring that answers are not just text snippets but coherent, intelligent responses.

### 3. **Asynchronous Architecture**
Built with a **FastAPI** backend, the system handles document processing and query execution asynchronously, ensuring the UI remains responsive even during heavy indexing tasks.

### 4. **Premium Glassmorphic UI**
The frontend is designed with **Streamlit** using custom CSS overrides to provide a "SaaS-grade" experience, featuring glassmorphism, gradients, and smooth transitions.

### 5. **Strict Context Adherence**
AuraDocs is engineered to prevent "hallucinations." If the answer isn't in your document, it won't make one up. It stays loyal to your data.

---

## 🏆 What Makes AuraDocs Different?

Most RAG implementations are simple scripts. AuraDocs is a full-stack platform.

| Feature | Generic RAG | **AuraDocs** |
| :--- | :--- | :--- |
| **Response Tone** | Robotic / Dry | Intelligent & Conversational |
| **Logic Layer** | Simple Search | Semantic Vector Retrieval |
| **Backend** | Single Script | Scalable FastAPI Architecture |
| **UI/UX** | Terminal / Basic | Premium Glassmorphic Web App |
| **Hallucination Control** | Low | High (Strict Document-Only Mode) |

---

## 🛠️ Technology Stack

-   **LLM Engine**: Hugging Face `Mistral-7B-Instruct-v0.2`
-   **Orchestration**: LangChain
-   **Vector Database**: FAISS (Facebook AI Similarity Search)
-   **Embeddings**: `all-MiniLM-L6-v2` (Sentence Transformers)
-   **Backend**: FastAPI
-   **Frontend**: Streamlit
-   **PDF Processing**: PyPDF + Recursive Character Text Splitting

---

## 📦 Installation & Setup

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd AuraDocs
    ```

2.  **Environment Setup**:
    Create a `.env` file in the root directory:
    ```env
    HF_API_KEY=your_huggingface_token
    MODEL_NAME=mistralai/Mistral-7B-Instruct-v0.2
    EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
    CHUNK_SIZE=1000
    CHUNK_OVERLAP=200
    ```

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

---

## 🚦 Running the Application

AuraDocs runs on a client-server architecture:

### 1. Launch the Backend (Server)
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### 2. Launch the Frontend (Client)
```bash
streamlit run streamlit_app.py
```

Access the UI at: `http://localhost:8501`

---

## 🛡️ License
Distributed under the MIT License. See `LICENSE` for more information.

---
**AuraDocs** — *Clarity in every page.*
