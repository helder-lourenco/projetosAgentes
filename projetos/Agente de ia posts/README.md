Ferramentas de Post (Gemini Direto) 🚀
Este projeto é uma ferramenta Streamlit que utiliza a API oficial do Google Gemini para gerar posts de redes sociais. Ele foi desenvolvido para auxiliar na criação de conteúdo envolvente, permitindo que você especifique o conteúdo do post, o público-alvo e o tom de voz desejado.

🌟 Funcionalidades
Geração de Posts Personalizados: Crie posts adaptados para diferentes plataformas de redes sociais.
Controle de Tom de Voz: Escolha entre diversos tons, como "Amigável", "Profissional", "Urgente", "Engraçado" e "Inspirador".
Interface Intuitiva: Desenvolvido com Streamlit para uma experiência de usuário simples e eficaz.
Integração Direta com Gemini API: Utiliza a biblioteca oficial do Google Gemini para garantir a qualidade da geração de texto.
🛠️ Tecnologias Utilizadas
Python
Streamlit: Para a interface de usuário web.
Google Gemini API: Para a geração de texto.
python-dotenv: Para o gerenciamento de variáveis de ambiente.
🚀 Como Executar o Projeto
Siga os passos abaixo para configurar e rodar o projeto em sua máquina local:

1. Pré-requisitos
   Certifique-se de ter o Python instalado (versão 3.8 ou superior é recomendada).

2. Configuração do Ambiente
   a. Clone o Repositório:
   bash git clone <URL_DO_SEU_REPOSITORIO> cd <pasta_do_projeto>
   (Substitua <URL_DO_SEU_REPOSITORIO> e <pasta_do_projeto> pelos valores corretos do seu repositório).

b. Crie um Ambiente Virtual (Recomendado):
bash python -m venv venv source venv/bin/activate # No Windows, use `venv\Scripts\activate`

c. Instale as Dependências:
bash pip install -r requirements.txt
(Você precisará criar um arquivo requirements.txt se ainda não tiver um. Ele deve conter as seguintes linhas: streamlit, google-generativeai, python-dotenv).

3. Configuração da API do Gemini
   a. Obtenha sua Chave da API do Gemini:
   Se você ainda não tem uma chave, acesse o Google AI Studio para gerar uma.

b. Crie um Arquivo .env:
Na raiz do seu projeto (duas pastas acima do agente_de_ia_posts.py), crie um arquivo chamado .env e adicione sua chave da API da seguinte forma:
GEMINI_API_KEY="SUA_CHAVE_DA_API_AQUI"
Substitua "SUA_CHAVE_DA_API_AQUI" pela sua chave real da API do Gemini.

4. Executando o Aplicativo Streamlit
   Com o ambiente virtual ativado e as dependências instaladas, execute o script:

Bash

streamlit run agente_de_ia_posts.py
Isso abrirá o aplicativo no seu navegador padrão.

💡 Como Usar
Conteúdo do Post: Digite o texto principal que você deseja transformar em um post de rede social.
Público Alvo: Especifique para quem o post é destinado (ex: "empreendedores", "entusiastas de tecnologia", "donos de pequenos negócios").
Tom de Voz: Selecione o tom que você quer para o post no menu suspenso (ex: "Engraçado", "Profissional").
Gerar Post: Clique no botão "Gerar Post" para que o Gemini crie o conteúdo para você.
🤝 Contribuições
Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novas funcionalidades. Abra uma issue ou envie um pull request.

📄 Licença
Este projeto está licenciado sob a licença MIT.
