import pyautogui
import time

pyautogui.PAUSE = 0.5

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(1.5)

pyautogui.write(link)
pyautogui.press("enter")

time.sleep(2.5)

