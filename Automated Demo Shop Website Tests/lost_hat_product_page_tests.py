import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


s = Service("C:\\Users\\User\\Desktop\\Selenium Chromedriver\\chromedriver.exe")


class LostHatProductPageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=s)
        self.product_url = 'https://autodemo.testoneo.com/en/' + 'men/1-1-hummingbird-printed-t-shirt.html'

    def tearDown(self):
        self.driver.quit()

    def test_check_product_name(self):
        expected_text = 'HUMMINGBIRD PRINTED T-SHIRT'
        tshirt_xpath = '//*[@class="col-md-6"]//*[@itemprop="name"]'
        driver = self.driver

        driver.get(self.product_url)
        self.assert_element_text(driver, tshirt_xpath, expected_text)

    def test_check_product_price(self):
        expected_text = 'PLN23.52'
        tshirt_xpath = '//*[@id="main"]//*[@content="23.52"]'
        driver = self.driver

        driver.get(self.product_url)
        self.assert_element_text(driver, tshirt_xpath, expected_text)

    def assert_element_text(self, driver, xpath, expected_text):
        element = driver.find_element(by=By.XPATH, value=xpath)
        element_text = element.text
        self.assertEqual(expected_text, element_text,
                         f'Expected text differ from actual on page url: {driver.current_url}')