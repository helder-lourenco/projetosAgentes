document.addEventListener("DOMContentLoaded", () => {
  const itemGrid = document.getElementById("item-grid");

  // **DEFINA SEUS PROJETOS/FILMES AQUI**
  // Cada objeto na array representa um item (filme/projeto).
  // Certifique-se de que o 'githubLink' esteja correto para cada item!
  const projectsData = [
    {
      name: "AGENTE DE IA POSTS",
      imageUrl: "./assets/posts.png",
      githubLink:
        "https://github.com/SeuNomeDeUsuarioGitHub/seurepositorio/tree/main/projetos/liga-da-justica", // LINK DO SEU PROJETO/PASTA
    },

    {
      name: "AGENTE NOTICIAS SOBRE IA",
      imageUrl: "./assets/noticias.jpg",
      githubLink:
        "https://github.com/SeuNomeDeUsuarioGitHub/seurepositorio/tree/main/projetos/liga-da-justica", // LINK DO SEU PROJETO/PASTA
    },
  ];

  // Função para renderizar os cards
  function renderProjects() {
    if (projectsData.length === 0) {
      itemGrid.innerHTML =
        '<p class="no-projects">Nenhum projeto disponível no momento.</p>';
      return;
    }

    projectsData.forEach((project) => {
      const itemCard = document.createElement("div");
      itemCard.classList.add("item-card");

      itemCard.innerHTML = `
                <img src="${project.imageUrl}" alt="${project.name}">
                <h3>${project.name}</h3>
                <a href="${project.githubLink}" target="_blank" class="rate-button">Acessar Projeto</a>
            `;
      itemGrid.appendChild(itemCard);
    });
  }

  renderProjects();
});
