#PROJETO DISPONIBILIZADO PELO INTENSIVÂO DA HASHTAG
#machine learn

# PASSO A PASSO
# 1: entender o desafio

# 2: entendimento da area/empresa

# 3: extração/obtenção dos dados
import pandas as pd

tabela = pd.read_csv("barcos_ref.csv")
#print(tabela)
# 4: ajuste de dados (tratamento/limpeza)
#print(tabela.info())

# 5: analise exploratoria
import seaborn as sns
import matplotlib.pyplot as plt

print(tabela.corr()["Preco"])
#criar o grafico
sns.heatmap(tabela.corr()[["Preco"]], cmap="Blues", annot=True)

#exibir o grafico
plt.show()


# 6: modelagem + algoritmo (IA /se necessario)
y = tabela["Preco"]
x = tabela.drop("Preco", axis= 1)

from sklearn.model_selection import train_test_split
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y)


from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor


modelo_regressaoLinear = LinearRegression()
modelo_arvoredecisao = RandomForestRegressor()


modelo_regressaoLinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)


previsao_regressaolinear = modelo_regressaoLinear.predict(x_teste)
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)

from sklearn.metrics import r2_score
print(r2_score(y_teste, previsao_regressaolinear))
print(r2_score(y_teste, previsao_arvoredecisao))


# 7: interpretação dos resultados

tabela_aux = pd.DataFrame()
tabela_aux['y_teste'] = y_teste
tabela_aux["Previsoes Arvore Decisao"] = previsao_arvoredecisao
tabela_aux["Previsoes Regressao Linear"] = previsao_regressaolinear

sns.lineplot(data= tabela_aux)
plt.show()




