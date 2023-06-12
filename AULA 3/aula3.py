# automação web e busca de informação com python
#PROJETO DISPONIBILIZADO PELO INTENSIVÂO DA HASHTAG

# PASSO A PASSO
# ENTRAR NO CHROME
from selenium import webdriver

navegador = webdriver.Chrome()

# IMPORTAR A BASE DE DADOS
# PARA CADA PRODUTO DA NOSSA BASE
# PEGAR O PREÇO ATUAL DA PRODUTORA
# ATUALIZAR O PREÇO NA BASE DE DADOS

import pandas as pd

tabela = pd.read_excel("commodities.xlsx")
print(tabela)

for linha in tabela.index:
    produto = tabela.loc[linha, "Produto"]
    
    link = f"https://www.melhorcambio.com/{produto}-hoje"
    link = link.replace("ó","o").replace("ã","a").replace("á","a").replace("ç","c").replace("ú","u").replace("é","e")
    navegador.get(link)
    
    cotacao = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
    cotacao = cotacao.replace(".", "").replace(",", ".")
    cotacao = float(cotacao)
    print(cotacao)
    tabela.loc[linha, "Preço Atual"] = cotacao
    print(tabela)


# DECIDIR QUAIS PRODUTOS A GENTE VAI COMPRAR

tabela["Comprar"] = tabela["Preço Ideal"] < tabela["Preço Atual"]
print(tabela)
# EXPORTAR A BASE DE DADOS ATUALIZADA
navegador.quit()

tabela.to_excel("commodities_atualizado.xlsx", index=False )



