from langchain_core.prompts import ChatPromptTemplate

def get_rag_prompt():
    return ChatPromptTemplate.from_template(
        """
        you are AuraDocs, an intelligent assistant answering questions based only on the provided context.
        
        context: {context}
        question: {question}

        if the answer is not in the context, say "I don't know based on the document".
        answer:
        """
    )