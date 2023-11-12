# ols-regression-model
Repositório que guarda dados e códigos do modelo OLS de regressão econométrica para dados históricos do preço do Bitcoin

# informações
Os arquivos em Python desse repositório são:
1. ols_regression.py: responsável por executar a regressão OLS em cima da base de dados fornecida
2. run_granger_test_h-p.py: responsável por executar o teste de Granger em cima da hipótese "hash rate causa o preço"
3. run_granger_test_p-h.py: responsável por executar o teste de Granger inverso, em cima da hipótese: "preço causa hash rate"

Todos os arquivos analisam os dados da mesa base, também fornecida neste repositório: bitcoin15-17.xlsx
A  base em questão foi extraída de https://www.blockchain.com/explorer/charts

# como rodar o modelo
1. Baixe todos os arquivos do repositório e, para facilitar, salve-os em uma única pasta;
2. Instale o python instalado em seu computador. Para isso, acesse o site https://www.python.org/downloads/ e faça o download do arquivo de instalação do Python compatível com seu sistema operacional;
3. Instale o pip, que será responsável por gerenciar os pacotes necessários do python, seguindo esse passo a passo: https://www.dacsolution.com.br/central/index.php?rp=/knowledgebase/58/Como-Instalar-O-PIP-Para-Gerenciar-Pacotes-Python-No-Windows.html
4. Com o python e pip instalados, o primeiro passo é acessar o prompt de comando do seu computador. Para acessá-lo, abra o prompt do seu computador, digitando "cmd" no menu inicial de busca do Windows ou então aperte as teclas Windows + R.
5. Após instalar o pip, é possível instalar os pacotes e extensões necessárias para rodar o código. Basta digitar esses comandos no prompt, sequencialmente:
   python3 -m pip install pandas
   python3 -m pip install pnumpy
   python3 -m pip install statsmodels
   python3 -m pip install matplotlib
   python3 -m pip install statsmodels
   Obs: dependendo da versão do python, você deverá usar o comando python ao invés de python3 ou até mesmo somente o py.
6. Agora, como todos os pacotes instalados, para rodar o código é necessário você abrir o prompt, ir até a pasta onde os arquivos desse repositório estão instalados, e digitar python3 "nome_do_arquivo.py". Caso possua dificuldades para encontrar a pasta através do prompt, esse tutorial pode ajudar: https://www.softdownload.com.br/como-abrir-prompt-comando-windows-pasta-especifica.html
7. O resultado esperado, ao rodar o código, é que sejam retornados os resultados da regressão no próprio prompt e também o gráfico.

# créditos
Todas as informações aqui dispostas são de total responsabilidade do autor. Qualquer dúvida, sugestão ou problema, contacte yago.dotti@outlook.com   
