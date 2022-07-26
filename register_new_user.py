import os.path
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class RegisterNewUser(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        ## Setup chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless") # Ensure GUI is off
        chrome_options.add_argument("--no-sandbox") # Ensure GUI is off

        # Set path to chromedriver as per your configuration
        homedir = os.path.expanduser("~")
        webdriver_service = Service(f"{homedir}/testing/chromedriver")

        # Choose Chrome Browser
        cls.browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)
        browser = cls.browser
        browser.get('http://demo-store.seleniumacademy.com')
        browser.maximize_window()
        # Get page


    def test_register_new_user(self):
        browser = self.browser
        browser.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        browser.find_element(By.LINK_TEXT, 'Log In').click()

        create_account_button = browser.find_element(By.XPATH, '//*[@id="login-form"]/div/div[1]/div[2]/a')
        self.assertTrue(create_account_button.is_displayed and create_account_button.is_enabled())
        create_account_button.click()
        self.assertTrue(browser.title, 'Create New Customer Account')

        first_name = browser.find_element(By.ID, 'firstname')
        middle_name = browser.find_element(By.ID, 'middlename')
        last_name = browser.find_element(By.ID, 'lastname')
        email_address = browser.find_element(By.ID, 'email_address')
        news_letter_subscription = browser.find_element(By.ID, 'is_subscribed')
        password = browser.find_element(By.ID, 'password')
        confirm_password = browser.find_element(By.ID, 'confirmation')
        submit_button = browser.find_element(By.XPATH, '//*[@id="form-validate"]/div[2]/button')


    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()



if __name__ == "__main__":
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))
