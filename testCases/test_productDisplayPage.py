import os
import unittest

import pytest

from pageObjects.homePage import HomePage
from pageObjects.productInfoPage import ProductInfoPage
from pageObjects.searchPage import SearchPage
from utilities.custom_logger import LogGen


class Test_003_productDisplayPage(unittest.TestCase):
    logger = LogGen.loggen()

    @pytest.fixture(autouse=True)
    def class_setup(self, setUp):
        self.driver = setUp
        self.home_page = HomePage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.product_page = ProductInfoPage(self.driver)

    def test_validate_product_name_brand_and_code(self):
        self.logger.info("Test started: validating product name, brand, and code.")

        # Search for 'iMac'
        self.logger.info("Searching for product: 'iMac'")
        self.home_page.inputSearchElement("iMac")
        self.home_page.clickOnSearchButton()

        # Navigate to product detail page
        self.logger.info("Opening iMac product detail page.")
        self.search_page.clickOnImacImage()

        # Validate product name
        expected_product_name = "iMac"
        actual_product_name = self.product_page.get_product_name_text()
        self.logger.info("Validating product name")

        try:
            self.assertEqual(
                actual_product_name,
                expected_product_name,
                f"Product name mismatch: expected '{expected_product_name}', but got '{actual_product_name}'"
            )
            self.logger.info("Product name validation passed.")

        except AssertionError as e:
            self._log_failure("product_name_error.png", "product name validation failed", e)

        # Validate brand
        expected_brand = "Apple"
        actual_brand = self.product_page.get_product_brand_text()
        self.logger.info("Validating brand")

        try:
            self.assertEqual(
                actual_brand,
                expected_brand,
                f"Brand mismatch: expected '{expected_brand}', but got '{actual_brand}'"
            )
            self.logger.info("Brand validation passed")

        except AssertionError as e:
            self._log_failure("brand_error.png", "Brand validation failed", e)

        # Validate product code
        expected_product_code = "Product 14"
        actual_product_code = self.product_page.split_product_code_text()
        self.logger.info("Validating product code")
        # print(actual_product_code)

        try:
            self.assertEqual(
                expected_product_code,
                actual_product_code,
                f"Product code mismatch: expected '{expected_product_code}', but got '{actual_product_code}'"
            )
            self.logger.info("Product code validation passed")

        except AssertionError as e:
            self._log_failure("product_code_error", "Product code validation", e)

    def _log_failure(self, screenshot_name, message, exception):
        screenshot_path = os.path.join("screenshots", screenshot_name)
        self.driver.save_screenshot(screenshot_path)
        self.logger.error(f"{message}\n"
                          f"Screenshot saved at: {screenshot_path}\n"
                          f"Details: {exception}")
        raise exception

    def test_validate_product_default_quantity(self):
        pass