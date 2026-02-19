from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from app.core.llm import get_llm
from app.core.prompts import get_rag_prompt

def build_rag_chain(retriever):

    llm = get_llm()
    prompt = get_rag_prompt()

    chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain
