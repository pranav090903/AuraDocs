import os
from dotenv import load_dotenv
load_dotenv()

class settings:
    HF_API_KEY=os.getenv("HF_API_KEY")
    MODEL_NAME=os.getenv("MODEL_NAME")
    EMBEDDING_MODEL=os.getenv("EMBEDDING_MODEL")
    VECTOR_DB_PATH=os.getenv("VECTOR_DB_PATH")
    CHUNK_SIZE=int(os.getenv("CHUNK_SIZE",1000))
    CHUNK_OVERLAP=int(os.getenv("CHUNK_OVERLAP",200))
    TOP_K=int(os.getenv("TOP_K",4))

settings=settings()