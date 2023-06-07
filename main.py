import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

ser = Service("C:\Program Files (x86)\chromedriver.exe")
op = webdriver.ChromeOptions()
op.add_experimental_option("detach", True)
driver=webdriver.Chrome(service=ser, options=op)
driver.maximize_window()

#                   Digitar no campo de pesquisa
driver.get("https://google.com")
search_field = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
search_field.send_keys("Ja Morant")
search_field.send_keys(Keys.ENTER)
time.sleep(10)
print(search_field)


#          Recuperar dados da busca
about = driver.find_element(by=By.XPATH, value="/html/body/div[6]/div/div[11]/div[4]/div[4]/div/div/div[2]/div/div/div/div[2]/div/div/div/span[2]")
about_text = about.get_attribute("innerHTML")

print(about_text)
