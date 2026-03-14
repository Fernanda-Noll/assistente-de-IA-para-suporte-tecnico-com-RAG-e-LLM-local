import os
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma.vectorstores import Chroma
import re

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASTA_DADOS = os.path.join(BASE_DIR, "base_de_conhecimento")

def criar_bd():
    if os.path.isfile("banco_vetorial/chroma.sqlite3"):
        print("Banco vetorial já existe.")
        return
    documentos = carregar_documentos()
    print("Documentos carregados:", len(documentos))
    chunks = dividir_chunks(documentos)
    print("Chunks criados:", len(chunks))
    vetorizar_chunks(chunks)

def carregar_documentos():
    carregar = PyPDFDirectoryLoader(PASTA_DADOS)
    documentos = carregar.load()
    for doc in documentos:
        doc.page_content = limpar_texto(doc.page_content)
        print(doc)     
    return documentos

def limpar_texto(texto):
    texto = re.sub(r"\n+", " ", texto)
    texto = re.sub(r"\s+", " ", texto)
    return texto.strip()

def dividir_chunks(documentos):
    separador_documentos = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    chunks = separador_documentos.split_documents(documentos)
    return chunks

def vetorizar_chunks(chunks):
    db = Chroma.from_documents(chunks, embeddings, persist_directory="banco_vetorial")
    print("Banco de dados criado")

if __name__ == "__main__":
    criar_bd()
