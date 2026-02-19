from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="AuraDocs API",
    description="Advanced RAG Engine powered by LangChain & HuggingFace",
    version="1.0.0"
)

app.include_router(router)
