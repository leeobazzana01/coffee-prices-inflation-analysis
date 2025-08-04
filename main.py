import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

historico_precos_cafe=pd.read_csv('coffee_prices.csv')

#renomeando as colunas para facilitar 
historico_precos_cafe = historico_precos_cafe.rename(
    columns={
        'observation_date': 'time',
        'APU0000717311': 'price'
    }
)

#convertendo esses valores de strings para data e tipo
historico_precos_cafe['time'] = pd.to_datetime(historico_precos_cafe['time'])
#verificando os tipos
historico_precos_cafe.dtypes



#analisando o dataset
historico_precos_cafe.shape
historico_precos_cafe.columns.tolist()
historico_precos_cafe.info
historico_precos_cafe.describe


#ordenando o dataset por tempo, colocando as datas mais recentes no topo
historico_precos_cafe.sort_values(by='time', ascending=False)

#preço médio
preco_medio=historico_precos_cafe.iloc[:,1].mean()

#verificando quantiadade de valores faltantes
historico_precos_cafe['price'].isnull().sum()

#retirando os valores faltantes
novo_historico_precos_cafe=historico_precos_cafe.dropna()
novo_historico_precos_cafe.shape
novo_historico_precos_cafe = historico_precos_cafe


#plotando o gráfico

x = historico_precos_cafe['time']
y = historico_precos_cafe['price'].values

plt.figure(figsize=(12,4), dpi=300)
plt.bar(x, y, width=20)  # width em dias (para eixo datetime)

plt.xlabel("Ano")
plt.ylabel("Preço (US$/libra-peso)")
plt.title("Variação Mensal do Preço Internacional do Café")
plt.show()



#explorando o dataset da cpi
cpi = pd.read_csv('cpi_usa.csv')
print(cpi.head(10))
print(cpi.tail(10))
print(cpi.shape)

#criando um novo dadaset com os dados de cpi só a partir de 1980
cpi['observation_date'] = pd.to_datetime(cpi['observation_date']) #garantindo que a data esteja no formato correto
cpi_pos_1980 = cpi[cpi['observation_date'] >= '1980-01-01'].copy()

print(cpi_pos_1980.head())
print(cpi_pos_1980.tail())
print(cpi_pos_1980.shape)

#ordenando a cpi pos 80 em ordem crescente de tempo
cpi_pos_1980.sort_values(by='observation_date',ascending=False).head()

#plotando gráfico para identificar os padrões
plt.figure(figsize=(6,4), dpi=300)
x1=np.array(cpi_pos_1980.iloc[:,0])
y1=np.array(cpi_pos_1980.iloc[:,1])
plt.plot(x1,y1,label='CPIAUCSL', color='g')
plt.title("Índice de Preços ao Consumidor (CPI) nos EUA desde 1980")
plt.xlabel('Anos')
plt.ylabel('Índice (Base Ajustada)')
plt.show()

#explorando os dados da inflação norte americana
inf_usa = pd.read_csv('usa_inflation.csv')
inf_usa.head()
inf_usa.tail()
inf_usa.shape

#criando um dataset com a inflação só a partir de 1980
inf_usa['observation_date'] = pd.to_datetime(inf_usa['observation_date'])
inf_usa_pos_1980 = inf_usa[inf_usa['observation_date'] >= '1980-01-01'].copy()
inf_usa_pos_1980 = inf_usa_pos_1980.sort_values(by='observation_date',ascending=False)


#plotando o gráfico da inflação
plt.figure(figsize=(6,4), dpi=300)
x2=np.array(inf_usa_pos_1980.iloc[:,0])
y2=np.array(inf_usa_pos_1980.iloc[:,1])
plt.plot(x2,y2,label='price',color='r')
plt.title("Taxa de Inflação Anual nos EUA desde 1980")
plt.xlabel("Ano")
plt.ylabel("Inflação Anual (%)")
plt.show()

#comparacao cafe X cpi
fig, ax1 = plt.subplots(figsize=(10, 4), dpi=300)

# cafe
ax1.bar(historico_precos_cafe['time'], historico_precos_cafe['price'], 
        width=50, color='blue', alpha=0.7, label='Preço Café (US$/libra)')
ax1.set_ylabel("Preço do Café (US$/lb)", color='')
ax1.tick_params(axis='y', labelcolor='saddlebrown')

# cpi
ax2 = ax1.twinx()
ax2.plot(cpi_pos_1980['observation_date'], cpi_pos_1980['CPIAUCSL'], 
         color='g', linewidth=2, label='CPI EUA')
ax2.set_ylabel("CPI (Índice)", color='g')
ax2.tick_params(axis='y', labelcolor='g')

#layout
plt.title("Comparação: Preço do Café × CPI (EUA)")
fig.tight_layout()
plt.show()

#cafe x inflação
fig, ax = plt.subplots(figsize=(10, 4), dpi=300)

#cafe
ax.bar(historico_precos_cafe['time'], historico_precos_cafe['price'], 
       width=20, color='blue', alpha=0.7, label='Preço Café (US$/libra-peso)')

#inflacao
ax.plot(inf_usa_pos_1980['observation_date'], inf_usa_pos_1980.iloc[:, 1], 
        color='r', linewidth=2, label='Inflação EUA (%)')

ax.set_title("Comparação: Preço do Café × Inflação EUA")
ax.set_xlabel("Ano")
ax.set_ylabel("Valor / Índice")
ax.legend()
plt.tight_layout()
plt.show()


