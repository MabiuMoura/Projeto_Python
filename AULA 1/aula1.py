import pyautogui
import time
import pyperclip
import pandas as pd

pyautogui.PAUSE = 1.5

# ABRIR O NAVEGOR E BAIXAR O DOCUMENTO DE DADOS

pyautogui.press("win")
pyautogui.write("navegador opera")
pyautogui.press("enter")
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=925, y=356)
pyautogui.write("meu login")
pyautogui.click(x=914, y=423)
pyautogui.write("senha")
pyautogui.click(x=961, y=489)
pyautogui.click(x=1706, y=312)

time.sleep(4)
# IMPORTAR A BASE DE DADOS

tabela = pd.read_csv(r"Compras.csv",sep=";")

print(tabela)
total_gasto = tabela["ValorFinal"].sum()
quantidade = tabela["Quantidade"].sum()
preco_medio = total_gasto / quantidade
print(preco_medio)
print(total_gasto)
print(quantidade)
    


    #Mesma ideia de automatização de passos
    
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://outlook.live.com/mail/0/")
pyautogui.press("enter")
time.sleep(4)
pyautogui.press("n")
pyautogui.write("mabiu.moura07@aluno.ifce.edu.br")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.write("Analise da planilha")
pyautogui.press("tab")
texto = f"""
Escreva o texto,
total gasto = R${total_gasto:,.2f}
quantidade = {quantidade:,}
preço médio = R${preco_medio:,.2f}
"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("ctrl","enter")    
#time.sleep(2)
#print(pyautogui.position())