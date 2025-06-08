document.addEventListener("DOMContentLoaded", () => {
  const itemGrid = document.getElementById("item-grid");

  // **DEFINA SEUS PROJETOS/FILMES AQUI**
  // Cada objeto na array representa um item (filme/projeto).
  // Certifique-se de que o 'githubLink' esteja correto para cada item!
  // Adicione a propriedade 'progress' para cada projeto (valor entre 0 e 100).
  const projectsData = [
    {
      name: "AGENTE DE IA POSTS",
      imageUrl: "./assets/posts.png",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Agente%20de%20ia%20posts/README.md", // LINK DO SEU PROJETO/PASTA
      progress: 100, // Exemplo de progresso (entre 0 e 100)
    },

    {
      name: "AGENTE NOTICIAS SOBRE IA",
      imageUrl: "./assets/noticias.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Agenda%20FALAR%20de%20IA/README.md", // LINK DO SEU PROJETO/PASTA
      progress: 100, // Exemplo de progresso (entre 0 e 100)
    },

    {
      name: "IA AUDIO TRANSLATOR ING/PT-BR",
      // Este projeto é um tradutor de texto que utiliza IA para traduzir entre diferentes idiomas.
      imageUrl: "./assets/tradutor.png",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Agenda%20FALAR%20de%20IA/README.md", // LINK DO SEU PROJETO/PASTA
      progress: 100, // Exemplo de progresso (entre 0 e 100)
    },

    {
      name: "APP DE GESTÃO DE PROJETOS COM IA",
      imageUrl: "./assets/projeto.jpg",
      githubLink:
        "https://github.com/helder-lourenco/AI_ProjectFlow-main/blob/main/README.md", // LINK DO SEU PROJETO/PASTA
      progress: 40, // Exemplo de progresso (entre 0 e 100)
    },
    // Adicione mais projetos aqui, se necessário
    // {
    //   name: "NOVO PROJETO",
    //   imageUrl: "./assets/new_project.jpg",
    //   githubLink: "https://github.com/helder-lourenco/novo-projeto/README.md",
    //   progress: 30,
    // },
  ];

  // Função para renderizar os cards
  function renderProjects() {
    if (projectsData.length === 0) {
      itemGrid.innerHTML =
        '<p class="no-projects">Nenhum projeto disponível no momento.</p>';
      return;
    }

    itemGrid.innerHTML = ""; // Clear existing content before rendering

    projectsData.forEach((project) => {
      const itemCard = document.createElement("div");
      itemCard.classList.add("item-card");

      // Ensure progress is a number and within 0-100
      const projectProgress =
        typeof project.progress === "number"
          ? Math.max(0, Math.min(100, project.progress))
          : 0;

      itemCard.innerHTML = `
                <img src="${project.imageUrl}" alt="${project.name}">
                <h3>${project.name}</h3>
                <div class="progress-container">
                    <div class="progress-bar" style="width: ${projectProgress}%"></div>
                    <span class="progress-value">${projectProgress}%</span>
                </div>
                <a href="${project.githubLink}" target="_blank" class="rate-button">Acessar Projeto</a>
            `;
      itemGrid.appendChild(itemCard);
    });
  }

  renderProjects();
});
