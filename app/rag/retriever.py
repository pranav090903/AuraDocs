from app.config.settings import settings

def get_retriever(vectorstore):
    return vectorstore.as_retriever(
        search_kwargs={"k": settings.TOP_K}
    )
