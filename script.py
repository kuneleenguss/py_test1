from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

service = webdriver.ChromeService(executable_path="D:\VSC Projects\py_test1\chromedriver-win64\chromedriver.exe")

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


