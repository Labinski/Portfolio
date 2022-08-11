import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


s = Service("C:\\Users\\User\\Desktop\\Selenium Chromedriver\\chromedriver.exe")


class LostHatFrontPageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=s)
        self.base_url = 'https://autodemo.testoneo.com/en/'

    def tearDown(self):
        self.driver.quit()

    def test_slider_presention(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element(By.XPATH, '//*[@id="carousel"]')

    def test_slider_minimum_size(self):
        expected_min_height = 300
        expected_min_width = 600
        slider_xpath = '//*[@id="carousel"]'
        driver = self.driver

        driver.get(self.base_url)
        slider_element = driver.find_element(By.XPATH, '//*[@id="carousel"]')
        actual_slider_height = slider_element.size['height']
        actual_slider_width = slider_element.size['width']

        with self.subTest('Element height'):
            self.assertLess(expected_min_height, actual_slider_height,
                            f'Element height found by xpath {slider_xpath} on page {driver.current_url} is smaller than expected {expected_min_height}px')

        with self.subTest('Element width'):
            self.assertLess(expected_min_width, actual_slider_width,
                            f'Element width found by xpath {slider_xpath} on page {driver.current_url} is smaller than expected {expected_min_width}px')

    def test_slider_contain_exact_number_of_slides(self):
        expected_number_of_slides = 3
        driver = self.driver

        driver.get(self.base_url)
        slider_elements = driver.find_elements(By.XPATH, '//*[@id="carousel"]/ul/li')
        actual_number_of_slides = len(slider_elements)

        self.assertEqual(expected_number_of_slides, actual_number_of_slides,
                         f'Number of slides differ for page {self.base_url}')

    def test_slides_required_title_text(self):
        expected_text_included_in_side = 'sample'
        driver = self.driver

        driver.get(self.base_url)
        title_elements = driver.find_elements(By.XPATH,
                                              '//*[@id="carousel"]/ul/li//*[contains(@class, "text-uppercase")]')

        for title_element in title_elements:
            title_element_text = title_element.get_attribute("textContent")
            title_element_text_lower = title_element_text.lower()
            self.assertIn(expected_text_included_in_side, title_element_text_lower,
                          f'Slides does not contain expected text for page {self.base_url}')

    def test_exact_number_of_products_on_main_page(self):
        expected_number_of_products = 8
        driver = self.driver

        driver.get(self.base_url)
        product_elements = driver.find_elements(By.XPATH, '//*[@class="product-miniature js-product-miniature"]')
        actual_number_of_products = len(product_elements)

        self.assertEqual(expected_number_of_products, actual_number_of_products,
                         f'Number of products differ from expected for page {self.base_url}')



