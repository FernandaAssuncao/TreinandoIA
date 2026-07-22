from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")


prompt_cidade = PromptTemplate(
    template='''
    Sugira uma cidade dada o meu interesse por {interesse}.
    ''',
    input_variables=['interesse']
)
modelo = ChatGroq(model="llama-3.1-8b-instant", api_key=api_key)
cadeia = prompt_cidade | modelo | StrOutputParser()

resposta = cadeia.invoke(
    {
        'interesse': 'hipismo'
    }
)
print(resposta)
