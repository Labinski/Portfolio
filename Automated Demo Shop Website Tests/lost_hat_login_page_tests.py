import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from helpers import functional_helpers as fh

s = Service("C:\\Users\\User\\Desktop\\Selenium Chromedriver\\chromedriver.exe")


class LostHatLoginPageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=s)
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_url = 'https://autodemo.testoneo.com/en/' + 'login'

    def tearDown(self):
        self.driver.quit()

    def test_log_in_header(self):
        expected_text = 'Log in to your account'
        header_element_xpath = '//header[@class="page-header"]'
        driver = self.driver

        driver.get(self.base_url)
        sign_in = self.driver.find_element(By.XPATH, '//*[@id="_desktop_user_info"]//span')
        sign_in.click()

        self.assert_element_text(driver, header_element_xpath, expected_text)

    def test_correct_log_in(self):
        expected_text = 'Adam Sandler'
        customer_account_button_xpath = '//a[@class="account"]/*[@class="hidden-sm-down"]'
        user_email = '123@123.com'
        user_pass = '1234567890'
        driver = self.driver

        driver.get(self.login_url)
        fh.user_login(driver, user_email, user_pass)
        self.assert_element_text(driver, customer_account_button_xpath, expected_text)

    def test_incorrect_log_in(self):
        expected_text = 'Authentication failed.'
        alert_xpath = '//*[@id="content"]//*[@class="alert alert-danger"]'
        user_email = '123@1.com'
        user_pass = '12343560'
        driver = self.driver

        driver.get(self.login_url)
        fh.user_login(driver, user_email, user_pass)
        self.assert_element_text(driver, alert_xpath, expected_text)

    def assert_element_text(self, driver, xpath, expected_text):
        element = driver.find_element(by=By.XPATH, value=xpath)
        element_text = element.text
        self.assertEqual(expected_text, element_text,
                         f'Expected text differ from actual on page url: {driver.current_url}')