# -*- coding: utf-8 -*-
"""Projeto Imersão.py

Este script gera uma agenda de discussão de IA e planos de posts,
sendo executado como um aplicativo Streamlit, com funcionalidade de envio de e-mail.
"""

# Importa as bibliotecas necessárias para o projeto
import os
import sys
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai # Mantém esta importação para o alias 'genai'

from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search # Importa a ferramenta google_search
# REMOVIDO: from google.generativeai import types # Esta linha foi removida e não é mais necessária
from datetime import date
import textwrap

import requests
import warnings
warnings.filterwarnings("ignore")

import smtplib # Para enviar e-mails
from email.mime.text import MIMEText # Para criar o corpo do e-mail

# --- Configuração da Chave da API do Google Gemini e Credenciais de E-mail ---
current_dir = os.path.dirname(__file__)
dotenv_path = os.path.join(current_dir, '..', '..', '.env')

load_dotenv(dotenv_path)

api_key = os.getenv('GEMINI_API_KEY')
email_host = os.getenv('EMAIL_HOST')
email_port = os.getenv('EMAIL_PORT')
email_username = os.getenv('EMAIL_USERNAME')
email_password = os.getenv('EMAIL_PASSWORD')

if api_key is None:
    st.error("ERRO: A variável de ambiente 'GEMINI_API_KEY' não foi encontrada.")
    st.write(f"Por favor, verifique seu arquivo .env em '{dotenv_path}' e certifique-se de que 'GEMINI_API_KEY' está configurada.")
    st.stop()
else:
    os.environ["GEMINI_API_KEY"] = api_key

# Validação das credenciais de e-mail
if any(cred is None for cred in [email_host, email_port, email_username, email_password]):
    st.warning("Atenção: As credenciais de e-mail (EMAIL_HOST, EMAIL_PORT, EMAIL_USERNAME, EMAIL_PASSWORD) não foram totalmente configuradas no .env. A função de envio de e-mail pode não funcionar.")
    st.info("Para habilitar o envio de e-mail, adicione essas variáveis ao seu arquivo .env.")


genai.configure(api_key=api_key)
MODEL_ID = "gemini-2.0-flash"

# --- Instancia o serviço de sessão e o armazena no Streamlit session_state ---
# Isso garante que o estado da sessão seja mantido entre as chamadas dos agentes.
if 'session_service_adk' not in st.session_state:
    st.session_state.session_service_adk = InMemorySessionService()

def call_agent(agent: Agent, message_text: str) -> str:
    """
    Função auxiliar para executar um agente e obter sua resposta final.
    Usa um serviço de sessão global (persistido via st.session_state) para manter o estado da sessão.
    """
    session_service = st.session_state.session_service_adk # Usa a instância do session_state
    session_id = "session1" # ID fixo para a sessão do exemplo

    session = None
    try:
        # Tenta criar uma nova sessão. Se já existir, uma ValueError será lançada.
        session = session_service.create_session(app_name=agent.name, user_id="user1", session_id=session_id)
    except ValueError:
        # Se a sessão já existe, recupera a sessão existente.
        session = session_service.get_session(app_name=agent.name, user_id="user1", session_id=session_id)
        if session is None:
            # Fallback caso get_session também falhe inesperadamente
            raise ValueError(f"Falha ao criar ou recuperar a sessão: {session_id}")

    runner = Runner(agent=agent, app_name=agent.name, session_service=session_service)
    # CORRIGIDO: Acessa Content e Part diretamente do módulo genai (google.generativeai)
    content = genai.Content(role="user", parts=[genai.Part(text=message_text)])

    final_response = ""
    for event in runner.run(user_id="user1", session_id=session_id, new_message=content):
        if event.is_final_response():
          for part in event.content.parts:
            if part.text is not None:
              final_response += part.text
              final_response += "\n"
    return final_response

def to_markdown_for_streamlit(text):
  """
  Formata o texto para exibição em Markdown no Streamlit.
  """
  text = text.replace('•', '  *')
  return text

def send_email(recipient_email: str, subject: str, body: str):
    """
    Função para enviar um e-mail com a agenda gerada.
    Requer configuração de EMAIL_HOST, EMAIL_PORT, EMAIL_USERNAME, EMAIL_PASSWORD no .env
    """
    if not all([email_host, email_port, email_username, email_password]):
        st.error("Erro: Credenciais de e-mail incompletas. Não é possível enviar o e-mail.")
        return False

    msg = MIMEText(body, 'html', 'utf-8') # Usando 'html' para permitir formatação Markdown que o LLM gera
    msg['Subject'] = subject
    msg['From'] = email_username
    msg['To'] = recipient_email

    try:
        # Usando SMTP_SSL para porta 465 ou STARTTLS para outras (ex: 587)
        if int(email_port) == 465:
            server = smtplib.SMTP_SSL(email_host, int(email_port))
        else:
            server = smtplib.SMTP(email_host, int(email_port))
            server.starttls() # Habilita TLS
        
        server.login(email_username, email_password)
        server.send_message(msg)
        server.quit()
        st.success(f"E-mail enviado com sucesso para {recipient_email}!")
        return True
    except Exception as e:
        st.error(f"Erro ao enviar e-mail: {e}")
        st.warning("Verifique suas credenciais de e-mail, host, porta e configurações de segurança (ex: permissão de aplicativos menos seguros para Gmail).")
        return False


# Define as opções para os segmentos de negócio
segmentos = [
    'Todos',
    'Tecnologia da Informação',
    'Indústria Química',
    'Saúde',
    'Educação',
    'Finanças',
    'Varejo',
    'Agricultura'
]

# Define as opções para a periodicidade
periodicidades = [
    'Sob Demanda',
    'Diário',
    'Semanal',
    'Mensal'
]


##########################################
# --- Agente 1: Buscador de Notícias --- #
##########################################
def agente_buscador_noticias(segmento_negocio):
    """
    Define e executa um agente para buscar notícias relevantes sobre inovação e IA
    dentro de um segmento de negócio específico ou notícias gerais, focando em categorias.

    Retorna uma string formatada (JSON-like) com 3 itens por categoria.
    """
    buscador = Agent(
        name="agente_buscador_noticias",
        model=MODEL_ID,
        instruction="""
        Você é um agente especialista em buscar notícias e informações sobre inovação e IA.
        Sua tarefa é utilizar a ferramenta Google Search para encontrar as 3 notícias/exemplos mais relevantes
        para CADA UMA das seguintes categorias:
        1.  **Ferramentas de IA:** Notícias sobre novas ferramentas, plataformas, APIs ou frameworks de IA.
        2.  **Segurança em IA:** Notícias sobre desafios de segurança, vulnerabilidades, privacidade ou novas soluções de segurança relacionadas à IA.
        3.  **Exemplos de Implementação de IA com Sucesso:** Casos de uso reais, estudos de caso ou sucessos na aplicação de IA em empresas ou indústrias.
        4.  **Aprendizados/Erros em Implementação de IA:** Casos onde a implementação de IA resultou em desafios, falhas, lições aprendidas ou considerações éticas importantes.

        - Se um 'Segmento de Negócio' específico for fornecido (diferente de 'Todos'), foque sua busca
          em notícias e exemplos relevantes para esse segmento.
        - Se o 'Segmento de Negócio' for 'Todos', busque informações gerais sobre IA para as categorias.

        Para cada categoria, encontre as 3 informações mais impactantes e concisas.
        **Formate sua resposta estritamente como uma string JSON**, com as chaves sendo os nomes das categorias
        e os valores sendo listas de strings, onde cada string é um resumo conciso do item encontrado.
        Exemplo de formato esperado:
        ```json
        {
          "Ferramentas": [
            "Resumo da ferramenta 1.",
            "Resumo da ferramenta 2.",
            "Resumo da ferramenta 3."
          ],
          "Segurança": [
            "Resumo da segurança 1.",
            "Resumo da segurança 2.",
            "Resumo da segurança 3."
          ],
          "Sucesso": [
            "Resumo do sucesso 1.",
            "Resumo do sucesso 2.",
            "Resumo do sucesso 3."
          ],
          "Aprendizado": [
            "Resumo do aprendizado 1.",
            "Resumo do aprendizado 2.",
            "Resumo do aprendizado 3."
          ]
        }
        ```
        """,
        description="Agente que busca e resume notícias e exemplos de IA em categorias específicas (ferramentas, segurança, sucesso, aprendizado).",
        tools=[google_search] # Mantém google_search sem parênteses
    )

    if segmento_negocio == 'Todos':
        entrada_do_agente_buscador = "Busque 3 notícias/exemplos para cada categoria: Ferramentas de IA, Segurança em IA, Casos de sucesso de IA, Casos de aprendizado/erros de IA em geral."
    else:
        entrada_do_agente_buscador = f"Segmento de Negócio: {segmento_negocio}\nBusque 3 notícias/exemplos para cada categoria: Ferramentas de IA, Segurança em IA, Casos de sucesso de IA, Casos de aprendizado/erros de IA relevantes para este segmento."

    noticias_encontradas = call_agent(buscador, entrada_do_agente_buscador)
    return noticias_encontradas

###########################################################
# --- NOVO Agente 3: Organizador da Agenda (Próximo Passo) --- #
###########################################################
def agente_organizador_agenda(dados_brutos_ia):
    """
    Recebe os dados brutos de IA (notícias e exemplos) e os organiza em uma sugestão de agenda
    para discussão, formatada para o corpo do e-mail.
    """
    organizador = Agent(
        name="agente_organizador_agenda",
        model=MODEL_ID,
        instruction="""
        Você é um organizador de agenda especialista em Inteligência Artificial.
        Sua tarefa é receber um conjunto de dados brutos sobre IA (ferramentas, segurança, sucessos, aprendizados/erros)
        e transformá-los em uma estrutura de agenda de discussão clara e concisa.

        Os dados brutos estarão em formato JSON, conforme o exemplo:
        ```json
        {
          "Ferramentas": ["Resumo da ferramenta 1.", "Resumo da ferramenta 2.", "Resumo da ferramenta 3."],
          "Segurança": ["Resumo da segurança 1.", "Resumo da segurança 2.", "Resumo da segurança 3."],
          "Sucesso": ["Resumo do sucesso 1.", "Resumo do sucesso 2.", "Resumo do sucesso 3."],
          "Aprendizado": ["Resumo do aprendizado 1.", "Resumo do aprendizado 2.", "Resumo do aprendizado 3."]
        }
        ```
        Selecione os 3 itens mais relevantes ou interessantes de CADA CATEGORIA (se houver mais de 3)
        e os formate no seguinte modelo para uma SUGGESTÃO DE AGENDA DE DISCUSSÃO, em Markdown:

        ## Sugestão de Pauta para a Comissão de Inovação (COE) - Discussão sobre IA

        Olá a todos,

        Sugiro os seguintes tópicos para nossa próxima reunião de discussão sobre Inteligência Artificial,
        com base nas últimas tendências e desenvolvimentos:

        ### 1. Ferramentas e Tecnologias Emergentes em IA
        * **[Nome da Ferramenta/Notícia]:** [Breve resumo do item 1. Max 2 frases.]
            * _Ponto para Discussão:_ [Sugira uma pergunta ou tópico para a comissão discutir sobre este item.]
        * **[Nome da Ferramenta/Notícia]:** [Breve resumo do item 2. Max 2 frases.]
            * _Ponto para Discussão:_ [Sugira uma pergunta ou tópico para a comissão discutir sobre este item.]
        * **[Nome da Ferramenta/Notícia]:** [Breve resumo do item 3. Max 2 frases.]
            * _Ponto para Discussão:_ [Sugira uma pergunta ou tópico para a comissão discutir sobre este item.]

        ### 2. Desafios e Boas Práticas em Segurança da IA
        * **[Tópico de Segurança/Notícia]:** [Breve resumo do item 1. Max 2 frases.]
            * _Ponto para Discussão:_ [Sugira uma pergunta ou tópico para a comissão discutir sobre este item.]
        * **[Tópico de Segurança/Notícia]:** [Breve resumo do item 2. Max 2 frases.]
            * _Ponto para Discussão:_ [Sugira uma pergunta ou tópico para a comissão discutir sobre este item.]
        * **[Tópico de Segurança/Notícia]:** [Breve resumo do item 3. Max 2 frases.]
            * _Ponto para Discussão:_ [Sugira uma pergunta ou tópico para a comissão discutir sobre este item.]

        ### 3. Exemplos de Sucesso na Implementação de IA
        * **[Exemplo/Caso de Sucesso]:** [Breve resumo do item 1. Max 2 frases.]
            * _Ponto para Discussão:_ [Sugira uma pergunta ou tópico para a comissão discutir sobre este item.]
        * **[Exemplo/Caso de Sucesso]:** [Breve resumo do item 2. Max 2 frases.]
            * _Ponto para Discussão:_ [Sugira uma pergunta ou tópico para a comissão discutir sobre este item.]
        * **[Exemplo/Caso de Sucesso]:** [Breve resumo do item 3. Max 2 frases.]
            * _Ponto para Discussão:_ [Sugira uma pergunta ou tópico para a comissão discutir sobre este item.]

        ### 4. Aprendizados com Desafios e Erros em IA
        * **[Desafio/Erro/Aprendizado]:** [Breve resumo do item 1. Max 2 frases.]
            * _Ponto para Discussão:_ [Sugira uma pergunta ou tópico para a comissão discutir sobre este item.]
        * **[Desafio/Erro/Aprendizado]:** [Breve resumo do item 2. Max 2 frases.]
            * _Ponto para Discussão:_ [Sugira uma pergunta ou tópico para a comissão discutir sobre este item.]
        * **[Desafio/Erro/Aprendizado]:** [Breve resumo do item 3. Max 2 frases.]
            * _Ponto para Discussão:_ [Sugira uma pergunta ou tópico para a comissão discutir sobre este item.]

        Atenciosamente,
        [Seu Nome/Time]
        """,
        description="Agente que organiza dados brutos sobre IA em uma sugestão de agenda de discussão formatada para e-mail.",
        tools=[] # Não precisa de ferramentas externas para esta tarefa de organização
    )

    entrada_do_organizador = f"Dados brutos de IA para organizar em agenda: {dados_brutos_ia}"
    agenda_formatada = call_agent(organizador, entrada_do_organizador)
    return agenda_formatada

####################################################
# --- Agente 2 (Renomeado): Gerador de E-mail --- #
####################################################
def agente_gerador_email(agenda_formatada_markdown):
    """
    Recebe o corpo da agenda já formatada em Markdown e finaliza o conteúdo do e-mail.
    """
    gerador_email = Agent(
        name="agente_gerador_email",
        model=MODEL_ID,
        instruction="""
        Você é um agente especialista em comunicação corporativa.
        Sua tarefa é receber um conteúdo de agenda de discussão de IA já formatado em Markdown
        e apresentá-lo como o CORPO de um e-mail.

        Você NÃO deve gerar o assunto do e-mail, apenas o corpo.
        Você NÃO deve gerar saudações ou despedidas adicionais, pois elas já estão incluídas no conteúdo fornecido ou serão adicionadas pelo sistema de envio.

        O conteúdo da agenda será fornecido como uma string Markdown.
        Apenas retorne o conteúdo exato que deve ir no corpo do e-mail.
        """,
        description="Agente que formata uma agenda de discussão em Markdown para o corpo de um e-mail.",
        tools=[] # Não precisa de ferramentas externas
    )

    entrada_do_gerador_email = f"Conteúdo da agenda em Markdown para corpo do e-mail: {agenda_formatada_markdown}"
    corpo_email = call_agent(gerador_email, entrada_do_gerador_email)
    return corpo_email

def run_agenda_process_streamlit(segmento, periodicidade, recipient_email):
    """
    Orquestra a execução dos agentes e exibe a saída no Streamlit,
    com a opção de enviar e-mail.
    """
    st.markdown(f"### Segmento selecionado: {segmento}")
    st.markdown(f"### Periodicidade selecionada: {periodicidade}")
    st.markdown(f"### E-mail do Destinatário: {recipient_email if recipient_email else 'Não configurado'}")

    if periodicidade == 'Sob Demanda':
        st.info("🚀 Executando processo de geração de agenda e plano de posts 'Sob Demanda'...")
    else:
        st.info(f"⏰ Este processo foi configurado para ser executado {periodicidade}. "
                "Executando agora para demonstração...")

    # Exibe um spinner enquanto os agentes estão trabalhando
    with st.spinner("Buscando notícias, organizando agenda e gerando conteúdo do e-mail... Isso pode levar alguns segundos."):
        # Etapa 1: Chama o Agente Buscador de Notícias
        st.subheader("🔎 Buscando notícias sobre inovação e IA por categorias...")
        dados_brutos = agente_buscador_noticias(segmento)
        st.markdown("---")
        st.markdown("**Saída Bruta do Agente Buscador (para depuração):**")
        st.code(dados_brutos) # Exibe a saída JSON bruta para inspeção

        # Etapa 2: Chama o Agente Organizador da Agenda
        st.subheader("📋 Organizando a agenda de discussão...")
        agenda_formatada = agente_organizador_agenda(dados_brutos)
        st.markdown("### 📝 Sugestão de Agenda de Discussão:")
        st.markdown(agenda_formatada) # Exibe a agenda formatada para o usuário

        # Etapa 3: Chama o Agente Gerador de E-mail
        st.subheader("📧 Gerando o corpo do e-mail...")
        corpo_email_final = agente_gerador_email(agenda_formatada)
        st.markdown("### Prévia do Corpo do E-mail:")
        st.markdown(corpo_email_final) # Exibe o corpo final do e-mail

    st.success("✅ Geração de Agenda e E-mail concluída!")

    # Armazena os dados no session_state para uso no botão de envio
    st.session_state['corpo_email_final'] = corpo_email_final
    st.session_state['email_subject'] = "COE - Comissão de Inovação: Sugestão de Pauta de IA"


# --- Interface Streamlit ---
st.set_page_config(layout="wide") # Configura a página para usar a largura total

st.title("🤖 Gerador de Agenda de Discussão de IA para Empresas")
st.markdown("---")

st.write("Selecione o segmento de negócio e a periodicidade para gerar uma agenda de discussão de IA e planos de posts. Você também pode configurar o envio de e-mail para um grupo.")

# Inicializa st.session_state para a periodicidade se não existir
if 'periodicidade_index' not in st.session_state:
    st.session_state['periodicidade_index'] = 0 # Define "Sob Demanda" como padrão

# Seletores de segmento e periodicidade
segmento_selecionado = st.selectbox("Selecione o segmento de negócio:", segmentos, key="segment_select")
# Recupera o índice da periodicidade do session_state
periodicidade_selecionada = st.selectbox(
    "Selecione a periodicidade do processo:",
    periodicidades,
    index=st.session_state['periodicidade_index'],
    key="periodicity_select"
)
# Atualiza o session_state com a nova seleção de periodicidade
st.session_state['periodicidade_index'] = periodicidades.index(periodicidade_selecionada)


email_destinatario = st.text_input("E-mail do Destinatário (ex: grupo.inovacao@empresa.com):", key="email_recipient")

col1, col2 = st.columns(2) # Cria duas colunas para os botões

with col1:
    if st.button("Gerar Agenda e Prévia do E-mail", key="generate_button"):
        run_agenda_process_streamlit(segmento_selecionado, periodicidade_selecionada, email_destinatario)

with col2:
    if st.button("Cancelar Processo e Limpar", key="cancel_button"):
        # Limpa todas as chaves do session_state, exceto a periodicidade
        for key in st.session_state.keys():
            if key != 'periodicidade_index': # Não limpa a periodicidade
                del st.session_state[key]
        st.experimental_rerun() # Reinicia o aplicativo Streamlit

# Botão de envio de e-mail, que só aparece após a geração da agenda
if 'corpo_email_final' in st.session_state and st.session_state['corpo_email_final'] and email_destinatario:
    st.markdown("---")
    if st.button("Enviar E-mail Agora", key="send_email_final_button"):
        send_email(email_destinatario, st.session_state['email_subject'], st.session_state['corpo_email_final'])
else:
    if st.session_state.get('corpo_email_final') is not None and not email_destinatario:
        st.warning("Preencha o campo 'E-mail do Destinatário' para habilitar o envio do e-mail.")
