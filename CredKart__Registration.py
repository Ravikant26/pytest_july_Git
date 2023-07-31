import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

# 1 Open Browser
driver = webdriver.Chrome()
driver.maximize_window()
# 2 Go to Url
driver.get("https://automation.credence.in/register")
# 3 Enter Name
driver.find_element(By.ID, "name").send_keys("Credence12")
# 5 Enter Email
driver.find_element(By.ID, "email").send_keys("Credencetest69@test.com")
# 6 Enter Password
driver.find_element(By.NAME, "password").send_keys("Credence@12356")
# 7 Enter Confirm Password
driver.find_element(By.NAME, "password_confirmation").send_keys("Credence@12356")
# 8 Click Register button
driver.find_element(By.CLASS_NAME, "btn").click()
# Verify Registration status
try:
    driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
    print("Registration TestCase is Passed")
except:
    print("Registration TestCase is Failed")

time.sleep(10)
