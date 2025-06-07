# -*- coding: utf-8 -*-
"""Projeto Imersão.py

Versão atualizada com formatação de e-mail melhorada.
"""

import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
from datetime import date
import smtplib
from email.mime.text import MIMEText

# --- Configuração inicial ---
current_dir = os.path.dirname(__file__)
dotenv_path = os.path.join(current_dir, '..', '..', '.env')
load_dotenv(dotenv_path)

# Configuração da API Gemini
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    st.error("ERRO: Chave API não encontrada. Verifique seu arquivo .env")
    st.stop()

genai.configure(api_key=api_key)
MODEL = genai.GenerativeModel('gemini-2.0-flash')

# Configuração de e-mail
email_config = {
    'host': os.getenv('EMAIL_HOST'),
    'port': os.getenv('EMAIL_PORT'),
    'username': os.getenv('EMAIL_USERNAME'),
    'password': os.getenv('EMAIL_PASSWORD')
}

# --- Funções Principais ---
def generate_content(prompt):
    """Gera conteúdo usando a API Gemini"""
    try:
        response = MODEL.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Erro ao gerar conteúdo: {str(e)}")
        return None

def buscar_noticias(segmento):
    """Busca notícias sobre IA para o segmento selecionado"""
    prompt = f"""
    Para o segmento {segmento}, liste em formato JSON:
    1. 3 ferramentas/tecnologias emergentes de IA com:
       - Nome
       - Descrição (1-2 frases)
       - Ponto para discussão (pergunta relevante)
    2. 3 desafios/boas práticas de segurança com IA com:
       - Tópico
       - Descrição
       - Ponto para discussão
    3. 3 casos de sucesso de implementação de IA com:
       - Caso
       - Descrição
       - Ponto para discussão
    4. 3 aprendizados/erros comuns com IA com:
       - Tópico
       - Descrição
       - Ponto para discussão
    """
    return generate_content(prompt)

def formatar_agenda(dados_noticias):
    """Formata os dados em uma agenda de discussão profissional"""
    prompt = f"""
    Com base nestes dados sobre IA:
    {dados_noticias}
    
    Crie uma agenda de discussão em MARKDOWN com este formato EXATO:

    ## 📌 Sugestão de Pauta - Inteligência Artificial

    ### 1️⃣ Ferramentas e Tecnologias Emergentes
    🔹 **[Nome da Ferramenta]** - [Descrição breve em 1-2 frases]
      *Ponto para discussão:* [Pergunta aberta para debate]
    (Repetir para 3 ferramentas)

    ### 2️⃣ Desafios e Boas Práticas
    🔸 **[Tópico de Desafio]** - [Descrição breve]
      *Ponto para discussão:* [Pergunta para reflexão]
    (Repetir para 3 desafios)

    ### 3️⃣ Casos de Sucesso
    🔹 **[Nome do Caso]** - [Descrição breve]
      *Ponto para discussão:* [Pergunta sobre aplicação]
    (Repetir para 3 casos)

    ### 4️⃣ Aprendizados e Recomendações
    🔸 **[Tópico de Aprendizado]** - [Descrição breve]
      *Ponto para discussão:* [Pergunta para melhoria]
    (Repetir para 3 aprendizados)

    Use emojis e formatação consistente como no exemplo.
    """
    return generate_content(prompt)

def formatar_email(agenda, segmento):
    """Formata o corpo completo do e-mail"""
    prompt = f"""
    Com esta agenda:
    {agenda}
    
    Crie um e-mail profissional em MARKDOWN com este formato EXATO:

    Prezados(as) colegas,

    Espero que esta mensagem os encontre bem. Segue a sugestão de pauta para nossa próxima reunião 
    sobre Inteligência Artificial no segmento {segmento}, com foco nas tendências atuais e lições aprendidas.

    ---

    [INSIRA A AGENDA COMPLETA AQUI, MANTENDO A FORMATAÇÃO]

    ---

    Fico à disposição para ajustes nesta proposta e para discutirmos esses tópicos em nossa reunião.

    Atenciosamente,  
    [Seu Nome]  
    [Seu Cargo/Área]

    Observações:
    - Mantenha a formatação MARKDOWN
    - Use os emojis e estrutura da agenda fornecida
    - Não altere os pontos de discussão
    """
    return generate_content(prompt)

def enviar_email(destinatario, assunto, corpo):
    """Envia e-mail usando SMTP"""
    if not all(email_config.values()):
        st.error("Configuração de e-mail incompleta")
        return False

    try:
        msg = MIMEText(corpo, 'html', 'utf-8')
        msg['Subject'] = assunto
        msg['From'] = email_config['username']
        msg['To'] = destinatario

        if email_config['port'] == '465':
            server = smtplib.SMTP_SSL(email_config['host'], int(email_config['port']))
        else:
            server = smtplib.SMTP(email_config['host'], int(email_config['port']))
            server.starttls()

        server.login(email_config['username'], email_config['password'])
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        st.error(f"Erro ao enviar e-mail: {str(e)}")
        return False

# --- Interface Streamlit ---
def main():
    st.set_page_config(
        page_title="Gerador de Agenda de IA",
        page_icon="🤖",
        layout="wide"
    )

    # CSS personalizado
    st.markdown("""
    <style>
    .email-format {
        font-family: Arial, sans-serif;
        line-height: 1.6;
        color: #333;
        padding: 15px;
        background-color: #f9f9f9;
        border-radius: 5px;
        border-left: 4px solid #3498db;
    }
    .email-format h2 {
        color: #2c3e50;
        border-bottom: 1px solid #eee;
        padding-bottom: 5px;
    }
    .email-format h3 {
        color: #3498db;
    }
    .discussion-point {
        font-style: italic;
        color: #7f8c8d;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("📅 Gerador de Agenda - IA e Inovação")
    st.markdown("---")

    # Dados de configuração
    segmentos = [
        'Todos', 'Tecnologia', 'Indústria', 
        'Saúde', 'Educação', 'Finanças'
    ]

    # Widgets de entrada
    col1, col2 = st.columns(2)
    with col1:
        segmento = st.selectbox("Segmento de Negócio", segmentos, index=0)
    with col2:
        destinatario = st.text_input("E-mail do Destinatário")

    # Botão de geração
    if st.button("Gerar Agenda Completa", type="primary"):
        with st.spinner("Criando conteúdo personalizado..."):
            # Etapa 1: Buscar dados
            st.subheader("Dados Coletados")
            dados = buscar_noticias(segmento)
            if dados:
                st.json(dados, expanded=False)
            
            # Etapa 2: Formatando agenda
            st.subheader("Agenda Formatada")
            agenda = formatar_agenda(dados) if dados else None
            if agenda:
                st.markdown('<div class="email-format">' + agenda + '</div>', 
                           unsafe_allow_html=True)
            
            # Etapa 3: E-mail completo
            st.subheader("E-mail Pronto")
            corpo_email = formatar_email(agenda, segmento) if agenda else None
            if corpo_email:
                st.markdown('<div class="email-format">' + corpo_email + '</div>', 
                           unsafe_allow_html=True)
                
                # Armazena para envio
                st.session_state['email_data'] = {
                    'body': corpo_email,
                    'subject': f"Pauta IA - {segmento} - {date.today().strftime('%d/%m/%Y')}"
                }
                st.success("Conteúdo gerado com sucesso!")

    # Botão de envio
    if 'email_data' in st.session_state and destinatario:
        st.markdown("---")
        if st.button("Enviar E-mail", type="secondary"):
            if enviar_email(
                destinatario,
                st.session_state['email_data']['subject'],
                st.session_state['email_data']['body']
            ):
                st.balloons()
                st.success("E-mail enviado com sucesso!")

    # Botão de limpeza
    if st.button("Limpar Tudo", key="clear"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

if __name__ == "__main__":
    main()