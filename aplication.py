import pyautogui
import time

pyautogui.PAUSE = 0.5

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
pyautogui.write("teste@gmail.com")
#mudar para o campo da senha
pyautogui.press("tab")
#digitar a senha (nesse caso pode ser qualquer coisa)
pyautogui.write("test123")
#apertar enter para ir para enviar o formulario
pyautogui.press("enter")

#margem de segurança para carregar a próxima página
time.sleep(2.5)