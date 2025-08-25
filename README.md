project:
  title: "🎮 Análise de Vendas de Jogos – Apresentação Visual"
  description: >
    Projeto de análise exploratória da base de vendas de jogos (vgsales.csv),
    com geração de gráficos e insights para melhor compreensão do mercado de games.
    
execution:
  steps:
    - step: "Criar ambiente virtual e instalar dependências"
      commands:
        - "python -m venv .venv"
        - ".venv\\Scripts\\Activate.ps1"
        - "pip install -r requirements.txt"
    - step: "Colocar o dataset"
      details: "Mover o arquivo vgsales.csv para a pasta data/"
    - step: "Rodar o script"
      commands:
        - "& .venv\\Scripts\\python.exe src/analise_jogos.py"
    - step: "Abrir o notebook"
      details: "notebooks/analise_jogos.ipynb para apresentação visual dos gráficos"

graphics:
  - name: "Matriz de correlação"
    description: "Relação entre vendas em diferentes regiões e totais"
  - name: "Distribuição de vendas globais"
    description: "Mostra que poucos jogos vendem muito e muitos vendem pouco"
  - name: "Composição regional dos 10 jogos mais vendidos"
    description: "Peso de cada região nas vendas dos maiores sucessos"
  - name: "Vendas globais por plataforma (Top 10)"
    description: "Quais consoles/computadores lideram o mercado em vendas totais"
  notes: "Todos os gráficos são salvos em figs/ e exibidos em sequência para apresentação"

objectives:
  - "Visualizar tendências do mercado de games"
  - "Facilitar a comunicação dos resultados em reuniões e apresentações"
  - "Apoiar discussões sobre estratégias, preferências regionais e plataformas líderes"

requirements:
  python: "3.x"
  libraries:
    - pandas
    - numpy
    - matplotlib
  install_command: "pip install -r requirements.txt"

credits:
  dataset: "Kaggle – Video Game Sales"
  purpose: "Desenvolvido para fins acadêmicos e didáticos"

