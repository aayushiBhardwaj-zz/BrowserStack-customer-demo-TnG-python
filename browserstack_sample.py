from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

desired_cap = {
    # Set your access credentials

    "browserstack.user" : "aayushib_T4hCqr",
    "browserstack.key" : "GFwMmRcqbvz2bxzVBAzW",

    # Set URL of the application under test
    "app" : "bs://d80b9da704ef6d9e78bd9b0c15fb6ed7b874c27f",

    # Specify device and os_version for testing
    "device" : "Samsung Galaxy S21 Ultra",
    "os_version" : "11.0",
    
    # Set other BrowserStack capabilities
    "project" : "First Python project", 
    "build" : "Python Android - Custom APP",
    "name" : "first_test"
}

# Initialize the remote Webdriver using BrowserStack remote URL
# and desired capabilities defined above
driver = webdriver.Remote(
    command_executor="http://hub-cloud.browserstack.com/wd/hub", 
    desired_capabilities=desired_cap
)

# Test case for the BrowserStack sample Android app. 
# If you have uploaded your app, update the test case here. 

#click on Login button
login_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ID, "my.com.tngdigital.ewallet.sit:id/ftv_bottom_click_text"))
)
print("login button")
login_button.click()

mobile_number = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ID, "my.com.tngdigital.ewallet.sit:id/et_center"))
)

mobile_number.send_keys("198908541")
time.sleep(5)


# Invoke driver.quit() after the test is done to indicate that the test is completed.
driver.quit()
