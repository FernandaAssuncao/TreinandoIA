from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')
modelo = ChatGroq(model="llama-3.1-8b-instant", api_key=api_key)
prompt_consultor = ChatPromptTemplate.from_messages(
    [
        ('system', 'Você é um consutor de viagem '),
        ('human', '{query}'),
    ]
)
assistente = prompt_consultor | modelo | StrOutputParser()
print(assistente.invoke({'query': 'Quero ferias em praias no brasil'}))
