import time
import os.path
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class HelloWorld(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        ## Setup chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless") # Ensure GUI is off
        chrome_options.add_argument("--no-sandbox")

        # Set path to chromedriver as per your configuration
        homedir = os.path.expanduser("~")
        webdriver_service = Service(f"{homedir}/testing/chromedriver")

        # Choose Chrome Browser
        cls.browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)
        cls.browser.implicitly_wait(10)

    def test_hello_world(cls):
        # Get page
        cls.browser.get("https://cloudbytes.dev")
    
    def test_hello_wikipedia(cls):
        # Get page
        cls.browser.get("https://www.wikipedia.org")

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))

# import time
# import os.path
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options

# ## Setup chrome options
# chrome_options = Options()
# chrome_options.add_argument("--headless") # Ensure GUI is off
# chrome_options.add_argument("--no-sandbox")

# # Set path to chromedriver as per your configuration
# homedir = os.path.expanduser("~")
# webdriver_service = Service(f"{homedir}/testing/chromedriver")

# # Choose Chrome Browser
# browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# # Get page
# browser.get("https://cloudbytes.dev")

# # Extract description from page and print
# description = browser.find_element(By.NAME, "description").get_attribute("content")
# print(f"{description}")

# #Wait for 10 seconds
# time.sleep(10)
# browser.quit()