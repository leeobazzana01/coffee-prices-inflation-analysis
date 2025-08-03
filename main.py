import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

historico_precos_cafe=pd.read_csv('coffee-prices-historical-data.csv')

df_raw = pd.read_csv('coffee-prices-historical-data.csv', dtype=str)

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
print(historico_precos_cafe.dtypes)



#analisando o dataset
historico_precos_cafe.shape
historico_precos_cafe.columns.tolist()
historico_precos_cafe.info
historico_precos_cafe.describe


#ordenando o dataset por tempo, colocando as datas mais recentes no topo
historico_precos_cafe.sort_values(by='time', ascending=False)

#preço médio
preco_medio=historico_precos_cafe.iloc[:,1].mean()
print("Valor Médio: ", preco_medio)

#verificando quantiadade de valores faltantes
print(historico_precos_cafe['price'].isnull().sum())

#retirando os valores faltantes
novo_historico_precos_cafe=historico_precos_cafe.dropna()
novo_historico_precos_cafe.shape
novo_historico_precos_cafe = historico_precos_cafe


#plotando o gráfico
#anos = historico_precos_cafe['time'].dt.year

'''x = historico_precos_cafe['time']
y = historico_precos_cafe['price'].values

plt.figure(figsize=(12,4), dpi=300)
plt.bar(x, y, width=20)  # width em dias (para eixo datetime)

plt.xlabel("Ano")
plt.ylabel("Preço (Dólares/Libra)")
plt.title("Histórico de Preços do Café")
plt.show()'''



#explorando o dataset da cpi
cpi = pd.read_csv('cpi_in_usa.csv')
print(cpi.head(10))
print(cpi.tail(10))
print(cpi.shape)

#criando um novo dadaset com os dados de cpi só a partir de 1980
