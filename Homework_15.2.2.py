# Artur Klimov Homework 15.2.2 12/17/2022
from selenium import webdriver


driver = webdriver.Chrome()

driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

driver.maximize_window()

logo = driver.find_element("xpath", '//img[@title="Brainbucket"]')

new_registrant_btn = driver.find_element("xpath", '//a[contains(text(), "Continue")]')
new_registrant_btn.click()

# Register Account
# Personal Details
# First Name
firstname_field = driver.find_element("xpath", '//div[@class="form-group required"]')
firstname_field_class = firstname_field.get_attribute("class")
assert "required" in firstname_field_class

firstname_input = driver.find_element("xpath", '//input[@name="firstname"]')
firstname_input.clear()
firstname_input.send_keys("Artur")

# Last Name
lastname_field = driver.find_element("xpath", '//div[@class="form-group required"]')
lastname_field_class = lastname_field.get_attribute("class")
assert "required" in lastname_field_class

lastname_input = driver.find_element("xpath", '//input[@name="lastname"]')
lastname_input.send_keys("Klimov")

# Email
email = driver.find_element("xpath", '//div[@class="form-group required"]')
email_class = email.get_attribute("class")
assert "required" in email_class

email_input = driver.find_element("xpath", '//input[@name="email"]')
email_input.send_keys("klimovartur123@gmail.com")

# Telephone
telephone = driver.find_element("xpath", '//div[@class="form-group required"]')
telephone_class = telephone.get_attribute("class")
assert "required" in telephone_class

telephone_input = driver.find_element("xpath", '//input[@name="telephone"]')
telephone_input.send_keys("+12012895698")

# Address1
address1 = driver.find_element("xpath", '//div[@class="form-group required"]')
address1_class = address1.get_attribute("class")
assert "required" in address1_class

address1_input = driver.find_element("xpath", '//input[@name="address_1"]')
address1_input.send_keys("789 Monmouth St.")

# Address2
address2_input = driver.find_element("xpath", '//input[@name="address_2"]')
address2_input.send_keys("apt.4")

# City
city = driver.find_element("xpath", '//div[@class="form-group required"]')
city_class = city.get_attribute("class")
assert "required" in city_class

city_input = driver.find_element("xpath", '//input[@name="city"]')
city_input.send_keys("Jersey City")

# Postcode
postcode = driver.find_element("xpath", '//div[@class="form-group required"]')
postcode_class = postcode.get_attribute("class")
assert "required" in postcode_class

postcode_input = driver.find_element("xpath", '//input[@name="postcode"]')
postcode_input.send_keys("45689")

# Password
password = driver.find_element("xpath", '//div[@class="form-group required"]')
password_class = password.get_attribute("class")
assert "required" in password_class

password_input = driver.find_element("xpath", '//input[@name="password"]')
password_input.send_keys("Password123")

# Password Conform
passwordconfirm = driver.find_element("xpath", '//div[@class="form-group required"]')
passwordconfirm_class = passwordconfirm.get_attribute("class")
assert "required" in passwordconfirm_class

passwordconfirm_input = driver.find_element("xpath", '//input[@name="confirm"]')
passwordconfirm_input.send_keys("Password123")
