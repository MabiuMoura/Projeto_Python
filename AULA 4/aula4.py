#PROJETO DISPONIBILIZADO PELO INTENSIVÂO DA HASHTAG
#machine learn
from sklearn.metrics import r2_score
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor


tabela = pd.read_csv("barcos_ref.csv")
print(tabela)
print(tabela.info())


print(tabela.corr()["Preco"])
sns.heatmap(tabela.corr()[["Preco"]], cmap="Blues", annot=True)

plt.show()


y = tabela["Preco"]
x = tabela.drop("Preco", axis= 1)


x_treino, x_teste, y_treino, y_teste = train_test_split(x, y)
modelo_regressaoLinear = LinearRegression()
modelo_arvoredecisao = RandomForestRegressor()

modelo_regressaoLinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)


previsao_regressaolinear = modelo_regressaoLinear.predict(x_teste)
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)

from sklearn.metrics import r2_score
print(r2_score(y_teste, previsao_regressaolinear))
print(r2_score(y_teste, previsao_arvoredecisao))



tabela_aux = pd.DataFrame()
tabela_aux['y_teste'] = y_teste
tabela_aux["Previsoes Arvore Decisao"] = previsao_arvoredecisao
tabela_aux["Previsoes Regressao Linear"] = previsao_regressaolinear

sns.lineplot(data= tabela_aux)
plt.show()




