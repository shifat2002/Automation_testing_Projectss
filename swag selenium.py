# Selenium Python Task:
# 1. Go to URL: https://www.saucedemo.com/
# 2. Log in with standard_user
# 3. Verify login is successful
# 4. Add a product to the cart
# 5. Go to cart and checkout
# 6. Enter name & postal code
# 7. Finish the purchase
# 8. Verify that the purchase is successful
# 8. Go back to homepage
# 9. Log out
# 10. Verify user is logged out successfully

from selenium import webdriver

driver = webdriver.Firefox()

driver.maximize_window()
driver.get("https://www.saucedemo.com/")


driver.find_element("xpath", "//input[@id='user-name']").send_keys("standard_user")
driver.find_element("xpath", "//input[@id='password']").send_keys("secret_sauce")
driver.find_element("id", "login-button").click()

act_title = driver.title
exp_title = 'Swag Labs'

if act_title == exp_title:
    print('Login Test Passed')
else:
    print('Login Test Failed')

driver.find_element("id", "add-to-cart-sauce-labs-bike-light").click()
driver.find_element("xpath", "//a[@class='shopping_cart_link']").click()
driver.find_element("id", "checkout").click()
driver.find_element("xpath", "//input[@id='first-name']").send_keys("shifat")
driver.find_element("xpath", "//input[@id='last-name']").send_keys("mahmud")
driver.find_element("xpath", "//input[@id='postal-code']").send_keys("3450")
driver.find_element("xpath", "//input[@id='continue']").click()
driver.find_element("xpath", "//button[@id='finish']").click()

act_title = driver.title
exp_title = 'Swag Labs'

if act_title == exp_title:
    print('purchase is successful')
else:
    print('purchase is fail')

driver.find_element("xpath", "//button[@id='back-to-products']").click()
driver.find_element("id", "react-burger-menu-btn").click()
driver.find_element("id", "logout_sidebar_link").click()

act_title = driver.title
exp_title = 'Swag Labs'

if act_title == exp_title:
    print('Successfully log out')
else:
    print('log out is fail')

driver.close()
