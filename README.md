Coleção de Agentes de IA Básicos 🤖
Bem-vindo ao repositório "Coleção de Agentes de IA Básicos"! Este projeto é um compilado de implementações simples de agentes de Inteligência Artificial, criados a partir de diversos recursos de aprendizado. O principal objetivo aqui foi explorar diferentes abordagens e técnicas apresentadas por tutores em bootcamps, vídeos do YouTube e semanas de programação.

meche.mit.edu
Este repositório serve como um diário de bordo da minha jornada de aprendizado em IA, destacando a diversidade de métodos e a riqueza de conhecimento disponível na comunidade. Cada agente representa um passo nessa jornada, permitindo uma compreensão prática dos conceitos fundamentais da IA.

Conteúdo do Repositório 📚
Aqui você encontrará uma variedade de agentes de IA básicos, cada um implementado de acordo com um tutorial específico. Estes agentes são predominantemente agentes conversacionais (chatbots), criados através da utilização de grandes modelos de linguagem (LLMs) e otimizados por meio de diversas técnicas de prompt engineering. Os agentes podem abordar temas como:

🗣️ Chatbots simples: Agentes capazes de manter conversas básicas e responder a perguntas.

🤝 Agentes de assistência: Pequenos assistentes para tarefas específicas, demonstrando interação com LLMs.

✨ Exploração de prompt engineering: Exemplos de como diferentes prompts moldam o comportamento e as respostas dos agentes.

🧠 Outras implementações introdutórias de IA baseadas em LLM.

www.freepik.com
Cada agente geralmente reside em sua própria pasta, com seu próprio código e, se necessário, suas próprias dependências.

Como Usar ▶️
Para começar, clone o repositório para a sua máquina local:

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

business-science.github.io
Para executar um agente específico, navegue até a pasta do agente desejado e siga as instruções contidas no README.md ou nos comentários do código dentro dessa pasta (geralmente python seu_agente.py ou similar).

Instalação e Configuração ⚙️
Para rodar os projetos neste repositório, siga os passos de instalação e configuração abaixo. É altamente recomendado usar um ambiente virtual (.venv) para gerenciar as dependências do projeto.

1. Criar e Ativar o Ambiente Virtual (.venv)
   Usando o Anaconda Prompt (ou seu terminal de preferência), navegue até a pasta raiz do projeto clonado e crie um ambiente virtual:

python -m venv .venv

Após a criação, ative o ambiente virtual.

No Windows (Anaconda Prompt/CMD):

.\.venv\Scripts\activate

No macOS/Linux (Terminal):

source ./.venv/bin/activate

Você saberá que o ambiente está ativado quando (.venv) aparecer no início da linha de comando.

askubuntu.com 2. Instalar as Dependências
Com o ambiente virtual ativado, instale as bibliotecas necessárias. É uma boa prática ter um arquivo requirements.txt com todas as dependências. Se este arquivo estiver disponível no projeto, execute:

pip install -r requirements.txt

Caso contrário, você pode instalar as principais bibliotecas manualmente:

pip install langchain streamlit openai python-dotenv

3. Configurar Chaves de API (.env)
   Muitos dos agentes exigem chaves de API para interagir com os LLMs (como da OpenAI). Por questões de segurança, essas chaves NÃO devem ser commitadas no Git.

Crie um arquivo chamado .env no diretório raiz do projeto.

Dentro do arquivo .env, adicione suas chaves de API no formato CHAVE=SEU_VALOR, por exemplo:

OPENAI_API_KEY=sua_chave_secreta_aqui

Consulte os README.md específicos de cada agente ou arquivos .env.example (se fornecidos) para saber quais variáveis de ambiente são necessárias.

www.geeksforgeeks.org
Bibliotecas e Tecnologias Utilizadas 🛠️
Este projeto utiliza diversas bibliotecas e tecnologias para o desenvolvimento e execução dos agentes de IA:

Python: A linguagem de programação principal para a implementação dos agentes.

LangChain: Um framework para desenvolver aplicações alimentadas por modelos de linguagem, facilitando a criação de agentes complexos e cadeias de LLMs.

Streamlit: Uma ferramenta para criar aplicativos web interativos rapidamente, ideal para prototipar e exibir os agentes de IA.

OpenAI: APIs e modelos de IA, incluindo LLMs, que são utilizados para alimentar os agentes conversacionais.

Anaconda Prompt: Ambiente de linha de comando utilizado para gerenciar ambientes Python e instalar dependências.

www.vecteezy.com
Créditos e Recursos de Aprendizado 🎓
Um agradecimento especial a todos os tutores e criadores de conteúdo que tornaram este aprendizado possível! Sua paixão por ensinar e a clareza de suas explicações foram fundamentais.

www.vectorstock.com
Aqui estão os recursos de aprendizado que foram utilizados para a criação destes agentes. Se você está interessado em aprofundar seus conhecimentos, recomendo fortemente conferir estes materiais:

[Nome do Bootcamp/Canal/Evento/Autor] - [Link para a playlist/curso/vídeo específico, se disponível]

Breve descrição do tipo de agente ou conceito aprendido e como foi aplicado neste projeto.

[Nome do Bootcamp/Canal/Evento/Autor] - [Link para a playlist/curso/vídeo específico, se disponível]

Breve descrição do tipo de agente ou conceito aprendido e como foi aplicado neste projeto.

[Nome do Bootcamp/Canal/Evento/Autor] - [Link para a playlist/curso/vídeo específico, se disponível]

Breve descrição do tipo de agente ou conceito aprendido e como foi aplicado neste projeto.

[Nome do Bootcamp/Canal/Evento/Autor] - [Link para a playlist/curso/vídeo específico, se disponível]

Breve descrição do tipo de agente ou conceito aprendido e como foi aplicado neste projeto.

(Adicione mais itens conforme necessário)

Catálogo de Agentes no GitHub Pages 🌐
Em breve, este projeto contará com um catálogo interativo de todos os agentes, hospedado no GitHub Pages! Isso facilitará a visualização e o acesso a cada implementação, servindo como uma demonstração mais rica do portfólio. Fique atento às atualizações!

www.homeandlearn.co.uk
Contribuições 🤝
Este repositório é principalmente para fins de aprendizado pessoal, mas sugestões e melhorias são sempre bem-vindas! Se você identificar algum erro ou tiver uma ideia de como aprimorar alguma implementação, sinta-se à vontade para abrir uma issue ou enviar um pull request.

Licença 📜
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Espero que este repositório seja útil para quem está começando no mundo da IA e deseja explorar diferentes formas de implementar agentes básicos!
