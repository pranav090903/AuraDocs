from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
import os

from app.rag.loader import load_pdf
from app.rag.splitter import split_documents
from app.rag.vectorstore import create_vectorstore
from app.rag.retriever import get_retriever
from app.rag.chain import build_rag_chain
from app.utils.helpers import save_uploaded_file

router = APIRouter()

class QuestionRequest(BaseModel):
    question: str

VECTORSTORE = None


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    global VECTORSTORE

    file_path = f"data/documents/{file.filename}"
    save_uploaded_file(file, file_path)

    documents = load_pdf(file_path)
    print("Loaded docs:", len(documents))

    chunks = split_documents(documents)
    print("Chunks created:", len(chunks))

    if not chunks:
        return {"error": "No text found in PDF"}

    VECTORSTORE = create_vectorstore(chunks)

    return {"message": "PDF processed successfully"}


@router.post("/ask")
async def ask_question(request: QuestionRequest):
    question = request.question
    global VECTORSTORE

    if VECTORSTORE is None:
        return {"error": "No document uploaded yet"}

    retriever = get_retriever(VECTORSTORE)
    chain = build_rag_chain(retriever)

    answer = chain.invoke(question)

    return {"answer": answer}
