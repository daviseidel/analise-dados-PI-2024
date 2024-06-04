# MATLIB: Biblioteca para visualização de dados
import matplotlib.pyplot as plt
# SEABORN: Biblioteca para organizar os dados e visualização nos gráficos
import seaborn as sns
import pandas as pd

# Load the data from the provided CSV file
file_path = './data.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataframe to understand its structure
data.head()

# Configuração para visualização
sns.set(style="whitegrid")

## DEMOGRAFIA

# Gráfico de barras para a idade x gênero
plt.figure(figsize=(10, 6))
sns.displot(data=data, x='Qual é a sua idade?', hue='Qual seu gênero?', kde="true")
plt.title('Distribuição de Idade e Gênero')
plt.xlabel('Idade')
plt.ylabel('Contagem')
# plt.legend(title='Gênero')
plt.show()

# Gráfico de barras para a frequência de exercício físico
plt.figure(figsize=(10, 6))
sns.displot(data=data, x='Com que frequência você pratica atividades físicas?', kde="true")
plt.title('Frequência de Atividade Física')
plt.xlabel('Frequência')
plt.ylabel('Contagem')
plt.show()
"""
# Gráfico de barras para a duração das sessões de exercício
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='Qual é a duração média das suas sessões de exercício?')
plt.title('Duração Média das Sessões de Exercício')
plt.xlabel('Duração')
plt.ylabel('Contagem')
plt.show()

# Analisar e preparar os dados para o tipo de exercício
exercise_types = data['Que tipo de exercício físico você mais pratica? (marque todas as opções aplicáveis)'].str.get_dummies(', ')

# Gráfico de barras para o tipo de exercício físico
plt.figure(figsize=(12, 8))
exercise_types.sum().sort_values(ascending=False).plot(kind='bar')
plt.title('Tipos de Exercício Físico Praticado')
plt.xlabel('Tipo de Exercício')
plt.ylabel('Contagem')
plt.show()


# Gráfico de barras para a frequência de leitura
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='Com que frequência você lê livros?')
plt.title('Frequência de Leitura de Livros')
plt.xlabel('Frequência')
plt.ylabel('Contagem')
plt.show()

# Gráfico de barras para a combinação de leitura com atividade física
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='Você já tentou combinar a leitura com a atividade física, como ouvir audiolivros enquanto se exercita?')
plt.title('Combinação de Leitura com Atividade Física')
plt.xlabel('Tentativa de Combinação')
plt.ylabel('Contagem')
plt.show()

# Gráfico de barras para a concentração após exercício físico
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='Como você avalia a sua concentração durante a leitura após uma sessão de exercício físico?')
plt.title('Concentração Durante a Leitura Após Exercício Físico')
plt.xlabel('Nível de Concentração')
plt.ylabel('Contagem')
plt.show()

# Gráfico de barras para o impacto do exercício na aprendizagem e memória
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='Você acredita que o exercício físico regular impacta positivamente sua capacidade de aprendizagem e memória?')
plt.title('Impacto do Exercício na Aprendizagem e Memória')
plt.xlabel('Percepção')
plt.ylabel('Contagem')
plt.show()
"""
