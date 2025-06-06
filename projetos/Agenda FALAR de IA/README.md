# 🤖 Gerador de Agenda de Discussão de IA para Empresas

Este projeto é um gerador de agenda de discussão de IA para empresas, utilizando agentes autônomos para buscar notícias relevantes e planejar conteúdo relacionado a inovações e avanços em Inteligência Artificial para segmentos de negócio específicos ou para o mercado em geral.

## 🚀 Como Funciona

O sistema é composto por agentes inteligentes que interagem para cumprir a tarefa principal:

1.  **Agente Buscador de Notícias (`agente_buscador_noticias`):** Pesquisa as 5 notícias mais relevantes sobre inovação e IA, com base em um segmento de negócio escolhido (ou notícias gerais se 'Todos' for selecionado). Ele utiliza a ferramenta Google Search para encontrar fontes confiáveis e com alto impacto.

2.  **Agente Planejador de Conteúdo (`agente_planejador`):** Com base nas notícias coletadas pelo Agente Buscador, este agente gera um plano detalhado para postagens em redes sociais ou blog. Cada plano inclui título, público-alvo, objetivo, pontos de discussão, chamada para ação (CTA), hashtags e formato sugerido.

## 🛠️ Requisitos e Configuração

Para rodar este projeto, você precisará ter o Python instalado e seguir os passos abaixo:

### 1. Clonar o Repositório

```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd <nome_do_seu_repositorio>
```
