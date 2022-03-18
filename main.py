import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.common.keys import Keys
from datetime import datetime

with open("links.txt","r",encoding="utf-8") as file:
    lines = [i for i in file.readlines()]

print(time.asctime())

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--headless")

for i in lines:
    print(time.asctime())
    driver = webdriver.Chrome()
    driver.get(i)
    wait_a_minute = WebDriverWait(driver, 600)
    driver.maximize_window()
    time.sleep(3)
    button = pyautogui.locateCenterOnScreen('bbb.png')
    print(button)
    if button == None:
        print("fgmpdfgm")
        button = 1390,229
    pyautogui.moveTo(button)
    # 1026,223
    time.sleep(1)
    print(pyautogui.position())
    pyautogui.click()
    pyautogui.click()
    time.sleep(2)
    leave_button = pyautogui.locateCenterOnScreen('leaveAndJoin.png')
    if not leave_button == None:
        pyautogui.moveTo(leave_button)
        pyautogui.click()
    driver.close()
    time.sleep(10)
    #  pyautogui.press(['win','up'])

    pyautogui.press('alt')
    print("girdi")
    chat = pyautogui.locateCenterOnScreen('chat.png')
    while chat == None:
        pyautogui.press('alt')
        print("girdi")
        chat = pyautogui.locateCenterOnScreen('chat.png')
    print("çıktı")
    print(chat)
    pyautogui.moveTo(chat)


    """pyautogui.click()
    chatBox = pyautogui.locateCenterOnScreen('chatBox.png')
    pyautogui.moveTo(chatBox)
    pyautogui.click()
    pyautogui.write("21992871 Utku Bora")
    pyautogui.press('enter')"""

    time.sleep(3000)
