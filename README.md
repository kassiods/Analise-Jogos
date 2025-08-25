# 🎮 Análise de Vendas de Jogos – Apresentação Visual

Este projeto explora a base de dados de vendas de jogos (`vgsales.csv`), gerando gráficos e insights para facilitar a compreensão do mercado de games.

## Estrutura do Projeto

```text
analise_jogos/
├─ data/
│  └─ vgsales.csv
├─ figs/                # Gráficos gerados
├─ src/
│  └─ analise_jogos.py  # Script principal
├─ README.md            # Este arquivo
└─ requirements.txt     # Dependências
```

## Como executar

1. Instale o Python 3 e crie o ambiente virtual:

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

2. Coloque o arquivo `vgsales.csv` na pasta `data/`.

3. Execute o script:

   ```powershell
   & .venv\Scripts\python.exe src/analise_jogos.py
   ```

4. Ou utilize o notebook para apresentação visual dos gráficos.

## Gráficos gerados

- **Matriz de correlação entre variáveis numéricas**
  - Relação entre vendas em diferentes regiões e totais.
- **Distribuição de vendas globais por jogo**
  - Mostra que poucos jogos vendem muito e muitos vendem pouco.
- **Composição regional de vendas nos 10 jogos mais vendidos**
  - Peso de cada região nas vendas dos maiores sucessos.
- **Vendas globais por plataforma (Top 10)**
  - Quais consoles/computadores lideram o mercado em vendas totais.

Todos os gráficos são salvos na pasta `figs/` e exibidos em sequência para facilitar a apresentação.

## Objetivo

- Visualizar tendências do mercado de games.
- Facilitar a comunicação dos resultados em reuniões e apresentações.
- Servir como base para discussões sobre estratégias, preferências regionais e plataformas líderes.

## Requisitos

- Python 3
- pandas
- numpy
- matplotlib

Instale as dependências com:

```powershell
pip install -r requirements.txt
```

## Créditos

- Base de dados: [Kaggle - Video Game Sales](https://www.kaggle.com/datasets/gregorut/videogamesales)
