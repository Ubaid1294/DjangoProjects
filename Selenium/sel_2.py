import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.google.com")
driver.maximize_window()

input = driver.find_element(By.NAME,"q")
input.send_keys("Selenium")

button = driver.find_element(By.CLASS_NAME,"gNO89b")
button.submit()

time.sleep(20)