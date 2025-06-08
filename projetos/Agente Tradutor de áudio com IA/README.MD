Agente Tradutor de Áudio com IA
Este projeto apresenta um aplicativo web interativo construído com Streamlit que permite gravar áudio, transcrevê-lo e, em seguida, traduzi-lo para o inglês usando modelos de Inteligência Artificial.

Funcionalidades
Gravação de Áudio: Grave áudio diretamente do seu navegador por um tempo configurável.
Transcrição de Áudio: Transcreve o áudio gravado para texto em português.
Tradução de Texto: Traduz o texto transcrito para o inglês.
Como Usar
Instalação das Dependências:
Certifique-se de ter o Python instalado. Em seguida, instale as bibliotecas Python necessárias:

Bash

pip install openai soundfile sounddevice streamlit google-generativeai
Nota: Para sounddevice, pode ser necessário instalar portaudio separadamente em seu sistema operacional.

Configuração das Chaves de API:
Este projeto requer chaves de API da OpenAI e do Google Gemini para suas funcionalidades de IA. Você deve definir essas chaves como variáveis de ambiente.

Obtenha sua chave de API da OpenAI.
Obtenha sua chave de API do Google Gemini no Google AI Studio.
Recomenda-se criar um arquivo .env na mesma pasta do projeto e adicionar suas chaves da seguinte forma:

API_KEY="sua_chave_openai_aqui"
GEMINI_API_KEY="sua_chave_gemini_aqui"
Alternativamente, você pode definir as variáveis de ambiente diretamente no seu terminal antes de executar o aplicativo.

Execução do Aplicativo:
Com as dependências instaladas e as chaves de API configuradas, você pode iniciar o aplicativo Streamlit:

Bash

streamlit run agente_tradutor.py
Isso abrirá o aplicativo no seu navegador padrão.

Uso do Aplicativo
Ajuste a Duração do Áudio: Use o controle deslizante para definir quantos segundos de áudio você deseja gravar.
Grave o Áudio: Clique no botão "Gravar Áudio". Uma vez que a gravação for concluída, o áudio será reproduzido.
Traduza o Áudio: Após a gravação, clique no botão "Traduzir Áudio". O aplicativo irá transcrever o áudio e exibir a transcrição original e a tradução em inglês.
