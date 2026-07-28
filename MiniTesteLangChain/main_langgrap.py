from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from typing import Literal, TypedDict
import os

load_dotenv()
api_key = os.getenv('API_KEY')
modelo = ChatGroq(model="llama-3.3-70b-versatile", api_key=api_key)
prompt_consultor_pria = ChatPromptTemplate.from_messages(
    [
        ('system', 'Apresente-se como Sra Praia. Você é uma especialista em viagens com destinos para a praia'),
        ('human', '{query}'),
    ]
)
prompt_consultor_montanha = ChatPromptTemplate.from_messages(
    [
        ('system', 'Apresente-se como Sra Montanha . Você é uma especialista em viagens com destinos para a montanhas e atividades radicais'),
        ('human', '{query}'),
    ]
)

cadeia_praia = prompt_consultor_pria | modelo| StrOutputParser()
cadeia_montanha = prompt_consultor_montanha | modelo| StrOutputParser()

class Rota(TypedDict):
    destino: Literal['praia', 'montanha']



prompt_roteador = ChatPromptTemplate.from_messages(
    [
        ('system', 'Analise a pergunta e classifique o destino desejado entre praia ou montanha '),
        ('human', '{query}')
    ]
)

roteador = prompt_roteador | modelo.with_structured_output(Rota)

def responda(pergunta: str):
    rota = roteador.invoke({'query': pergunta})
    if rota['destino'] == 'praia':
        return cadeia_praia.invoke({'query': pergunta})
    return cadeia_montanha.invoke({'query': pergunta})

print(responda('quero passear por praias belas'))
