import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import grangercausalitytests
import matplotlib.pyplot as plt

# Carregar os dados do arquivo XLSX
dados = pd.read_excel('bitcoin15-17.xlsx')

# Selecionar as variáveis a serem testadas
data = dados[['giga-hashrate', 'marketprice']].dropna()

# Executar o teste de Granger
max_lag = 3  # Número máximo de defasagens a serem consideradas
results = grangercausalitytests(data, max_lag, verbose=False)

# Exibir os resultados do teste de Granger como uma tabela
for lag in results.keys():
    print(f"Lag {lag}:")
    print("------")
    for key, value in results[lag][0].items():
        print(f"{key}: {value}")
    print("\n")

# Plotar os resultados do teste de Granger
lags = range(1, max_lag+1)
p_values = [results[lag][0]['ssr_chi2test'][1] for lag in lags]

plt.bar(lags, p_values)
plt.xlabel('Defasagem (lag)')
plt.ylabel('Valor-p')
plt.title('Teste de Granger: hashrate -> marketprice')
plt.xticks(lags)
plt.show()
