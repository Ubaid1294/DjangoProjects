from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.amazon.in")
driver.maximize_window()

button = driver.find_element(By.CLASS_NAME,"a-button-text")
button.click()

search = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
search.send_keys("iphones")

driver.find_element(By.ID,"nav-search-submit-button").submit()

list =  driver.find_elements(By.XPATH, "//span[contains(translate(text(),'IPHONE','iphone'),'iphone')]")

print(f"{len(list)} Products Found:\n")

Count = 1
for item in list:
    text = item.text.strip()
    if text:
        print(f"{Count}. {text}")
        Count += 1
time.sleep(20)
driver.quit()