from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os, json
import threading, platform


with open('config.json') as config_file:
    CONFIG = json.load(config_file)

TASK_ID = int(os.environ['TASK_ID']) if 'TASK_ID' in os.environ else 0

# Take user credentials from environment variables if they are defined
if 'BROWSERSTACK_USERNAME' in os.environ: CONFIG['capabilities']['browserstack.user'] = os.environ['BROWSERSTACK_USERNAME'] 
if 'BROWSERSTACK_ACCESS_KEY' in os.environ: CONFIG['capabilities']['browserstack.key'] = os.environ['BROWSERSTACK_ACCESS_KEY']

# Initialize the remote Webdriver using BrowserStack remote URL
# and desired capabilities defined above
desired_capabilities = CONFIG['capabilities']
#check how many devices
number_devices=len(CONFIG['environments'])


def login_steps():
    driver = webdriver.Remote(
     desired_capabilities=dict(desired_capabilities),
        command_executor="http://hub-cloud.browserstack.com/wd/hub"
    )
    #click on Login button
    login_button = WebDriverWait(driver, 30).until(
        EC._element_if_visible((MobileBy., "my.com.tngdigital.ewallet.sit:id/ftv_bottom_click_text"))
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
    
jobs = []
for index in range(number_devices):
    desired_capabilities['device'] = CONFIG['environments'][index]['device']
    thread = threading.Thread(target=login_steps(),args=(index,))
    thread.start()
    jobs.append(thread)
    
    
    print(desired_capabilities['device'])

for thread in jobs:
    thread.join()

