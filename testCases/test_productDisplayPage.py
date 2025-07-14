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

        # Step 1: Search for 'iMac'
        self.logger.info("Searching for product: 'iMac'")
        self.home_page.inputSearchElement("iMac")
        self.home_page.clickOnSearchButton()

        # Step 2: Navigate to product detail page
        self.logger.info("Opening iMac product detail page.")
        self.search_page.clickOnImacImage()

        # Step 3: Validate product name
        self.logger.info("check product information's")
        expected_product_name = "iMac"
        actual_product_name = self.product_page.get_product_name_text()
        try:
            self.assertEqual(
                actual_product_name,
                expected_product_name,
                f"Product name mismatch: expected '{expected_product_name}', but got '{actual_product_name}'"
            )
            self.logger.info("Product name validation passed.")

        except AssertionError as e:
            # Save screenshot for failure analysis
            screenshot_name = "product_name_error.png"
            screenshot_path = os.path.join(os.getcwd(), "Screenshots", screenshot_name)
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"Product name validation failed.\n"
                              f"Screenshot saved at: {screenshot_path}\n"
                              f"Details: {e}")
            raise






