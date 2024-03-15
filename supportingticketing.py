from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.edge.options import Options
import time

browser = "chrome"  # chrome, firefox, edge
driver = ''

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

driver.get("https://ticketing.learnsqa.com/login")
driver.maximize_window()

time.sleep(3)
driver.find_element("id","email").send_keys("admin@admin.com")
time.sleep(3)
driver.find_element("id","password").send_keys("password")
time.sleep(3)
driver.find_element("xpath","//input[@id='remember']").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".btn").click()

act_title=driver.title
exp_title="Support Ticketing"

if act_title==exp_title:
    print('Login Test Passed')
else:
    print('Login Test Failed')

#driver.get_screenshot_as_file("Login.png")

time.sleep(5)
driver.find_element("xpath", "//a[normalize-space()='User management']").click()
time.sleep(3)
driver.find_element("xpath", "//a[normalize-space()='Permissions']").click()
time.sleep(5)
driver.find_element("xpath", "//select[@name='DataTables_Table_0_length']").click()
time.sleep(5)
driver.find_element("xpath", "//option[@value='25']").click()
time.sleep(3)
driver.find_element("xpath", "//input[@type='search']").send_keys("25")
time.sleep(5)
driver.find_element("xpath", "//a[normalize-space()='View']").click()
driver.find_element("xpath", "//a[normalize-space()='Back to list']").click()
time.sleep(5)
driver.find_element("xpath", "//td[normalize-space()='45']").click()
driver.find_element("xpath", "//tbody/tr[7]/td[4]/a[2]").click()
time.sleep(5)
driver.find_element("xpath", "//input[@id='title']").send_keys("new formula")
time.sleep(3)
driver.find_element("xpath", "//input[@value='Save']").click()

act_title=driver.title
exp_title="Support Ticketing"

if act_title==exp_title:
    print('Login Test Passed')
else:
    print('Login Test Failed')



#driver.close()


