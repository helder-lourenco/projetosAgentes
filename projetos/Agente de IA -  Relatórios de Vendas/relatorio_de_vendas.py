import os
import streamlit as st
import pandas as pd
import google.generativeai as genai

# Configurar a chave da API Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro') # Instanciar o modelo Gemini

st.set_page_config(page_title="Relatório de Vendas", page_icon=":bar_chart:")

st.title("Relatório de Vendas")

planilha = st.file_uploader("Envia um CSV coma as colunas: Estado, Loja, Dia, Vendas", type=["csv"])
if not planilha:
    st.warning("Por favor, envie um arquivo CSV.")
    st.stop()

tabela_dados = pd.read_csv(planilha)
tabela_dados["DIA"]  = pd.to_datetime(tabela_dados["Dia"], dayfirst= True, errors='coerce')
tabela_dados["Vendas"]  = pd.to_numeric(tabela_dados["Vendas"], errors='coerce')

#Metricas
total_vendas = tabela_dados["Vendas"].sum()
numeroDias = tabela_dados["DIA"].nunique()
vendasDia = total_vendas / numeroDias
topEstados = tabela_dados.groupby("Estado")["Vendas"].sum().nlargest(5).index.tolist()

# vendas por semana
tabelaSemanal = tabela_dados.set_index("DIA")
tabelaSemanal = tabelaSemanal.resample("W").sum()

# Gráfico de vendas por semana
st.subheader("Vendas por Semana")   
st.bar_chart(tabelaSemanal["Vendas"])
# Gráfico de vendas por estado
st.subheader("Vendas por Estado")
tabelaEstado = tabela_dados.groupby("Estado")["Vendas"].sum().reset_index()
st.bar_chart(tabelaEstado.set_index("Estado")["Vendas"])
# Gráfico de vendas por loja
st.subheader("Vendas por Loja")
tabelaLoja = tabela_dados.groupby("Loja")["Vendas"].sum().reset_index()

st.bar_chart(tabelaLoja.set_index("Loja")["Vendas"])

# Gráfico de vendas por dia
st.subheader("Vendas por Dia")
tabelaDia = tabela_dados.groupby("DIA")["Vendas"].sum().reset_index()
st.bar_chart(tabelaDia.set_index("DIA")["Vendas"])
# Exibir métricas
st.subheader("Métricas")
st.metric("Total de Vendas", f"R$ {total_vendas:,.2f}")
st.metric("Número de Dias", numeroDias)
st.metric("Top 5 Estados", ", ".join(topEstados))
# Análise de vendas
st.subheader("Análise de Vendas")
if st.button("Gerar Análise"):  
    with st.spinner("Gerando análise..."):
        prompt = f"""
        Você é um analista de BI. Gere um relatório em Markdown (português) contendo:

Início e final do período de análise.
Visão geral com total de vendas e média diária.
Tendência semanal, mencionando padrões notáveis.
Ranking Top-5 Estados por Vendas.
Três insights acionáveis para o time comercial.
        Dados de Vendas:
        {tabela_dados.to_csv(index=False)}
        Analise os dados de vendas a seguir e gere um relatório detalhado:
        Total de Vendas: R$ {total_vendas:,.2f}
        Número de Dias: {numeroDias}
        vendas por Dia: R$ {vendasDia:,.2f}
        Período: {tabela_dados["DIA"].min().strftime('%d/%m/%Y')} a {tabela_dados["DIA"].max().strftime('%d/%m/%Y')}
        Top 5 Estados: {', '.join(topEstados)}
        
        Dados:
        {tabela_dados.to_csv(index=False)}
        
        Gere um relatório que inclua insights sobre tendências, padrões e recomendações.
        """
        with st.spinner("Gerando Relatório..."):
            resposta = model.generate_content(prompt)
            report = resposta.text # A variável 'report' é definida aqui
            st.subheader("Relatório Gerado") # Mover para dentro do bloco if
            st.markdown(report) # Mover para dentro do bloco if