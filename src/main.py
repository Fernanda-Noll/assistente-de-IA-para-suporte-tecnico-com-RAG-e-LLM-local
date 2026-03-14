import streamlit as st
from services.conexao_lm_studio import conexao_com_llama
from langchain_chroma.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

def carregar_banco():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )
    return Chroma(
        persist_directory="banco_vetorial",
        embedding_function=embeddings,
    )

# Inicializa Chroma + embeddings
db = carregar_banco()

# Recupera os chunks mais relevantes e retorna, após já chama o LLM local
def busca_info(pergunta):
    resultados = db.similarity_search_with_score(pergunta, k=5)

    # Extrai o texto dos chunks
    textos_resultado = [
        doc.page_content
        for doc, score in resultados
        if score < 15
    ]
    base_conhecimento = "\n\n----\n\n".join(textos_resultado)

    # Prepara o prompt RAG
    prompt_final = f"""                                          
    BASE DE CONHECIMENTO:
    {base_conhecimento}

    PERGUNTA:
    {pergunta}                                         
    """
    
    resposta = conexao_com_llama(prompt_final)
    return resposta

# Interface Streamlit
def interface_st():
    st.title("👩💬 Manu, sua assistente de suporte técnico")

    if pergunta := st.chat_input("Qual é a sua dúvida sobre suporte técnico?"):
        with st.chat_message("user", avatar="👤"):
            st.markdown(pergunta)

        with st.spinner("👩 A Manu está pensando..."):
            resposta = busca_info(pergunta)

            with st.chat_message("assistant"):
                st.markdown(resposta)

if __name__ == "__main__":
    interface_st()
