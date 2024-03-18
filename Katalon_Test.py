# Selenium Task:
# Step-1: Go to URL(https://katalon-test.s3.amazonaws.com/aut/html/form.html)
# Step-2: Enter the first name
# Step-3: Enter the last name
# Step-4: Select the Gender (radio button)
# Step-5: Select the date of birth (calendar)
# Step-6: Enter your address
# Step-7: Enter your email
# Step-8: Enter the password
# Step-9: Enter your company name
# Step-10: Select your role in the company from dropdown
# Step-11: Select the job expectation from selectbox
# Step-12: Select the ways of development from checkbox (multiple can be checked)
# Step-13: Enter the comment
# Step-14: Click on the Submit button

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

browser = "chrome"  # chrome, firefox, edge
driver = ''
Gender = "Male" # Male, Female, In Between
if browser == "chrome":
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
elif browser == "firefox":
    driver = webdriver.Firefox()
elif browser == "edge":
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Edge(options=options)
else:
    driver = webdriver.Chrome()

driver.get("https://katalon-test.s3.amazonaws.com/aut/html/form.html")
driver.maximize_window()

time.sleep(5)
driver.find_element("xpath", "//input[@id='first-name']").send_keys("Bob")
time.sleep(3)
driver.find_element("xpath", "//input[@id='last-name']").send_keys("Dylan")
time.sleep(3)
driver.find_element("xpath", "(//input[@name='gender'])[1]").click()


# Scrolling down the window
time.sleep(3)
driver.execute_script("window.scrollTo(0, window.scrollY + 100)")

time.sleep(3)
driver.find_element("xpath", "(//input[@id='dob'])[1]").click()
time.sleep(3)
driver.find_element("xpath", "(//td[normalize-space()='20'])[1]").click()
driver.find_element("xpath", "//form[@id='infoForm']").click()
time.sleep(3)
driver.find_element("xpath", "//input[@id='address']").send_keys("123/A, Green Street")

time.sleep(3)
driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

time.sleep(3)
driver.find_element("xpath", "//input[@id='email']").send_keys("Bobdylan@example.com")
time.sleep(3)
driver.find_element("xpath", "//input[@id='password']").send_keys("bobdyan123")

time.sleep(3)
driver.execute_script("window.scrollTo(0, window.scrollY + 300)")

time.sleep(3)
driver.find_element("xpath", "//input[@id='company']").send_keys("X-Corporation")
time.sleep(3)
driver.find_element("xpath", "//select[@id='role']").click()

time.sleep(3)
driver.find_element("xpath", "//option[@value='QA']").click()
driver.find_element("xpath", "//form[@id='infoForm']").click()
time.sleep(3)
driver.find_element("xpath", "//option[@value='Excellent colleagues']").click()
time.sleep(3)
driver.find_element("xpath", "//label[normalize-space()='Read tech blogs']").click()

time.sleep(3)
driver.execute_script("window.scrollTo(0, window.scrollY + 400)")

time.sleep(3)
driver.find_element("xpath", "//textarea[@id='comment']").send_keys("Open to work worldwide.")
time.sleep(3)
driver.find_element("xpath", "//button[@id='submit']").click()

time.sleep(3)
actual_title = driver.title
expected_title = "Demo AUT"
if actual_title == expected_title:
    print('Test Successful')
else:
    print('Test Failed')

driver.close()