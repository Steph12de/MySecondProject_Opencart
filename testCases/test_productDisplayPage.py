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

    def _log_failure(self, screenshot_name, message, exception):
        screenshot_path = os.path.join("screenshots", screenshot_name)
        self.driver.save_screenshot(screenshot_path)
        self.logger.error(f"{message}\n"
                          f"Screenshot saved at: {screenshot_path}\n"
                          f"Details: {exception}")
        raise exception

    def search_and_open_product(self, product_name):
        # Search for 'iMac'
        self.logger.info(f"Starting product search for: '{product_name}'")
        self.home_page.inputSearchElement(product_name)
        self.home_page.clickOnSearchButton()

        # Navigate to product detail page
        self.logger.info(f"Navigating to product detail page for '{product_name}'")
        self.search_page.clickOnImacImage()

    def test_validate_product_name_brand_and_code(self):
        self.logger.info("Test started: validating product name, brand, and code.")

        self.search_and_open_product("iMac")

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
            self._log_failure("product_code_error", "Product code validation failed", e)

    def test_validate_product_default_quantity(self):
        self.logger.info("Test started: validating default quantity of a product set as 1")

        self.search_and_open_product("iMac")

        # Validate one as default quantity
        expected_quantity = 1
        actual_quantity = int(self.product_page.get_quantity_input_field_attribute())
        # print(actual_quantity)

        try:
            self.assertEqual(
                expected_quantity,
                actual_quantity,
                f"Product quantity mismatch: expected '{expected_quantity}', but got '{actual_quantity}'")
            self.logger.info("Product quantity validation passed")

        except AssertionError as e:
            self._log_failure("default_quantity_error.png", "Product quantity validation failed", e)
