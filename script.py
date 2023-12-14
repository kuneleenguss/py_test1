from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import os

dir = os.path.dirname(__file__)

service = webdriver.ChromeService(executable_path="{}\chromedriver-win64\chromedriver.exe".format(dir))
driver = webdriver.Chrome(service=service)

driver.get(url="https://www.gismeteo.ru/")

search = driver.find_element(By.TAG_NAME, "input")
time.sleep(5.0)

search.send_keys("Уфа")
time.sleep(5.0)

search.send_keys(Keys.ENTER)
time.sleep(5.0)

footer = driver.find_element(By.TAG_NAME, "footer")

action = ActionChains(driver, duration=3000)
action.scroll_to_element(footer)
action.perform()
time.sleep(5.0)


