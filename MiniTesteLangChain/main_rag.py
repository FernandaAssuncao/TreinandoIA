from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
api_key = os.getenv("API_KEY")
modelo = ChatGroq(model="llama-3.3-70b-versatile", api_key=api_key)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

documento = TextLoader(
    "dados_base_conhecimento.txt",
    encoding="utf-8",
).load()

pedacos = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
).split_documents(documento)

dados_recuperados = FAISS.from_documents(
    pedacos, embeddings
).as_retriever(search_kwargs={"k": 2})

prompt_consulta = ChatPromptTemplate.from_messages(
    [
        ('system', 'Você é um assistente prestativo. Responda à pergunta do usuário utilizando apenas o contexto fornecido abaixo.'),
        ('human', '{query}\n\nContexto: {context}\n\nResposta: ')
    ]
)

cadeia = prompt_consulta | modelo | StrOutputParser()

def responder(pergunta:str):
    trecos = dados_recuperados.invoke(pergunta)
    contexto = '\n\n'.join(um_trecho.page_content for um_trecho in trecos)
    return cadeia.invoke({
        "query": pergunta,
        "context": contexto,
    })

print(responder('Qual é a política de reembolso para viagens?'))
