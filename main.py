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

"""
# Gráfico de barras para a idade x gênero
# plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='Qual é a sua idade?', hue='Com que frequência você pratica atividades físicas?')
plt.title('Distribuição de Atividade Física por Idade')
plt.xlabel('Idade')
plt.ylabel('Contagem')
# plt.legend(title='Gênero')
plt.show()

# Gráfico de barras para a frequência de exercício físico
# plt.figure(figsize=(10, 6))
sns.displot(data=data, x='Com que frequência você pratica atividades físicas?', kde="true")
plt.title('Frequência de Atividade Física')
plt.xlabel('Frequência')
plt.ylabel('Contagem')
plt.show()
# Gráfico de barras para a duração das sessões de exercício
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='Qual é a duração média das suas sessões de exercício?')
plt.title('Duração Média das Sessões de Exercício')
plt.xlabel('Duração')
plt.ylabel('Contagem')
plt.show()

# Analisar e preparar os dados para o tipo de exercício
exercise_types = data['Que tipo de exercício físico você mais pratica? (marque todas as opções aplicáveis)'].str.get_dummies(', ')
exercise_types = exercise_types.drop(['basquete','etc.)'], axis=1)


# Gráfico de barras para o tipo de exercício físico
plt.figure(figsize=(12, 8))
exercise_types.sum().sort_values(ascending=False).plot(kind='bar')
plt.title('Tipos de Exercício Físico Praticado')
plt.xlabel('Tipo de Exercício')
plt.ylabel('Contagem')
plt.show()

exercise_types = exercise_types.join(data['Qual é a sua idade?'])
# Derretendo o dataframe para facilitar a plotagem com 'hue'
exercise_types_melted = exercise_types.melt(id_vars='Qual é a sua idade?', var_name='Tipo de Exercício', value_name='Pratica')

# Filtrar apenas os registros onde 'Pratica' é 1
exercise_types_melted = exercise_types_melted[exercise_types_melted['Pratica'] == 1]

# Gráfico de barras para o tipo de exercício físico com hue para idade
sns.countplot(data=exercise_types_melted, y='Qual é a sua idade?', hue="Tipo de Exercício")
plt.title('Tipos de Exercício Físico Praticado por Idade')
plt.xlabel('Contagem')
plt.ylabel('Tipo de Exercício')
plt.show()

"""
# Gráfico de barras para a frequência de leitura
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='Qual é a sua idade?', hue="Com que frequência você lê livros?")
plt.title('Frequência de Leitura de Livros')
plt.xlabel('Frequência')
plt.ylabel('Contagem')
plt.show()
"""
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
"""
# Gráfico de barras para o impacto do exercício na aprendizagem e memória
plt.figure(figsize=(10, 6))
sns.displot(data=data, x='Você acredita que o exercício físico regular impacta positivamente sua capacidade de aprendizagem e memória?', kde="true")
plt.title('Impacto do Exercício na Aprendizagem e Memória')
plt.xlabel('Percepção')
plt.ylabel('Contagem')
plt.show()

# Gráfico de barras para a concentração após exercício físico
plt.figure(figsize=(10, 6))
sns.displot(data=data, x='Você nota alguma diferença na sua capacidade de retenção de informação quando está fisicamente ativo(a) em comparação com quando não está?', kde="true")
plt.title('Retençao De Informação Após Atividade')
plt.xlabel('Nível de Concentração')
plt.ylabel('Contagem')
plt.show()
