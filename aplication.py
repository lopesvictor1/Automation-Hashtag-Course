import pyautogui
import pandas as pd
import numpy as np
import time

pyautogui.PAUSE = 0.2

#read the file with all products
df = pd.read_csv("products.csv")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

#pressionar o botão do Windows
pyautogui.press("win")
#escrever chrome
pyautogui.write("chrome")
#pressionar o botão Enter
pyautogui.press("enter")

#margem de segurança para dar tempo de abrir o chrome
time.sleep(1.5)

#escrever o link e apertar o enter para entrar no site
pyautogui.write(link)
pyautogui.press("enter")

#margem de segurança para dar tempo de carregar o site
time.sleep(2.5)

#clicar no campo de email
pyautogui.click(x=763, y=369)
#escrever o email (nesse caso pode ser qualquer coisa)
pyautogui.write("estorodefacao@mail.com")
#mudar para o campo da senha
pyautogui.press("tab")
#digitar a senha (nesse caso pode ser qualquer coisa)
pyautogui.write("estoro123")
#apertar enter para ir para enviar o formulario
pyautogui.press("enter")

#margem de segurança para carregar a próxima página
time.sleep(2.5)



for line in df.index:
    
    #select the first input field
    pyautogui.click(x=787, y=254)

    
    #write the product code
    pyautogui.write(df.loc[line, "cod"])
    pyautogui.press("tab")
    
    

    #write the product brand
    pyautogui.write(df.loc[line, "brand"])
    pyautogui.press("tab")


    #write the product type
    pyautogui.write(df.loc[line, "type"])
    pyautogui.press("tab")


    #write the product category
    pyautogui.write(str(df.loc[line, "category"]))
    pyautogui.press("tab")


    #write the product un_price
    pyautogui.write(str(df.loc[line, "un_price"]))
    pyautogui.press("tab")


    #write the product cost
    pyautogui.write(str(df.loc[line, "cost"]))
    pyautogui.press("tab")

    obs = df.loc[line, "obs"]
    if not pd.isna(obs) :
        #write the product observation
        pyautogui.write(obs)
        pyautogui.press("tab")
    else:
        pyautogui.press("tab")
    #send form
    pyautogui.press("enter")
    #safety margin to ensure the new page has load
    time.sleep(0.5)
    #scroll up
    pyautogui.scroll(10000)