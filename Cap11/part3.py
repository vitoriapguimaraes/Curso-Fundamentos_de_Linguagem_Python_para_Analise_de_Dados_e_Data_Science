# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 11

### Análise e Ciência de Dados via programação Python através de duas poderosas bibliotecas: Matplotlib e Seaborn ###

### Usando Matplotlib, Seaborn, NumPy e Pandas na Criação de Gráfico Estatístico ###

# Imports
import numpy as np
import pandas as pd
import matplotlib as mat
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import seaborn as sea


# Valores randômicos
np.random.seed(42)
n = 1000
pct_smokers = 0.2

# Variáveis
flag_fumante = np.random.rand(n) < pct_smokers
idade = np.random.normal(40, 10, n)
altura = np.random.normal(170, 10, n)
peso = np.random.normal(70, 10, n)

# Dataframe
dados = pd.DataFrame({'altura': altura, 'peso': peso, 'flag_fumante': flag_fumante})

# Cria os dados para a variável flag_fumante
dados['flag_fumante'] = dados['flag_fumante'].map({True: 'Fumante', False: 'Não Fumante'})

print(dados.shape)
print(dados.head())


# Style
sea.set(style = "ticks")

# lmplot
sea.lmplot(x = 'altura', 
           y = 'peso', 
           data = dados, 
           hue = 'flag_fumante', 
           palette = ['tab:blue', 'tab:orange'], 
           height = 7)

# Labels e título
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.title('Relação Entre Altura e Peso de Fumantes e Não Fumantes')

# Remove as bordas
sea.despine()

# Show
plt.show()



### Links úteis

# Lista de cores no Matplotlib
# https://matplotlib.org/stable/gallery/color/named_colors.html

# Seaborn Gallery
# https://seaborn.pydata.org/examples/index.htmlData
