document.addEventListener("DOMContentLoaded", () => {
  const projectsContainer = document.getElementById("projects-container");

  // **DEFINA SEUS PROJETOS AQUI**
  // Cada objeto na array representa um projeto.
  // Certifique-se de que o 'link' esteja correto!
  const projectsData = [
    {
      name: "Meu Primeiro Projeto",
      description:
        "Uma página web simples sobre meu hobby favorito, feita com HTML e CSS.",
      link: "https://seunome.github.io/seurepositorio/projetos/meu-primeiro-projeto/index.html", // Exemplo de link para uma GitHub Page de subpasta
    },
    {
      name: "Calculadora JS",
      description: "Uma calculadora interativa construída com JavaScript puro.",
      link: "https://seunome.github.io/seurepositorio/projetos/calculadora-js/", // Exemplo de link para uma GitHub Page de subpasta
    },
    {
      name: "Portfólio Antigo",
      description: "Meu antigo site de portfólio, apenas para referência.",
      link: "https://github.com/SeuNomeDeUsuarioGitHub/seurepositorio/tree/main/projetos/portfolio-antigo", // Exemplo de link direto para a pasta no GitHub
    },
    {
      name: "Jogo da Memória",
      description:
        "Um divertido jogo da memória desenvolvido para treinar lógica com JS.",
      link: "https://seunome.github.io/seurepositorio/projetos/jogo-da-memoria/index.html",
    },
    // Adicione mais projetos aqui seguindo o mesmo formato
  ];

  function renderProjects() {
    if (projectsData.length === 0) {
      projectsContainer.innerHTML =
        '<p class="no-projects">Nenhum projeto disponível no momento.</p>';
      return;
    }

    projectsData.forEach((project) => {
      const projectCard = document.createElement("a");
      projectCard.href = project.link;
      projectCard.target = "_blank"; // Abre em nova aba
      projectCard.classList.add("project-card");

      projectCard.innerHTML = `
                <div class="project-card-header">${project.name}</div>
                <div class="project-card-body">
                    <p>${project.description}</p>
                    <span class="access-link">Acessar Projeto</span>
                </div>
            `;
      projectsContainer.appendChild(projectCard);
    });
  }

  // Chama a função para renderizar os projetos quando a página carregar
  renderProjects();
});
