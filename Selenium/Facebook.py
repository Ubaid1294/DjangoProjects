from selenium.webdriver import Keys

Mail = "******@gmail.com"
Pass = "888888888888888"
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")

emailelement = driver.find_element(By.XPATH, "//*[@id='email']")
emailelement.send_keys(Mail)

Password = driver.find_element(By.XPATH, "//*[@id='pass']")
Password.send_keys(Pass)

elem = driver.find_element(By.NAME, "login")
elem.submit()

statusElem = driver.find_element(By.XPATH, "//div[@aria-label='Post']")

time.sleep(5)

statusElem.send_keys("Hi there how are you!")

time.sleep(5)

button = driver.find_element(By.TAG_NAME, "button")

time.sleep(5)
button.submit()
for button in button:
    if button.text == "Post":
        button.click()


time.sleep(20)