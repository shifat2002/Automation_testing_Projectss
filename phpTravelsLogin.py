from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
#driver.implicitly_wait(30)
# Opening the phptravels landing page


driver.maximize_window()
driver.get("https://phptravels.net/")

time.sleep(15)
#wait = WebDriverWait(driver, 20)


#accountDropdown = wait.until(EC.presence_of_element_located((By.XPATH, "(//a[@href='javascriptvoid(0)'])[3]")))

# Locating & Clicking on the Account dropdown - Way-1
accountDropdown = driver.find_element("xpath", "(//a[@href='javascriptvoid(0)'])[3]")
#accountDropdown = driver.find_element("xpath", "//a[@href='https://phptravels.net/flights']")
accountDropdown.click()

# Locating & Clicking on the Account dropdown - Way-2
#driver.find_element("xpath", "(//a[@href='javascriptvoid(0)'])[3]").click()

# Locating & clicking on the Login link
driver.find_element("xpath", "//a[@href='https://phptravels.net/login']").click()

# locating email field
#email = driver.find_element("name", "email").send_keys("user@phptravels.com")
driver.find_element("name", "email").send_keys("user@phptravels.com")

# typing the email address
#email.send_keys("user@phptravels.com")

# locating password field & type password
driver.find_element("name", "password").send_keys("demouser")

time.sleep(10)
# Locating the login button & clicking on it
driver.find_element("id", "submitBTN").click()