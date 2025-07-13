import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.google.com")
driver.maximize_window()

input = driver.find_element(By.NAME,"q")
input.send_keys("Selenium")

button = driver.find_element(By.NAME,"btnK")
button.submit()

time.sleep(10)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)

driver.quit()