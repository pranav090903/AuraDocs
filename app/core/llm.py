from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from app.config.settings import settings

def get_llm():
    llm = HuggingFaceEndpoint(
        repo_id=settings.MODEL_NAME,
        task="conversational",
        huggingfacehub_api_token=settings.HF_API_KEY,
        temperature=0.3,
        max_new_tokens=512,
    )
    return ChatHuggingFace(llm=llm)
