# Análise de Dados: Exercício Físico e Leitura
Este repositório contém um código Python para a análise de um conjunto de dados sobre hábitos de exercício físico e leitura. O código utiliza as bibliotecas pandas, matplotlib e seaborn para realizar a análise estatística e gerar gráficos que visualizam os dados coletados por meio de um formulário para uma pesquisa científica. Ele pode ser encontrada em https://docs.google.com/document/d/1wiS7IwYWzV7v0tJ72qkyToGMMmEh-dC5Ocpen5eUCOc/edit?usp=sharing

Estrutura dos Dados

O arquivo CSV contém as seguintes colunas:

1. Carimbo de data/hora: Timestamp de quando a resposta foi registrada.
2. Qual é a sua idade?: Faixa etária do respondente.
3. Qual seu gênero?: Gênero do respondente.
4. Qual é o seu nível educacional?: Nível educacional do respondente.
5. Qual é a sua ocupação?: Ocupação do respondente.
6. Com que frequência você pratica atividades físicas?: Frequência de prática de atividades físicas.
7. Qual é a duração média das suas sessões de exercício?: Duração média das sessões de exercício.
8. Que tipo de exercício físico você mais pratica? (marque todas as opções aplicáveis): Tipo de exercício físico praticado.
9. Com que frequência você lê livros?: Frequência de leitura de livros.
10. Você já tentou combinar a leitura com a atividade física, como ouvir audiolivros enquanto se exercita?: Se já tentou combinar leitura e exercício físico.
11. Como você avalia a sua concentração durante a leitura após uma sessão de exercício físico?: Avaliação da concentração durante a leitura após exercício físico.
12. Você acredita que o exercício físico regular impacta positivamente sua capacidade de aprendizagem e memória?: Percepção sobre o impacto do exercício na aprendizagem e memória.

## Requisitos

    Python 3.x
    pandas
    matplotlib
    seaborn

Você pode instalar as bibliotecas necessárias usando pip:
'''
bash

pip install pandas matplotlib seaborn
'''
Como Utilizar

    Coloque o arquivo CSV no mesmo diretório do script Python.
    Execute o script script_de_análise.py.

Descrição do Código

O código realiza as seguintes tarefas:

    Carregamento dos Dados:

    python

import pandas as pd

# Carrega os dados do arquivo CSV
file_path = 'Exercício Físico e a Leitura (respostas) - Respostas ao formulário 1.csv'
data = pd.read_csv(file_path)

Visualização Inicial dos Dados:

python

data.head()

Análise e Visualização Estatística:

    Geração de gráficos para distribuição de idade e gênero, nível educacional e ocupação, frequência e duração de exercícios, tipo de exercício físico praticado, frequência de leitura, combinação de leitura com atividade física, concentração após exercício físico e impacto do exercício na aprendizagem e memória.
    Utiliza seaborn e matplotlib para criar gráficos de barras.

Como Utilizar

    Coloque o arquivo CSV no mesmo diretório do script Python.
    Execute o script script_de_análise.py.
