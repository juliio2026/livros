# Importação das bibliotecas que utilizei para manipular o banco de dados, analisar os dados e gerar os gráficos
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as seaborn_plot

# ==============================================================================
# PASSO 1: Conectar ao banco de dados SQLite, criar a tabela e inserir os dados
# Descrição: Nesta primeira etapa, eu criei a conexão com o banco de dados SQLite 
# 'dados_vendas.db'. Em seguida, criei a estrutura da tabela 'vendas1' e populei 
# com os registros do histórico de vendas do último ano fornecidos no roteiro[cite: 2, 3].
# ==============================================================================
conexao = sqlite3.connect('dados_vendas.db')
cursor = conexao.cursor()

# Criação da tabela de vendas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vendas1 (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATE,
    produto TEXT,
    categoria TEXT,
    valor_venda REAL
)
""")

# Inserção dos dados de vendas do ano de 2023
cursor.execute("SELECT COUNT(*) FROM vendas1")
if cursor.fetchone()[0] == 0:
    cursor.execute("""
    INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) VALUES
    ('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
    ('2023-01-05', 'Produto B', 'Roupas', 350.00),
    ('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
    ('2023-03-15', 'Produto D', 'Livros', 200.00),
    ('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
    ('2023-04-02', 'Produto F', 'Roupas', 400.00),
    ('2023-05-05', 'Produto G', 'Livros', 150.00),
    ('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
    ('2023-07-20', 'Produto I', 'Roupas', 600.00),
    ('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
    ('2023-09-30', 'Produto K', 'Livros', 300.00),
    ('2023-10-05', 'Produto L', 'Roupas', 450.00),
    ('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
    ('2023-12-20', 'Produto N', 'Livros', 250.00);
    """)
    conexao.commit()

# ==============================================================================
# PASSO 2: Explorar e preparar os dados
# Descrição: Nesta etapa, eu importei os dados salvos do SQLite diretamente para 
# um DataFrame do Pandas (df_vendas). Isso me permitiu visualizar as primeiras 
# linhas da tabela e checar a estrutura dos dados para garantir que estavam prontos[cite: 3].
# ==============================================================================
df_vendas = pd.read_sql_query("SELECT * FROM vendas1", conexao)
conexao.close() # Encarrei a conexão pois os dados já foram carregados na memória

print("--- PRIMEIRAS LINHAS DA MINHA TABELA DE VENDAS ---")
display(df_vendas.head())

print("\n--- RESUMO DA ESTRUTURA DOS MEUS DADOS ---")
df_vendas.info()

# ==============================================================================
# PASSO 3: Análise dos dados
# Descrição: Aqui eu realizei a análise descritiva das vendas. Calculei estatísticas 
# principais (como média e total) e fiz um agrupamento por categoria para descobrir 
# qual categoria de produtos gerou mais faturamento para a empresa[cite: 4].
# ==============================================================================
print("\n--- ESTATÍSTICAS DESCRITIVAS DOS VALORES DE VENDA ---")
print(df_vendas['valor_venda'].describe())

# Agrupei o valor total vendido por cada categoria de produto
vendas_por_categoria = df_vendas.groupby('categoria')['valor_venda'].sum().reset_index()
print("\n--- TOTAL QUE CADASTRASSEI EM VENDAS POR CATEGORIA ---")
display(vendas_por_categoria)

# ==============================================================================
# PASSO 4: Visualização dos dados
# Descrição: Para facilitar a interpretação dos meus achados, utilizei as 
# bibliotecas Matplotlib e Seaborn para plotar dois gráficos: um gráfico de barras 
# mostrando o faturamento por categoria e um gráfico de linha com a evolução das vendas no tempo[cite: 4].
# ==============================================================================
seaborn_plot.set_theme(style="whitegrid")

# Gráfico 1: Construí um gráfico de barras para comparar o faturamento entre categorias
plt.figure(figsize=(8, 5))
# Correção aplicada: adicionei hue='categoria' e legend=False para evitar o aviso
seaborn_plot.barplot(data=vendas_por_categoria, x='categoria', y='valor_venda', hue='categoria', palette='Blues_d', legend=False)
plt.title('Total de Vendas por Categoria (Minha Análise)')
plt.xlabel('Categoria de Produtos')
plt.ylabel('Faturamento Total (R$)')
plt.show()

# Gráfico 2: Criei um gráfico de linha para acompanhar a oscilação das vendas mês a mês
df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'])
plt.figure(figsize=(12, 5))
plt.plot(df_vendas['data_venda'], df_vendas['valor_venda'], marker='o', color='b', linestyle='-')
plt.title('Evolução das Vendas ao Longo de 2023')
plt.xlabel('Data das Vendas')
plt.ylabel('Valor da Venda (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
