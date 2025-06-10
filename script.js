document.addEventListener("DOMContentLoaded", () => {
  const itemGrid = document.getElementById("item-grid");

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
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Agente%20Tradutor%20de%20%C3%A1udio%20com%20IA/README.MD", // LINK DO SEU PROJETO/PASTA
      progress: 100, // Exemplo de progresso (entre 0 e 100)
    },
    {
      name: "ANALISE DE VENDAS COM IA",
      imageUrl: "./assets/realtori_vendas.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Agente%20de%20IA%20-%20%20Relat%C3%B3rios%20de%20Vendas/README.md", // LINK DO SEU PROJETO/PASTA
      progress: 100, // Exemplo de progresso (entre 0 e 100)
    },
    {
      name: "APP DE GESTÃO DE PROJETOS COM IA",
      imageUrl: "./assets/projeto.jpg",
      githubLink:
        "https://github.com/helder-lourenco/AI_ProjectFlow-main/blob/main/README.md", // LINK DO SEU PROJETO/PASTA
      progress: 40, // Exemplo de progresso (entre 0 e 100)
    },
    // Adicione mais 19 projetos fictícios para ter 24 no total na primeira página
    {
      name: "EM CONSTRUÇÂO", // "AGENTE DE CRM INTELIGENTE",
      imageUrl: "./assets/Emconstrucao.png",
      githubLink: "https://github.com/helder-lourenco",
      progress: 0,
    },
    /*
    {
      name: "EM CONSTRUÇÂO", // "SISTEMA DE RECOMENDAÇÃO DE FILMES",
      imageUrl: "./assets/Emconstrucao.png",
      githubLink: "https://github.com/helder-lourenco",
      progress: 95,
    },
    {
      name: "EM CONSTRUÇÂO", // "ANALISADOR DE SENTIMENTOS DE TWEETS",
      imageUrl: "./assets/Emconstrucao.png",
      githubLink: "https://github.com/helder-lourenco",
      progress: 70,
    },
    {
      name: "EM CONSTRUÇÂO", // "GERADOR DE IDEIAS DE NEGÓCIOS",
      imageUrl: "./assets/ideias.jpg",
      githubLink: "https://github.com/helder-lourenco",
      progress: 60,
    },
    {
      name: "EM CONSTRUÇÂO", // "AGENTE DE MONITORAMENTO DE COTAÇÕES",
      imageUrl: "./assets/cotacoes.jpg",
      githubLink: "https://github.com/helder-lourenco",
      progress: 100,
    },
    {
      name: "EM CONSTRUÇÂO", // "CRIADOR DE ARTIGOS AUTOMÁTICOS",
      imageUrl: "./assets/artigos.jpg",
      githubLink: "https://github.com/helder-lourenco",
      progress: 85,
    },
    {
      name: "EM CONSTRUÇÂO", // "ASSISTENTE DE ESTUDO COM IA",
      imageUrl: "./assets/estudo.jpg",
      githubLink: "https://github.com/helder-lourenco",
      progress: 75,
    },
    {
      name: "CLASSIFICADOR DE IMAGENS DE ANIMAIS",
      imageUrl: "./assets/animais.jpg",
      githubLink: "https://github.com/helder-lourenco",
      progress: 90,
    },
    {
      name: "AGENTE DE GESTÃO DE ESTOQUE",
      imageUrl: "./assets/estoque.jpg",
      githubLink: "https://github.com/helder-lourenco",
      progress: 50,
    },
    {
      name: "BOT DE NOTÍCIAS PERSONALIZADO",
      imageUrl: "./assets/news_bot.jpg",
      githubLink: "https://github.com/helder-lourenco",
      progress: 100,
    },
    {
      name: "DETECTOR DE SPAM EM E-MAILS",
      imageUrl: "./assets/spam.jpg",
      githubLink: "https://github.com/helder-lourenco",
      progress: 98,
    },
    {
      name: "TRADUTOR DE CÓDIGO FONTE",
      imageUrl: "./assets/code_translate.jpg",
      githubLink: "https://github.com/helder-lourenco",
      progress: 65,
    },
    {
      name: "GERADOR DE PERGUNTAS E RESPOSTAS",
      imageUrl: "./assets/qa.jpg",
      githubLink: "https://github.com/helder-lourenco",
      progress: 80,
    },
    {
      name: "ASSISTENTE VIRTUAL PARA VIAGENS",
      imageUrl: "./assets/viagem.jpg",
      githubLink: "https://github.com/helder-lourenco",
      progress: 70,
    },
    {
      name: "ANALISADOR DE DADOS FINANCEIROS",
      imageUrl: "./assets/finance.jpg",
      githubLink: "https://github.com/helder-lourenco",
      progress: 92,
    },
    {
      name: "AGENTE DE RESERVAS DE RESTAURANTES",
      imageUrl: "./assets/restaurante.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Reservas%20Restaurante/README.md",
      progress: 88,
    },
    {
      name: "PLATAFORMA DE ENSINO ADAPTATIVO",
      imageUrl: "./assets/adaptive_learning.jpg",
      githubLink: "https://github.com/helder-lourenco",
      progress: 77,
    },
    {
      name: "SISTEMA DE PREVISÃO DE DEMANDA",
      imageUrl: "./assets/demanda.jpg",
      githubLink: "https://github.com/helder-lourenco",
      progress: 94,
    },
    {
      name: "AGENTE DE MONITORAMENTO DE REDES SOCIAIS",
      imageUrl: "./assets/social_media.jpg",
      githubLink: "https://github.com/helder-lourenco",
      progress: 81,
    },
    {
      name: "ASSISTENTE PARA SAÚDE E BEM-ESTAR",
      imageUrl: "./assets/saude.jpg",
      githubLink: "https://github.com/helder-lourenco",
      progress: 68,
    },
    // Início da segunda página (adicionar mais para preencher as páginas)
    {
      name: "AGENTE DE OTIMIZAÇÃO DE RH",
      imageUrl: "./assets/rh_opt.jpg",
      githubLink: "https://github.com/helder-lourenco",
      progress: 80,
    },
    {
      name: "GERADOR DE RELATÓRIOS AMBIENTAIS",
      imageUrl: "./assets/ambiental.jpg",
      githubLink: "https://github.com/helder-lourenco",
      progress: 75,
    },
    {
      name: "SISTEMA DE PREVENÇÃO DE FRAUDES",
      imageUrl: "./assets/fraude.jpg",
      githubLink: "https://github.com/helder-lourenco",
      progress: 95,
    },
    {
      name: "ASSISTENTE JURÍDICO VIRTUAL",
      imageUrl: "./assets/juridico.jpg",
      githubLink: "https://github.com/helder-lourenco",
      progress: 70,
    },
    {
      name: "AGENTE DE SUPORTE TÉCNICO",
      imageUrl: "./assets/suporte_tec.jpg",
      githubLink: "https://github.com/helder-lourenco",
      progress: 90,
    },
    {
      name: "ANALISADOR DE PERFORMANCE ESPORTIVA",
      imageUrl: "./assets/esporte.jpg",
      githubLink: "https://github.com/helder-lourenco",
      progress: 85,
    },
    {
      name: "GERADOR DE CONTRATOS AUTOMÁTICOS",
      imageUrl: "./assets/contratos.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Gerador%20Contratos/README.md",
      progress: 60,
    },
    {
      name: "SISTEMA DE RECONHECIMENTO FACIAL",
      imageUrl: "./assets/facial.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Reconhecimento%20Facial/README.md",
      progress: 55,
    },
    {
      name: "AGENTE DE GESTÃO DE EVENTOS",
      imageUrl: "./assets/eventos.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Gestao%20Eventos/README.md",
      progress: 78,
    },
    {
      name: "OTIMIZADOR DE LOGÍSTICA DE ENTREGA",
      imageUrl: "./assets/logistica.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Otimizacao%20Logistica/README.md",
      progress: 93,
    },
    {
      name: "ASSISTENTE PARA COMPRAS ONLINE",
      imageUrl: "./assets/compras.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Assistente%20Compras/README.md",
      progress: 82,
    },
    {
      name: "GERADOR DE CURRÍCULOS COM IA",
      imageUrl: "./assets/cv.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Gerador%20CV/README.md",
      progress: 72,
    },
    {
      name: "SISTEMA DE RECONHECIMENTO DE VOZ",
      imageUrl: "./assets/voz.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Reconhecimento%20Voz/README.md",
      progress: 89,
    },
    {
      name: "AGENTE DE SEGURANÇA CIBERNÉTICA",
      imageUrl: "./assets/ciberseguranca.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Ciberseguranca/README.md",
      progress: 96,
    },
    {
      name: "ANALISADOR DE DADOS DE RH",
      imageUrl: "./assets/rh_data.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Analise%20RH/README.md",
      progress: 79,
    },
    {
      name: "GERADOR DE CRONOGRAMAS DE PROJETOS",
      imageUrl: "./assets/cronograma.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Gerador%20Cronograma/README.md",
      progress: 84,
    },
    {
      name: "AGENTE DE MARKETING DIGITAL",
      imageUrl: "./assets/marketing.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Marketing%20Digital/README.md",
      progress: 88,
    },
    {
      name: "SISTEMA DE GESTÃO DE CLIENTES",
      imageUrl: "./assets/gestao_clientes.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Gestao%20Clientes/README.md",
      progress: 91,
    },
    {
      name: "ASSISTENTE PARA ESCRITA CRIATIVA",
      imageUrl: "./assets/escrita_criativa.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Escrita%20Criativa/README.md",
      progress: 74,
    },
    {
      name: "AGENTE DE EDUCAÇÃO PERSONALIZADA",
      imageUrl: "./assets/educacao_pers.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Educacao%20Personalizada/README.md",
      progress: 87,
    },
    {
      name: "GERADOR DE IDEIAS DE CONTEÚDO PARA BLOG",
      imageUrl: "./assets/blog_ideas.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Ideias%20Blog/README.md",
      progress: 76,
    },
    {
      name: "SISTEMA DE GESTÃO DE METAS",
      imageUrl: "./assets/metas.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Gestao%20Metas/README.md",
      progress: 83,
    },
    {
      name: "ANALISADOR DE TEXTO PARA PLÁGIO",
      imageUrl: "./assets/plagio.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Analise%20Plagio/README.md",
      progress: 69,
    },
    {
      name: "AGENTE DE OTIMIZAÇÃO DE ENERGIA",
      imageUrl: "./assets/energia_opt.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Otimizacao%20Energia/README.md",
      progress: 90,
    },
    {
      name: "GERADOR DE RESUMOS DE NOTÍCIAS",
      imageUrl: "./assets/news_summary.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Resumos%20Noticias/README.md",
      progress: 92,
    },
    {
      name: "ASSISTENTE PARA CRIAÇÃO DE APRESENTAÇÕES",
      imageUrl: "./assets/presentation_maker.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Criacao%20Apresentacoes/README.md",
      progress: 78,
    },
    {
      name: "SISTEMA DE RECONHECIMENTO DE OBJETOS",
      imageUrl: "./assets/object_rec.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Reconhecimento%20Objetos/README.md",
      progress: 85,
    },
    {
      name: "AGENTE DE PROSPECÇÃO DE VENDAS",
      imageUrl: "./assets/prospeccao.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Prospeccao%20Vendas/README.md",
      progress: 88,
    },
    {
      name: "GERADOR DE DESCRIÇÕES DE PRODUTOS",
      imageUrl: "./assets/product_desc.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Descricoes%20Produtos/README.md",
      progress: 71,
    },
    {
      name: "ASSISTENTE DE PESQUISA ACADÊMICA",
      imageUrl: "./assets/pesquisa_acad.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Pesquisa%20Academica/README.md",
      progress: 93,
    },
    {
      name: "SISTEMA DE GESTÃO DE CONTEÚDO",
      imageUrl: "./assets/content_mgmt.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Gestao%20Conteudo/README.md",
      progress: 86,
    },
    {
      name: "AGENTE DE ATENDIMENTO AO CIDADÃO",
      imageUrl: "./assets/cidadao.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Atendimento%20Cidadao/README.md",
      progress: 89,
    },
    {
      name: "GERADOR DE SCRIPTS PARA VÍDEOS",
      imageUrl: "./assets/video_script.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Scripts%20Video/README.md",
      progress: 79,
    },
    {
      name: "ASSISTENTE DE ANÁLISE DE MERCADO",
      imageUrl: "./assets/market_analysis.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Analise%20Mercado/README.md",
      progress: 94,
    },
    {
      name: "SISTEMA DE MONITORAMENTO DE PREÇOS",
      imageUrl: "./assets/price_monitor.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Monitor%20Precos/README.md",
      progress: 91,
    },
    {
      name: "AGENTE DE COBRANÇA AUTOMATIZADA",
      imageUrl: "./assets/cobranca.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Cobranca%20Automatizada/README.md",
      progress: 73,
    },
    {
      name: "GERADOR DE RELATÓRIOS FINANCEIROS",
      imageUrl: "./assets/finance_report.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Relatorios%20Financeiros/README.md",
      progress: 90,
    },
    {
      name: "ASSISTENTE DE RECRUTAMENTO E SELEÇÃO",
      imageUrl: "./assets/recrutamento.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Recrutamento%20Selecao/README.md",
      progress: 84,
    },
    {
      name: "SISTEMA DE GESTÃO DE PEDIDOS",
      imageUrl: "./assets/pedidos.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Gestao%20Pedidos/README.md",
      progress: 88,
    },
    {
      name: "AGENTE DE ALERTA DE SEGURANÇA",
      imageUrl: "./assets/security_alert.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Alerta%20Seguranca/README.md",
      progress: 95,
    },
    {
      name: "GERADOR DE E-MAILS DE MARKETING",
      imageUrl: "./assets/email_marketing.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Emails%20Marketing/README.md",
      progress: 77,
    },
    {
      name: "ASSISTENTE PARA CRIAÇÃO DE CURSOS",
      imageUrl: "./assets/course_creator.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Criacao%20Cursos/README.md",
      progress: 81,
    },
    {
      name: "SISTEMA DE GESTÃO DE ESTOQUE DE PRODUTOS",
      imageUrl: "./assets/product_stock.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Gestao%20Estoque%20Produtos/README.md",
      progress: 92,
    },
    {
      name: "AGENTE DE ENGAJAMENTO EM REDES SOCIAIS",
      imageUrl: "./assets/social_engagement.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Engajamento%20Redes%20Sociais/README.md",
      progress: 89,
    },
    {
      name: "GERADOR DE PITCH DECKS",
      imageUrl: "./assets/pitch_deck.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Pitch%20Decks/README.md",
      progress: 83,
    },
    {
      name: "ASSISTENTE PARA GESTÃO DE TEMPO",
      imageUrl: "./assets/time_management.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Gestao%20Tempo/README.md",
      progress: 91,
    },
    {
      name: "SISTEMA DE GESTÃO DE PROJETOS ÁGEIS",
      imageUrl: "./assets/agile_project.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Projetos%20Ageis/README.md",
      progress: 87,
    },
    {
      name: "AGENTE DE SUGESTÃO DE PALAVRAS-CHAVE",
      imageUrl: "./assets/keywords.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Sugestao%20Keywords/README.md",
      progress: 94,
    },
    {
      name: "GERADOR DE SUMÁRIOS EXECUTIVOS",
      imageUrl: "./assets/executive_summary.jpg",
      githubLink:
        "https://github.com/helder-lourenco/projetosAgentes/blob/main/projetos/Sumarios%20Executivos/README.md",
      progress: 80,
    }, */
  ];

  const cardsPerPage = 8; // 4 colunas * 2 linhas = 8 cards por página
  let currentPage = 1;
  let totalPages = Math.ceil(projectsData.length / cardsPerPage);

  const currentPageTopSpan = document.getElementById("current-page-top");
  const currentPageBottomSpan = document.getElementById("current-page-bottom");
  const prevPageTopBtn = document.getElementById("prev-page-top");
  const nextPageTopBtn = document.getElementById("next-page-top");
  const prevPageBottomBtn = document.getElementById("prev-page-bottom");
  const nextPageBottomBtn = document.getElementById("next-page-bottom");

  // Função para renderizar os cards
  function renderProjects() {
    if (projectsData.length === 0) {
      itemGrid.innerHTML =
        '<p class="no-projects">Nenhum projeto disponível no momento.</p>';
      return;
    }

    itemGrid.innerHTML = ""; // Clear existing content before rendering

    const startIndex = (currentPage - 1) * cardsPerPage;
    const endIndex = startIndex + cardsPerPage;
    const projectsToDisplay = projectsData.slice(startIndex, endIndex);

    projectsToDisplay.forEach((project) => {
      const itemCard = document.createElement("div");
      itemCard.classList.add("item-card"); // Usando a classe existente

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

    updatePaginationInfo();
    updatePaginationButtons();
  }

  function updatePaginationInfo() {
    currentPageTopSpan.textContent = `${currentPage} de ${totalPages}`;
    currentPageBottomSpan.textContent = `${currentPage} de ${totalPages}`;
  }

  function updatePaginationButtons() {
    prevPageTopBtn.disabled = currentPage === 1;
    prevPageBottomBtn.disabled = currentPage === 1;
    nextPageTopBtn.disabled = currentPage === totalPages;
    nextPageBottomBtn.disabled = currentPage === totalPages;
  }

  function goToNextPage() {
    if (currentPage < totalPages) {
      currentPage++;
      renderProjects();
    }
  }

  function goToPrevPage() {
    if (currentPage > 1) {
      currentPage--;
      renderProjects();
    }
  }

  // Event Listeners para os botões de paginação
  prevPageTopBtn.addEventListener("click", goToPrevPage);
  nextPageTopBtn.addEventListener("click", goToNextPage);
  prevPageBottomBtn.addEventListener("click", goToPrevPage);
  nextPageBottomBtn.addEventListener("click", goToNextPage);

  // Renderizar os cards na primeira carga da página
  renderProjects();
});
