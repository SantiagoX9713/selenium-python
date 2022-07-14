import os.path
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

class SearchTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')

        homedir = os.path.expanduser("~")
        web_driver_service = Service(f'{homedir}/testing/chromedriver')

        self.browser = webdriver.Chrome(service=web_driver_service, options=chrome_options)
        browser = self.browser
        browser.get('http://demo-store.seleniumacademy.com')
        browser.maximize_window()


    def test_search_tee(self):
        browser = self.browser
        search_field = browser.find_element(By.NAME, 'q')
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()


    def test_search_salt_shaker(self):
        browser = self.browser
        search_field = browser.find_element(By.NAME, 'q')
        search_field.clear()

        search_field.send_keys('salt shaker')
        search_field.submit()

        products = browser.find_elements(By.XPATH, '//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')
        self.assertEqual(1, len(products))

    def tearDown(self):
        self.browser.quit()

