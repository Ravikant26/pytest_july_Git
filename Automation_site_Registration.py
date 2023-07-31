import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()


driver.get("https://automation.credence.in/register")
time.sleep(3)
driver.find_element(By.ID,"name").send_keys("Ravikant1")

driver.find_element(By.XPATH,"//input[@id='email']").send_keys("Ravikant@26.com")
time.sleep(3)

driver.find_element(By.CSS_SELECTOR,"input[name='password']").send_keys("Ravikasu@1")

driver.find_element(By.CSS_SELECTOR,"input[name='password_confirmation']").send_keys("Ravikasu@1")


driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)
try:
    driver.find_element(By.XPATH,"//h2[normalized-space()='CredKart']")
    print("Test case is passed")
except:
    print("test case is failed")


# driver.close()

