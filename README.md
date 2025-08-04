# Análise de Preços do Café e Indicadores Econômicos (EUA)
Este projeto realiza a análise exploratória do histórico de preços do café, comparando com o Índice de Preços ao Consumidor (CPI) e a inflação dos EUA a partir de 1980.

## Pré-requisitos
Antes de executar o projeto, é necessário ter instalado:

Python 3.8+

pip (gerenciador de pacotes do Python)

## Configuração do Ambiente Virtual
Criar o ambiente virtual

#### python -m venv venv

### Ativar o ambiente virtual

Windows

#### venv\Scripts\activate

Linux/Mac

#### source venv/bin/activate

### Instalar as dependências


#### pip install pandas numpy matplotlib
▶Como executar
Coloque os arquivos CSV (coffee_prices.csv, cpi_usa.csv, usa_inflation.csv) na pasta do projeto.

Execute o script Python:

#### python3.12 seu_arquivo.py
O script irá gerar gráficos comparando:

Preço do café × CPI

Preço do café × Inflação

