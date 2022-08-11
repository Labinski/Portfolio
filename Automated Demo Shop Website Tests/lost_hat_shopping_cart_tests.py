import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from helpers import operational_helpers as oh

s = Service("C:\\Users\\User\\Desktop\\Selenium Chromedriver\\chromedriver.exe")


class LostHatShoppingCartTests(unittest.TestCase):

    def setUp(self):
        self.product_mountain_fox_url = 'https://autodemo.testoneo.com/en/art/12-mountain-fox-vector-graphics.html'
        self.driver = webdriver.Chrome(service=s)

    def tearDown(self):
        self.driver.quit()

    def test_adding_item_to_shopping_cart(self):
        driver = self.driver
        expected_confirmation_text = 'Product successfully added to your shopping cart'
        confirmation_modal_title_xpath = '//*[@id="myModalLabel"]'
        add_to_cart_button_xpath = '//*[@class="btn btn-primary add-to-cart"]'

        driver.get(self.product_mountain_fox_url)
        add_to_cart_button = driver.find_element(By.XPATH, add_to_cart_button_xpath)
        add_to_cart_button.click()

        # Using my custom wait loop
        # confirmation_modal_elements = oh.wait_for_elements(driver, confirmation_modal_title_xpath)
        # confirmation_modal_element = confirmation_modal_elements[0]

        confirmation_modal_element = oh.visibility_of_element_wait(driver, confirmation_modal_title_xpath)
        self.assertIn(expected_confirmation_text, confirmation_modal_element.text)
