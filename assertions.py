import os.path
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

class AssertionsTest(unittest.TestCase):
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


    def test_search_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))


    def test_search_lang_switch(self):
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))


    def tearDown(self):
        self.browser.quit()

    # Esta función nos hará más fácil buscar elementos y regresar booleanos para hacer más corto el assertion
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(by=how, value=what)
        except NoSuchElementException as variable:
            return False
        return True