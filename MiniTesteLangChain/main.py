from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

class Destino(BaseModel):
    cidade:str = Field('A cidade recomendada para visitar ')
    motivo:str = Field('Motivo pelo qual é interessante visitar essa cidade')

class Restaurantes(BaseModel):
    cidade: str = Field('A cidade recomendada para visitar ')
    restaurantes: str = Field('Restaurantes recomendados na cidade')


parseador_destino = JsonOutputParser(pydantic_object=Destino)
parseador_restaurantes = JsonOutputParser(pydantic_object=Restaurantes)

prompt_cidade = PromptTemplate(
    template='''
    Sugira uma cidade dada o meu interesse por {interesse}.
    {formato de saida}
    ''',
    input_variables=['interesse'],
    partial_variables={'formato de saida': parseador_destino.get_format_instructions()}
)

prompt_restaurantes = PromptTemplate(
    template='''
    Sugira restaurantes populares entre locais em {cidade}.
    {formato de saida}
    ''',
    partial_variables={'formato de saida': parseador_restaurantes.get_format_instructions()}
)

prompt_cultura = PromptTemplate(
    template='''Sugira atividades e locais culturais em {cidade}.'''
)


modelo = ChatGroq(model="llama-3.1-8b-instant", api_key=api_key)
cadeia1 = prompt_cidade | modelo | parseador_destino
cadeia2 = prompt_restaurantes | modelo | parseador_restaurantes
cadeia3 = prompt_cultura | modelo | StrOutputParser()

cadeia = (cadeia1 | cadeia2 | cadeia3)
resposta = cadeia.invoke(
    {
        'interesse': 'hipismo'
    }
)
print(resposta)
