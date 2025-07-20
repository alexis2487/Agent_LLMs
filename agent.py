import os
from langchain_community.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSequence

def create_agent():
    # Modelo LLM a usar con Ollama
    model = os.getenv("LLM_MODEL", "llama3")
    llm = ChatOllama(model=model)

    # Prompt base del agente
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Eres un agente de ciberseguridad llamado BlackTechSec. Sé útil, directo y profesional."),
        ("user", "{input}")
    ])

    # Crear la cadena (prompt -> modelo)
    chain = RunnableSequence(prompt | llm)

    return chain
