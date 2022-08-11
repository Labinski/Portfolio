import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


s = Service("C:\\Users\\User\\Desktop\\Selenium Chromedriver\\chromedriver.exe")


class LostHatSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(service=s)
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.art_url = 'https://autodemo.testoneo.com/en/9-art'
        self.clothes_url = 'https://autodemo.testoneo.com/en/3-clothes'
        self.accessories_url = 'https://autodemo.testoneo.com/en/6-accessories'
        self.login_url = 'https://autodemo.testoneo.com/en/login?back=my-account'

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_main_page(self):
        page_title = 'Lost Hat'
        self.assert_title(self.base_url, page_title)

    def test_art_page(self):
        page_title = 'Art'
        self.assert_title(self.art_url, page_title)

    def test_clothes_page(self):
        page_title = 'Clothes'
        self.assert_title(self.clothes_url, page_title)

    def test_accessories_page(self):
        page_title = 'Accessories'
        self.assert_title(self.accessories_url, page_title)

    def test_login_page(self):
        page_title = 'Login'
        self.assert_title(self.login_url, page_title)

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    def assert_title(self, url, expected_title):
        page_title = self.get_page_title(url)
        self.assertEqual(expected_title, page_title,
                         f'Expected title {expected_title} differ from actual title {page_title} on page url: {url}')
