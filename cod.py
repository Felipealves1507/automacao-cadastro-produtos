# Passo 1
import pyautogui
import time


pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("Enter") 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("Enter") 
time.sleep(3)


# Passo 2
pyautogui.click(x=838, y=372)

pyautogui.write("estagiario.ti@dfv.com")
pyautogui.press('Tab')  
pyautogui.write("1234")
pyautogui.press('Tab')
pyautogui.press('Enter')
#Passo 3 
# pip install pandas openpyxl
#pandas = é usado para trabalhar com base de dados com o python
#openpyxl = pacote que da novas funcionalidades para o pandas
import pandas
tabela = pandas.read_csv("produtos.csv")
time.sleep(1)

#Passo 4
for linha in tabela.index:
    pyautogui.click(x=940, y=257)
    
    
    #codigo
    codigo = tabela.loc[linha, "codigo"]        #Linha,coluna
    pyautogui.write(codigo)
    pyautogui.press('Tab')
    
    #marca
    marca = tabela.loc[linha, "marca"]  
    pyautogui.write(marca)
    pyautogui.press('Tab')
    
    #tipo
    tipo = tabela.loc[linha, "tipo"]  
    pyautogui.write(tipo)
    pyautogui.press('Tab')
    
    #categoria
    categoria = tabela.loc[linha, "categoria"]  
    pyautogui.write(str(categoria))
    pyautogui.press('Tab')
    
    #preco_unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]  
    pyautogui.write(str(preco_unitario))
    pyautogui.press('Tab')
    
    #custo
    custo = tabela.loc[linha, "custo"]  
    pyautogui.write(str(custo))
    pyautogui.press('Tab')
    
    #obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":                       # != significa diferente
        pyautogui.write(obs)
    pyautogui.press('Tab')

    pyautogui.press("Enter") # Apertar o botão de enviar
    pyautogui.scroll(10000) 
#Passo 5

#str = formato de texto