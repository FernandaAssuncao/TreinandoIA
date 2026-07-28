import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from personagens import *
from time import sleep


if __name__ == '__main__':
    def mostrar_mensagens(mensagem):
        resposta = cadeia_com_memoria.invoke(
            {'query': mensagem},
            config={'session_id': sessao},
        )
        print(f' NARRADOR: {resposta}')
        sleep(2)

    load_dotenv()
    api_key = os.getenv("API_KEY_RPG")
    modelo = ChatGroq(model="llama-3.1-8b-instant", api_key = api_key)
    prompt_sugestao = ChatPromptTemplate.from_messages(
        [
            ('system', (
                'Você é um narrador de RPG Você é o Narrador épico de um jogo de RPG de combate em turnos. '
                'Seu objetivo é narrar as ações dos personagens de forma empolgante, '
                'as ações serão ditas e só então você faz a narração dos fatos, '
                'pode criar mini dialogos entre os personagens para deixar mais interessante, '
                'dramática e curta (máximo 3 frases por ação).'
            )),
            ('placeholder', '{historico}'),
            ('human', '{query}')
        ]
    )

    cadeia = prompt_sugestao | modelo | StrOutputParser()
    memoria = {}
    sessao = 'RPG'
    def historico_por_sessao(sessao: str):
        if not sessao in memoria:
            memoria[sessao] = InMemoryChatMessageHistory()
        return memoria[sessao]

    cadeia_com_memoria = RunnableWithMessageHistory(
        runnable=cadeia,
        get_session_history=historico_por_sessao,
        input_messages_key='query',
        history_messages__key='historico',
    )

    jg1 = Principe('Heitor Cortês', 9000)
    jg2 = Princesa('Fernanda Assunção', 9000)
    mostrar_mensagens(f'A batalha sera  entre {jg1.__class__.__name__} {jg1.nome} e {jg2.__class__.__name__} {jg2.nome}')

    mens1= jg1.atacar(jg2, 4000)
    mostrar_mensagens(mens1)
    mens2 = jg2.atacar(jg1, 4000)
    mostrar_mensagens(mens2)
    mens3 = jg2.curar()
    mostrar_mensagens(mens3)
    mens4 = jg1.curar()
    mostrar_mensagens(mens4)
    jg1.placar()
    jg2.placar()
