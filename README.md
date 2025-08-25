```markdown
# 🎮 Análise de Vendas de Jogos – Apresentação Visual
> Projeto de análise exploratória da base de **vendas de jogos (vgsales.csv)**, com geração de **gráficos e insights** para melhor compreensão do mercado de games.

---

## 📂 Estrutura do Projeto
```

analise\_jogos/
├─ data/
│  └─ vgsales.csv       # Base de dados
├─ figs/                # Gráficos gerados
├─ src/
│  └─ analise\_jogos.py  # Script principal
├─ README.md            # Este arquivo
└─ requirements.txt     # Dependências

````

---

## 🚀 Como Executar

1. **Criar ambiente virtual e instalar dependências**  
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
````

2. **Colocar o dataset** `vgsales.csv` na pasta `data/`.

3. **Rodar o script**

   ```powershell
   & .venv\Scripts\python.exe src/analise_jogos.py
   ```

4. **Ou abrir o notebook** em `notebooks/analise_jogos.ipynb` para apresentação visual dos gráficos.

---

## 📊 Gráficos Gerados

✅ **Matriz de correlação entre variáveis numéricas**
Relação entre vendas em diferentes regiões e totais.

✅ **Distribuição de vendas globais por jogo**
Mostra que poucos jogos vendem muito e muitos vendem pouco.

✅ **Composição regional nos 10 jogos mais vendidos**
Peso de cada região nas vendas dos maiores sucessos.

✅ **Vendas globais por plataforma (Top 10)**
Quais consoles/computadores lideram o mercado em vendas totais.

📌 Todos os gráficos são **salvos em `figs/`** e exibidos em sequência para facilitar a apresentação.

---

## 🎯 Objetivos

* 🔎 Visualizar **tendências do mercado de games**.
* 📈 Facilitar a **comunicação dos resultados** em reuniões e apresentações.
* 🎮 Apoiar discussões sobre **estratégias, preferências regionais e plataformas líderes**.

---

## 🛠️ Requisitos

* Python 3
* [pandas](https://pandas.pydata.org/)
* [numpy](https://numpy.org/)
* [matplotlib](https://matplotlib.org/)

Instale com:

```powershell
pip install -r requirements.txt
```

---

## 📚 Créditos

* 📊 Base de dados: [Kaggle – Video Game Sales](https://www.kaggle.com/datasets/gregorut/videogamesales)

