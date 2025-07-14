from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

Mail = "ubaid17cs001@gmail.com"
Pass = "Ubaid@17cs001"

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
driver.maximize_window()

# Login
driver.find_element(By.ID, "email").send_keys(Mail)
driver.find_element(By.ID, "pass").send_keys(Pass)
driver.find_element(By.NAME, "login").click()

# Wait for login to complete
time.sleep(5)

# Step 1: Click "Create a post" (use aria-label from your screenshot)
create_post = driver.find_element(By.XPATH, "//span[contains(text(),\"What's on your mind\")]")
time.sleep(5)
create_post.click()

# Wait for the post dialog to appear
time.sleep(5)

# Step 2: Type in the post content into the textbox
# textbox = driver.find_element(By.XPATH, "//span[contains(text(),\"What's on your mind\")]")
create_post.send_keys("Hi there, how are you!")

# Step 3: Wait and then click "Post" button
time.sleep(3)
post_button = driver.find_element(By.XPATH, "//div[@aria-label='Post']")
post_button.click()

print("✅ Post published!")

# Finish
time.sleep(10)
driver.quit()
