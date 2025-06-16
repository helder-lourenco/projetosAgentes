# Use uma imagem base do Python
FROM python:3.9-slim-buster

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# ---- ADICIONAR ESTA SEÇÃO PARA DEPENDÊNCIAS DE SISTEMA ----
# Instala pacotes de desenvolvimento e ferramentas de build
# apt-get update: Atualiza a lista de pacotes
# apt-get install -y --no-install-recommends: Instala os pacotes
#   build-essential: Inclui gcc, g++, make, etc. (ferramentas de compilação)
#   libpq-dev: Cabeçalhos de desenvolvimento para PostgreSQL (necessário para psycopg2-binary)
#   python3-dev: Cabeçalhos de desenvolvimento para Python
# rm -rf /var/lib/apt/lists/*: Limpa o cache do apt para manter a imagem pequena
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    python3-dev && \
    rm -rf /var/lib/apt/lists/*
# --------------------------------------------------------

# Copia o arquivo de requisitos e instala as dependências do Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o resto da aplicação para o diretório de trabalho
COPY . .

# Define variáveis de ambiente para o Django
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE rpa_orchestrator.settings

# Expõe a porta que a aplicação Django irá rodar
EXPOSE 8000

# Comando para iniciar a aplicação Django com Gunicorn (servidor de produção)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "rpa_orchestrator.wsgi:application"]