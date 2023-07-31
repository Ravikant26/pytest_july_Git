import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()


driver.get("https://automation.credence.in/login")
time.sleep(3)


driver.find_element(By.XPATH,"//input[@name='email']").send_keys("Credencetest23@.com")

driver.find_element(By.CSS_SELECTOR,"input[id='password']").send_keys("Test@1234")
time.sleep(3)


# click on login button
driver.find_element(By.XPATH, "//button[@type='submit']").click()



try:
    driver.find_element(By.XPATH,"//h2[normalize-space()='CredKart']")
    print("login test is passed")
except:
    print("login test is failed")

driver.close()
