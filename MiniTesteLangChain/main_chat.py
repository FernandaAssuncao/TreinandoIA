import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()
api_key = os.getenv('API_KEY')

modelo = ChatGroq(model="llama-3.1-8b-instant", api_key=api_key)

prompt_sugestao = ChatPromptTemplate.from_messages(
    [
        ('system', 'Voce é um guia de viagens especializado em destinos brasileiros.Apresente-se como Senhor Passeio'),
        ('placeholder', '{historico}'),
        ('human', '{query}')
    ]
)

cadeia = prompt_sugestao | modelo | StrOutputParser()

memoria = {}
sessao = 'guia'

def historico_por_sessao(sessao: str):
    if sessao not in memoria:
        memoria[sessao] = InMemoryChatMessageHistory()
    return memoria[sessao]

lista_perguntas = [
    'Quero visitar um lugar no brasil famoso por praias e culturas, pode sugerir.',
    'Qual a melhor epoca do ano para ir?'
]

cadeia_com_memoria = RunnableWithMessageHistory(
    runnable=cadeia,
    get_session_history=historico_por_sessao,
    input_messages_key='query',
    history_messages_key='historico',
)
for pergunta in lista_perguntas:
    resposta = cadeia_com_memoria.invoke(
        {
            'query': pergunta,
        },
        config={'session_id': sessao},
    )
    print('Usuario: ', pergunta)
    print('IA', resposta)

