# agente_de_ia_posts.py

# Descrição: Este script utiliza a biblioteca oficial do Google Gemini para gerar posts de redes sociais com base em um conteúdo fornecido, público alvo e tom de voz.

import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai # Importação para a biblioteca oficial do Google Gemini

# Carregar variáveis de ambiente do .env
# A lógica de caminho ainda é importante para encontrar o .env na raiz do projeto.
current_dir = os.path.dirname(__file__)
# Sobe duas pastas para chegar na raiz do repositório (projetos/projetospost -> projetos -> raiz do repo)
dotenv_path = os.path.join(current_dir, '..', '..', '.env')
load_dotenv(dotenv_path)

# Configuração do Streamlit
# A chave da API do Gemini estará no .env sob o nome GEMINI_API_KEY
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

if not GOOGLE_API_KEY:
    st.error("A chave da API do Gemini não foi encontrada. Certifique-se de que a variável de ambiente 'GEMINI_API_KEY' está configurada no seu arquivo .env.")
    st.stop() # Interrompe a execução do Streamlit se a chave não estiver disponível

# Configuração da API do Google Gemini
genai.configure(api_key=GOOGLE_API_KEY)

# Configuração do modelo de linguagem
# Use o modelo "gemini-pro" para texto (para texto)
model = genai.GenerativeModel('gemini-2.0-flash')

# Interface do Streamlit
st.title("Ferramentas de Post (Gemini Direto)")

conteudo = st.text_input("Conteúdo do Post", placeholder="Digite o conteúdo do post aqui...")
publico_alvo = st.text_input("Público Alvo", placeholder="Digite o público alvo aqui...")
tom = st.selectbox("Tom de voz", ["Amigavel","Profissional","Urgente","Engraçado","Inspirador"], index=0)

# O prompt é uma string normal, não mais um PromptTemplate do LangChain
template_prompt_text = '''
Você é um especialista em marketing digital e redes sociais. Sua tarefa é criar posts envolventes e atraentes para o público alvo especificado, com base no conteúdo fornecido e no tom de voz escolhido. Uma descrição do post deve ser gerada, mantendo o conteúdo original, mas adaptando-o para o formato de post de rede social.

Conteúdo: {conteudo}

Público Alvo: {publico_alvo}
Tom de voz: {tom}
'''

if st.button("Gerar Post"):
    if not conteudo or not publico_alvo:
        st.warning("Por favor, preencha o Conteúdo do Post e o Público Alvo.")
    else:
        with st.spinner("Gerando seu post..."):
            try:
                # Formata o prompt com os valores do usuário
                formatted_prompt = template_prompt_text.format(
                    conteudo=conteudo,
                    publico_alvo=publico_alvo,
                    tom=tom
                )
                
                # Faz a chamada à API do Gemini
                # Usamos generation_config para controlar a temperatura
                response = model.generate_content(
                    formatted_prompt,
                    generation_config=genai.types.GenerationConfig(
                        temperature=0 # Mantém a temperatura como 0
                    )
                )
                
                st.subheader("Post Gerado")
                st.write(response.text) # A resposta de texto é acessada via .text
            except Exception as e:
                st.error(f"Ocorreu um erro ao gerar o post: {e}")
                st.info("Verifique sua chave de API e sua conexão com a internet. Tente novamente.")