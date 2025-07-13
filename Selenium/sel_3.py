from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in")

button = driver.find_element(By.CLASS_NAME,"a-button-text")
button.click()

select = driver.find_element(By.LINK_TEXT,"Electronics")
select.click()

select_1 = driver.find_element(By.LINK_TEXT,"Cameras")
select_1.click()

time.sleep(20)