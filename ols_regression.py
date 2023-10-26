import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import grangercausalitytests

dados = pd.read_excel('bitcoin15-17.xlsx')

dados['log_hashrate'] = np.log(dados['giga-hashrate'])
dados['log_market-price'] = np.log(dados['marketprice'])
dados['log_coins-per-minute'] = np.log(dados['coins_per_minute'])

X = dados[['log_hashrate', 'log_coins-per-minute']]
y = dados['log_market-price']

X = sm.add_constant(X)

# Criar o modelo de regressão
modelo = sm.OLS(y, X)

# Ajustar o modelo aos dados
resultado = modelo.fit()

# Imprimir os resultados da regressão
print(resultado.summary())

# Plotar o gráfico de dispersão
plt.scatter(dados['log_hashrate'], dados['log_market-price'], label='Log Market Price')
plt.scatter(dados['log_hashrate'], dados['log_coins-per-minute'], label='Log Coins per Minute')
plt.xlabel('Log Hashrate')
plt.ylabel('Log Value')
plt.title('Relação entre Log Hashrate, Log Market Price e Log Coins per Minute')
plt.legend()

# Plotar a linha de regressão
plt.plot(dados['log_hashrate'], resultado.fittedvalues, color='red', linewidth=2)
plt.show()