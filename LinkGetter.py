import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.common.keys import Keys

print(time.asctime())

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--headless")
driver = webdriver.Chrome()
driver.get("https://linktr.ee/Hacettepe_Kariyer_Gunleri_B5")
wait_a_minute = WebDriverWait(driver, 600)
driver.maximize_window()
time.sleep(3)
#time.sleep(600)
#a = driver.find_elements_by_xpath('.//a')[0]

file = open("links-kariyerb.txt","w",encoding='utf-8')
for a in driver.find_elements_by_xpath('.//a'):
    value = a.get_attribute('href')
    file.write(value+"\n")
file.close()
driver.close()
