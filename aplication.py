import pyautogui
import pandas as pd
import numpy as np
import time

pyautogui.PAUSE = 0.2

#read the file with all products
df = pd.read_csv("products.csv")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

#press Windows Button
pyautogui.press("win")
#eSearch for Chrome
pyautogui.write("chrome")
#press Enter
pyautogui.press("enter")

#safety margin to ensure that Chrome has load
time.sleep(1.5)

#Write link and then press enter
pyautogui.write(link)
pyautogui.press("enter")

#safety margin to ensure the new page has load
time.sleep(2.5)

#click the first input field
pyautogui.click(x=763, y=369)
#write the email (can be anything in this site)
pyautogui.write("estorodefacao@mail.com")
#select next field
pyautogui.press("tab")
#write the password (can be anything in this site)
pyautogui.write("estoro123")
#press enter to send the form
pyautogui.press("enter")

#safety margin to ensure that Chrome has load
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


    #check if the current line has anything written in the Obs field
    obs = df.loc[line, "obs"]
    if not pd.isna(obs):
        #write the product observation
        pyautogui.write(obs)
    
    pyautogui.press("tab")

        
    #send form
    pyautogui.press("enter")
    #safety margin to ensure the new page has load
    time.sleep(0.5)
    #scroll up
    pyautogui.scroll(10000)