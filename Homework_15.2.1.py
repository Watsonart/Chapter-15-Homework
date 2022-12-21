# Artur Klimov Homework 15.2.1 12/17/2022
from selenium import webdriver


driver = webdriver.Chrome()

driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

driver.maximize_window()

email = driver.find_element("xpath", '//input[@name="email"]')
email.send_keys("klimovartur123@gmail.com")

password = driver.find_element("xpath", '//input[@name="password"]')
password.send_keys("Password123")

loginbtn = driver.find_element("xpath", '//input[@type="submit"]')
loginbtn.click()