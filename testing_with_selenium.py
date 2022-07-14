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

    # Check this way to use find_element is much different to the course
    def test_search_by_id(cls):
        field = cls.browser.find_element(By.ID, 'search')        


    def test_search_by_name(cls):
        field = cls.browser.find_element(By.NAME, 'q')

    
    def test_search_by_class_name(cls):
        field = cls.browser.find_element(By.CLASS_NAME, 'input-text')


    def test_search_button_enabled(cls):
        field = cls.browser.find_element(By.CLASS_NAME, 'button')
        

    def test_search_button_enabled_xpath(cls):
        field = cls.browser.find_element(By.XPATH, "//*[@class='button search-button']")


    def test_count_of_promo_banner_images(cls):
        banner_list = cls.browser.find_element(By.CLASS_NAME, 'promos')
        banners = banner_list.find_elements(By.TAG_NAME, 'img')
        cls.assertEqual(3, len(banners))


    def test_search_xpath(cls):
        field = cls.browser.find_element(By.XPATH, '//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[2]/a/img')


    def test_search_by_class_selector(cls):
        field = cls.browser.find_element(By.CSS_SELECTOR, 'div.header-minicart span.icon')


    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()



if __name__ == "__main__":
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))
