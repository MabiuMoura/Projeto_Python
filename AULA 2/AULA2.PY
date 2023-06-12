#PROJETO DE ANALISE DE DADOS
#PROJETO DISPONIBILIZADO PELO INTENSIVÂO DA HASHTAG

#PASSOS
#1 PEGAR/IMPORTAR A BASE DE DADOS
import pandas as pd
tabela = pd.read_csv("clientes.csv", encoding="latin",sep=";")

tabela = tabela.drop("Unnamed: 8", axis=1)

#2 VISUALIZAR A BASE DE DADOS : 
    # entender as informações que voce tem
#print(tabela)

    # procurar os erros na base de dados
#print(tabela.info())
     
     
#3 TRATAMENTO DE DADOS
    # valores no formato errado
tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], errors="coerce")

    # valores vazios
tabela = tabela.dropna()
 
#4 ANALISE INICIAL
#print(tabela.describe()) 

#5 ANALISE PROFUNDA
import plotly.express as px

# CRIAR O GRAFICO
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x= coluna , y="Nota (1-100)", histfunc="avg", text_auto=True, nbins=10)
    grafico.show()

# EXIBIR O GRAFICO
    
# PERFIL IDEAL DE CLIENTES
# ACIMA DE 10 ANOS
# AREA DE TRABALHO : ENTRETENIMENTO E ARTISTA (EVITAR CONSTRUÇÃO)
# ENTRE 10 E 15 ANOS DE EXPERIENCIA 
# FAMILIAS DE ATE 7 MEMBROS
# 


# OBS FINAL
# SALARIO N FAZ MUITA DIFERENÇA
# CLIENTES QUE VEM DE PROMOÇÃO SAO POUCO PIORES QUE OS QUE NAO VEM