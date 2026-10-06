import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from datetime import datetime, timedelta


# ============================================================
# 1. GERAÇÃO DOS DADOS FICTÍCIOS
# ============================================================

def gera_dados_ficticios(num_registro=600):
    """
    Gera um DataFrame do Pandas com dados fictícios.
    """

    print(f"\nIniciando a geração de {num_registro} registros de venda...")

    produtos = {
        'Laptop Gamer': {
            'categoria': 'Eletrônicos',
            'preco': 7500.00
        },

        'Mouse Vertical': {
            'categoria': 'Acessórios',
            'preco': 250.00
        },

        'Teclado Mecânico': {
            'categoria': 'Acessórios',
            'preco': 550.00
        },

        'Monitor Ultrawide': {
            'categoria': 'Eletrônicos',
            'preco': 2800.00
        },

        'Cadeira Gamer': {
            'categoria': 'Móveis',
            'preco': 1200.00
        },

        'Headset 7.1': {
            'categoria': 'Acessórios',
            'preco': 800.00
        },

        'Placa de Vídeo': {
            'categoria': 'Hardware',
            'preco': 4500.00
        },

        'SSD 1TB': {
            'categoria': 'Hardware',
            'preco': 600.00
        }
    }

    lista_produtos = list(produtos.keys())

    cidades_estados = {
        'São Paulo': 'SP',
        'Rio de Janeiro': 'RJ',
        'Belo Horizonte': 'MG',
        'Porto Alegre': 'RS',
        'Salvador': 'BA',
        'Curitiba': 'PR',
        'Fortaleza': 'CE'
    }

    lista_cidades = list(cidades_estados.keys())

    dados_vendas = []

    data_inicial = datetime(2024, 1, 1)

    for i in range(num_registro):

        # Escolhe um produto aleatório
        produto_nome = random.choice(lista_produtos)

        # Gera uma data para o pedido
        data_pedido = data_inicial + timedelta(
            days=int(i / 5),
            hours=random.randint(0, 23)
        )

        # Quantidade comprada
        quantidade = random.randint(1, 5)

        # Escolhe uma cidade
        cidade = random.choice(lista_cidades)

        # Alguns produtos podem receber pequenos descontos
        if produto_nome in ['Mouse Vertical', 'Teclado Mecânico']:

            preco_unitario = (
                produtos[produto_nome]['preco']
                * np.random.uniform(0.9, 1.0)
            )

        else:

            preco_unitario = produtos[produto_nome]['preco']

        dados_vendas.append({
            'ID_Pedido': 1000 + i,
            'Data_Pedido': data_pedido,
            'Nome_Produto': produto_nome,
            'Categoria': produtos[produto_nome]['categoria'],
            'Preco_Unitario': round(preco_unitario, 2),
            'Quantidade': quantidade,
            'ID_Cliente': np.random.randint(100, 150),
            'Cidade': cidade,
            'Estado': cidades_estados[cidade]
        })

    print("Geração de dados concluída.\n")

    return pd.DataFrame(dados_vendas)


# ============================================================
# 2. CRIANDO O DATAFRAME
# ============================================================

df_vendas = gera_dados_ficticios(500)


# ============================================================
# 3. CONHECENDO OS DADOS
# ============================================================

print("\n==============================")
print("TIPO DA VARIÁVEL")
print("==============================")
print(type(df_vendas))


print("\n==============================")
print("TAMANHO DO DATAFRAME")
print("==============================")
print(df_vendas.shape)


print("\n==============================")
print("PRIMEIRAS LINHAS")
print("==============================")
print(df_vendas.head())


print("\n==============================")
print("ÚLTIMAS LINHAS")
print("==============================")
print(df_vendas.tail())


print("\n==============================")
print("INFORMAÇÕES DO DATAFRAME")
print("==============================")
df_vendas.info()


print("\n==============================")
print("ESTATÍSTICAS")
print("==============================")
print(df_vendas.describe())


print("\n==============================")
print("TIPOS DE DADOS")
print("==============================")
print(df_vendas.dtypes)


# ============================================================
# 4. TRATAMENTO E PREPARAÇÃO DOS DADOS
# ============================================================

# Converte a coluna para formato de data
df_vendas['Data_Pedido'] = pd.to_datetime(
    df_vendas['Data_Pedido']
)


# Calcula o faturamento de cada venda
df_vendas['Faturamento'] = (
    df_vendas['Preco_Unitario']
    * df_vendas['Quantidade']
)


# Cria uma classificação de entrega
df_vendas['Status_Entrega'] = (
    df_vendas['Estado'].apply(
        lambda estado:
        'Rápida'
        if estado in ['SP', 'RJ', 'MG']
        else 'Normal'
    )
)


# Criando coluna do mês
df_vendas['Mes'] = (
    df_vendas['Data_Pedido'].dt.month
)


print("\n==============================")
print("DADOS PREPARADOS")
print("==============================")
print(df_vendas.head())


# ============================================================
# 5. VERIFICANDO DADOS AUSENTES
# ============================================================

print("\n==============================")
print("VALORES AUSENTES")
print("==============================")

print(df_vendas.isnull().sum())


# ============================================================
# 6. REMOVENDO DUPLICADOS
# ============================================================

df_vendas = df_vendas.drop_duplicates()

print("\nQuantidade de registros após limpeza:")
print(len(df_vendas))


# ============================================================
# 7. FATURAMENTO TOTAL
# ============================================================

faturamento_total = df_vendas['Faturamento'].sum()

print("\n==============================")
print("FATURAMENTO TOTAL")
print("==============================")

print(
    f"R$ {faturamento_total:,.2f}"
)


# ============================================================
# 8. ESTATÍSTICAS COM NUMPY
# ============================================================

faturamentos = np.array(
    df_vendas['Faturamento']
)

media = np.mean(faturamentos)

maior = np.max(faturamentos)

menor = np.min(faturamentos)

mediana = np.median(faturamentos)


print("\n==============================")
print("ESTATÍSTICAS DO FATURAMENTO")
print("==============================")

print(
    f"Média: R$ {media:,.2f}"
)

print(
    f"Mediana: R$ {mediana:,.2f}"
)

print(
    f"Maior venda: R$ {maior:,.2f}"
)

print(
    f"Menor venda: R$ {menor:,.2f}"
)


# ============================================================
# 9. O QUE VENDER?
# PRODUTOS MAIS VENDIDOS
# ============================================================

produtos_mais_vendidos = (
    df_vendas
    .groupby('Nome_Produto')['Quantidade']
    .sum()
    .sort_values(ascending=False)
)


print("\n==============================")
print("PRODUTOS MAIS VENDIDOS")
print("==============================")

print(produtos_mais_vendidos)


# GRÁFICO

plt.figure(figsize=(10, 6))

sns.barplot(
    x=produtos_mais_vendidos.values,
    y=produtos_mais_vendidos.index
)

plt.title(
    'Produtos Mais Vendidos'
)

plt.xlabel(
    'Quantidade Vendida'
)

plt.ylabel(
    'Produto'
)

plt.tight_layout()

plt.show()


# ============================================================
# 10. ONDE FOCAR?
# FATURAMENTO POR CATEGORIA
# ============================================================

faturamento_categoria = (
    df_vendas
    .groupby('Categoria')['Faturamento']
    .sum()
    .sort_values(ascending=False)
)


print("\n==============================")
print("FATURAMENTO POR CATEGORIA")
print("==============================")

print(faturamento_categoria)


# GRÁFICO

plt.figure(figsize=(9, 6))

sns.barplot(
    x=faturamento_categoria.index,
    y=faturamento_categoria.values
)

plt.title(
    'Faturamento por Categoria'
)

plt.xlabel(
    'Categoria'
)

plt.ylabel(
    'Faturamento (R$)'
)

plt.xticks(rotation=20)

plt.tight_layout()

plt.show()


# ============================================================
# 11. QUANDO AGIR?
# FATURAMENTO AO LONGO DO TEMPO
# ============================================================

faturamento_mensal = (
    df_vendas
    .groupby('Mes')['Faturamento']
    .sum()
)


print("\n==============================")
print("FATURAMENTO POR MÊS")
print("==============================")

print(faturamento_mensal)


# GRÁFICO

plt.figure(figsize=(10, 6))

sns.lineplot(
    x=faturamento_mensal.index,
    y=faturamento_mensal.values,
    marker='o'
)

plt.title(
    'Evolução do Faturamento Mensal'
)

plt.xlabel(
    'Mês'
)

plt.ylabel(
    'Faturamento (R$)'
)

plt.xticks(
    range(1, 13)
)

plt.grid(True)

plt.tight_layout()

plt.show()


# ============================================================
# 12. PARA ONDE EXPANDIR?
# FATURAMENTO POR ESTADO
# ============================================================

faturamento_estado = (
    df_vendas
    .groupby('Estado')['Faturamento']
    .sum()
    .sort_values(ascending=False)
)


print("\n==============================")
print("FATURAMENTO POR ESTADO")
print("==============================")

print(faturamento_estado)


# GRÁFICO

plt.figure(figsize=(9, 6))

sns.barplot(
    x=faturamento_estado.index,
    y=faturamento_estado.values
)

plt.title(
    'Faturamento por Estado'
)

plt.xlabel(
    'Estado'
)

plt.ylabel(
    'Faturamento (R$)'
)

plt.tight_layout()

plt.show()


# ============================================================
# 13. FATURAMENTO POR CIDADE
# ============================================================

faturamento_cidade = (
    df_vendas
    .groupby('Cidade')['Faturamento']
    .sum()
    .sort_values(ascending=False)
)


print("\n==============================")
print("FATURAMENTO POR CIDADE")
print("==============================")

print(faturamento_cidade)


# GRÁFICO

plt.figure(figsize=(10, 6))

sns.barplot(
    x=faturamento_cidade.values,
    y=faturamento_cidade.index
)

plt.title(
    'Faturamento por Cidade'
)

plt.xlabel(
    'Faturamento (R$)'
)

plt.ylabel(
    'Cidade'
)

plt.tight_layout()

plt.show()


# ============================================================
# 14. ANÁLISE DOS STATUS DE ENTREGA
# ============================================================

status_entrega = (
    df_vendas['Status_Entrega']
    .value_counts()
)


print("\n==============================")
print("STATUS DAS ENTREGAS")
print("==============================")

print(status_entrega)


plt.figure(figsize=(7, 5))

sns.barplot(
    x=status_entrega.index,
    y=status_entrega.values
)

plt.title(
    'Quantidade por Status de Entrega'
)

plt.xlabel(
    'Status'
)

plt.ylabel(
    'Quantidade'
)

plt.tight_layout()

plt.show()


# ============================================================
# 15. RESULTADOS FINAIS
# ============================================================

produto_campeao = (
    produtos_mais_vendidos.idxmax()
)

produto_menos_vendido = (
    produtos_mais_vendidos.idxmin()
)

categoria_campea = (
    faturamento_categoria.idxmax()
)

melhor_mes = (
    faturamento_mensal.idxmax()
)

melhor_estado = (
    faturamento_estado.idxmax()
)

melhor_cidade = (
    faturamento_cidade.idxmax()
)


print("\n==========================================")
print("           RESULTADOS FINAIS")
print("==========================================")

print(
    "Produto mais vendido:",
    produto_campeao
)

print(
    "Produto menos vendido:",
    produto_menos_vendido
)

print(
    "Categoria com maior faturamento:",
    categoria_campea
)

print(
    "Mês com maior faturamento:",
    melhor_mes
)

print(
    "Estado com maior faturamento:",
    melhor_estado
)

print(
    "Cidade com maior faturamento:",
    melhor_cidade
)

print(
    f"Faturamento total: R$ {faturamento_total:,.2f}"
)

print("\nAnálise de vendas concluída com sucesso!")