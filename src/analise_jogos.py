# =====================
# 1) Imports e setup
# =====================


# =====================
# Apresentação dos Gráficos Principais
# =====================
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs('figs', exist_ok=True)

def save_show(fig, filename, descricao):
    path = os.path.join('figs', filename)
    fig.savefig(path, bbox_inches='tight', dpi=120)
    plt.show()
    plt.pause(0.001)
    print(f"[salvo] {path}")
    print(f"\n{descricao}\n")
    input("Pressione Enter para ver o próximo gráfico...")
    plt.close(fig)

CSV_PATH = 'data/vgsales.csv'
if not os.path.exists(CSV_PATH):
    raise FileNotFoundError(f"Não encontrei {CSV_PATH}. Baixe a base (vgsales.csv) e coloque em data/.")
raw = pd.read_csv(CSV_PATH)
df = raw.copy()
df.columns = [c.strip().replace(' ', '_').replace('-', '_') for c in df.columns]
if 'Year' in df.columns:
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce').astype('Int64')
if 'Year' in df.columns:
    df['Decade'] = (df['Year'] // 10) * 10
num_cols = [c for c in df.columns if df[c].dtype.kind in 'fi']

# Gráfico 6: Correlação entre variáveis numéricas
descricao_6 = "Matriz de correlação entre variáveis numéricas. Mostra como as vendas em diferentes regiões e totais se relacionam."
if len(num_cols) >= 2:
    corr = df[num_cols].corr()
    fig, ax = plt.subplots(figsize=(6,5))
    cax = ax.imshow(corr.values, aspect='auto')
    ax.set_xticks(range(len(corr.columns)))
    ax.set_yticks(range(len(corr.columns)))
    ax.set_xticklabels(corr.columns, rotation=45)
    ax.set_yticklabels(corr.columns)
    ax.set_title('Matriz de correlação (numéricas)')
    fig.colorbar(cax)
    save_show(fig, 'correlacao_numericas.png', descricao_6)

# Gráfico E: Distribuição de vendas globais por jogo
descricao_e = "Distribuição de vendas globais por jogo. Mostra que poucos jogos vendem muito e muitos vendem pouco."
if 'Global_Sales' in df.columns:
    fig, ax = plt.subplots(figsize=(9,4))
    ax.hist(df['Global_Sales'].clip(upper=df['Global_Sales'].quantile(0.99)), bins=40)
    ax.set_title('Distribuição de vendas globais por jogo')
    ax.set_xlabel('Vendas globais (milhões)')
    ax.set_ylabel('Contagem de jogos')
    save_show(fig, 'dist_vendas_globais.png', descricao_e)

# Gráfico F: Composição regional de vendas nos 10 jogos mais vendidos
descricao_f = "Composição regional de vendas nos 10 jogos mais vendidos. Mostra o peso de cada região nas vendas dos maiores sucessos."
reg_cols = ['NA_Sales','EU_Sales','JP_Sales','Other_Sales']
if set(reg_cols + ['Name']).issubset(df.columns):
    top10 = df.sort_values('Global_Sales', ascending=False).head(10).set_index('Name')
    fig, ax = plt.subplots(figsize=(10,5))
    bottom = np.zeros(len(top10))
    for col in reg_cols:
        ax.bar(top10.index.astype(str), top10[col].values, bottom=bottom, label=col)
        bottom += top10[col].values
    ax.set_title('Top 10 jogos – composição regional de vendas')
    ax.set_xlabel('Jogo')
    ax.set_ylabel('Vendas (milhões)')
    ax.tick_params(axis='x', rotation=45)
    for label in ax.get_xticklabels():
        label.set_ha('right')
    ax.legend()
    save_show(fig, 'top10_composicao_regional.png', descricao_f)

# Gráfico C: Vendas globais por plataforma (Top 10)
descricao_c = "Vendas globais por plataforma (Top 10). Mostra quais consoles/computadores lideram o mercado em vendas totais."
if {'Platform','Global_Sales'}.issubset(df.columns):
    vendas_plat = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(9,4))
    ax.bar(vendas_plat.index.astype(str), vendas_plat.values)
    ax.set_title('Vendas globais por plataforma (Top 10)')
    ax.set_xlabel('Plataforma')
    ax.set_ylabel('Vendas globais (milhões)')
    ax.tick_params(axis='x', rotation=45)
    save_show(fig, 'vendas_globais_por_plataforma.png', descricao_c)

print("Apresentação concluída! Todos os gráficos estão salvos em figs/ e exibidos em sequência.")