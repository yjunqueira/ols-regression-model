# ols-regression-model
Repositório que guarda dados e códigos do modelo OLS de regressão econométrica para dados históricos do preço do Bitcoin

# informações
Os arquivos em Python desse repositório são:
1. ols_regression.py: responsável por executar a regressão OLS em cima da base de dados fornecida
2. run_granger_test_h-p.py: responsável por executar o teste de Granger em cima da hipótese "hash rate causa o preço"
3. run_granger_test_p-h.py: responsável por executar o teste de Granger inverso, em cima da hipótese: "preço causa hash rate"

Todos os arquivos analisam os dados da mesa base, também fornecida neste repositório: bitcoin15-17.xlsx

A  base em questão foi extraída de https://www.blockchain.com/explorer/charts
