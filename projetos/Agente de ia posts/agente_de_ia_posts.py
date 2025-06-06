# agente_de_ia_posts.py

# Descrição: Este script utiliza o LangChain e OpenAI para gerar posts de redes sociais com base em um conteúdo fornecido, público alvo e tom de voz.

import streamlit as st

from langchain_openai import ChatOpenAI  # Correto

from langchain.prompts import PromptTemplate

import os   



# Configuração do Streamlit

OPENAI_KEY = os.getenv("API_KEY")



# Configuração do modelo de linguagem

chat = ChatOpenAI(

    model="gpt-4o",

    temperature=0,

    openai_api_key=OPENAI_KEY

)



# Configuração do Prompt

st.title("Ferramentas de Post")



conteudo = st.text_input("Conteúdo do Post", placeholder="Digite o conteúdo do post aqui...")

publico_alvo = st.text_input("Público Alvo", placeholder="Digite o público alvo aqui...")

tom = st.selectbox("Tom de voz", ["Amigavel","Profissional","Urgente","Engraçado","Inspirador"], index=0)



template_prompt = '''

Você é um especialista em marketing digital e redes sociais. Sua tarefa é criar posts envolventes e atraentes para o público alvo especificado, com base no conteúdo fornecido e no tom de voz escolhido. Uma descrição do post deve ser gerada, mantendo o conteúdo original, mas adaptando-o para o formato de post de rede social.

otima. Conteúdo: {conteudo}

Público Alvo: {publico_alvo}   

Tom de voz: {tom}

'''

prompt = PromptTemplate.from_template(template_prompt)



# Interface do Streamlit

if st.button("Gerar Post"):

    resposta = chat.invoke(prompt.format(conteudo=conteudo, publico_alvo=publico_alvo, tom=tom))

    st.subheader("Post Gerado")

    st.write(resposta.content)