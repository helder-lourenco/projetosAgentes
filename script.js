document.addEventListener("DOMContentLoaded", () => {
  const projectsContainer = document.getElementById("projects-container");
  const loadingMessage = document.getElementById("loading-message");
  const errorMessage = document.getElementById("error-message");

  // Substitua com as suas informações!
  const GITHUB_USERNAME = "SeuNomeDeUsuarioGitHub"; // Seu username do GitHub
  const REPO_NAME = "nome-do-seu-repositorio"; // Nome do repositório que você está usando para o GitHub Pages
  const PROJECTS_BASE_PATH = "projetos/"; // Caminho da pasta que contém seus subprojetos
  const GITHUB_API_URL = `https://api.github.com/repos/${GITHUB_USERNAME}/${REPO_NAME}/contents/${PROJECTS_BASE_PATH}`;
  const GITHUB_PAGES_BASE_URL = `https://${GITHUB_USERNAME}.github.io/${REPO_NAME}/`;
  const GITHUB_REPO_BROWSE_URL = `https://github.com/${GITHUB_USERNAME}/${REPO_NAME}/tree/main/`; // URL para navegar no repo

  // Função para buscar os projetos no GitHub API
  async function fetchProjects() {
    try {
      loadingMessage.classList.remove("hidden"); // Mostra a mensagem de carregamento
      errorMessage.classList.add("hidden"); // Esconde qualquer mensagem de erro anterior

      const response = await fetch(GITHUB_API_URL);

      if (!response.ok) {
        // Tenta ler a mensagem de erro da API
        const errorData = await response
          .json()
          .catch(() => ({ message: "Erro desconhecido." }));
        throw new Error(
          `Erro HTTP! Status: ${response.status} - ${
            errorData.message || response.statusText
          }`
        );
      }

      const data = await response.json();

      // Filtra apenas diretórios (pastas)
      const projects = data.filter((item) => item.type === "dir");

      if (projects.length === 0) {
        projectsContainer.innerHTML =
          '<p class="no-projects">Nenhum projeto encontrado na pasta especificada.</p>';
        loadingMessage.classList.add("hidden");
        return;
      }

      projects.forEach((project) => {
        const projectCard = document.createElement("a"); // Usamos 'a' para que o card seja clicável
        projectCard.href = getProjectUrl(project.name); // Define o link do card
        projectCard.target = "_blank"; // Abre em nova aba
        projectCard.classList.add("project-card");

        projectCard.innerHTML = `
                    <div class="project-card-header">${formatProjectName(
                      project.name
                    )}</div>
                    <div class="project-card-body">
                        <p>${getProjectDescription(project.name)}</p>
                        <span class="access-link">Acessar Projeto</span>
                    </div>
                `;
        projectsContainer.appendChild(projectCard);
      });
    } catch (error) {
      console.error("Falha ao carregar projetos:", error);
      errorMessage.textContent = `Erro ao carregar os projetos: ${error.message}. Por favor, verifique o console para mais detalhes.`;
      errorMessage.classList.remove("hidden"); // Mostra a mensagem de erro
      projectsContainer.innerHTML = ""; // Limpa os projetos em caso de erro
    } finally {
      loadingMessage.classList.add("hidden"); // Esconde a mensagem de carregamento no final
    }
  }

  // Função auxiliar para formatar o nome do projeto (ex: my-project -> My Project)
  function formatProjectName(name) {
    return name
      .replace(/-/g, " ") // Substitui hífens por espaços
      .split(" ")
      .map((word) => word.charAt(0).toUpperCase() + word.slice(1)) // Capitaliza cada palavra
      .join(" ");
  }

  // Função auxiliar para obter a descrição do projeto
  // Esta é uma função *simples*. Para descrições mais ricas,
  // você teria que ler um README.md de cada pasta ou usar um JSON.
  function getProjectDescription(projectName) {
    switch (projectName) {
      case "projeto1":
        return "Um exemplo de página estática com HTML e CSS.";
      case "projeto2":
        return "Uma aplicação JavaScript simples para demonstração.";
      // Adicione mais casos conforme seus projetos
      default:
        return "Nenhuma descrição disponível para este projeto.";
    }
  }

  // Função auxiliar para determinar a URL do projeto
  function getProjectUrl(projectName) {
    // Opção 1: Se cada subpasta tiver um index.html e você quer a GitHub Page dela
    // Ex: https://seunome.github.io/seurepositorio/projetos/projeto1/
    const projectPageUrl = `${GITHUB_PAGES_BASE_URL}${PROJECTS_BASE_PATH}${projectName}/`;

    // Opção 2: Se você quer apenas navegar para a pasta no repositório GitHub
    // Ex: https://github.com/SeuNomeDeUsuarioGitHub/nome-do-seu-repositorio/tree/main/projetos/projeto1
    const projectRepoUrl = `${GITHUB_REPO_BROWSE_URL}${PROJECTS_BASE_PATH}${projectName}`;

    // A escolha da URL depende de como você quer que o usuário acesse o projeto.
    // Se cada projeto no subdiretório 'projetos/' tem um `index.html` e você
    // configurou o GitHub Pages para servir esse subdiretório (mais complexo),
    // use projectPageUrl.
    // Caso contrário, ou para simplicidade, use projectRepoUrl.

    // Por padrão, vamos usar a URL do GitHub Pages se houver um index.html
    // ou a URL do repositório se não tiver.
    // Para uma implementação mais robusta, você pode verificar a existência
    // de um index.html via API do GitHub para cada pasta.
    // Por agora, vamos assumir que queremos ir para a URL do GitHub Pages se possível.
    return projectPageUrl; // ou projectRepoUrl, dependendo da sua necessidade
  }

  // Inicia o carregamento dos projetos
  fetchProjects();
});
