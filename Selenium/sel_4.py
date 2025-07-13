from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.amazon.in")
driver.maximize_window()

button = driver.find_element(By.CLASS_NAME,"a-button-text")
button.click()

time.sleep(3)

driver.refresh()

time.sleep(10)
