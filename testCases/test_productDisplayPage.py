import os
import time
import unittest

import pytest

from pageObjects.homePage import HomePage
from pageObjects.productInfoPage import ProductInfoPage
from pageObjects.searchPage import SearchPage
from pageObjects.shoppingCartPage import ShoppingCartPage
from utilities.custom_logger import LogGen


class Test_003_productDisplayPage(unittest.TestCase):
    logger = LogGen.loggen()

    @pytest.fixture(autouse=True)
    def class_setup(self, setUp):
        self.driver = setUp
        self.home_page = HomePage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.product_page = ProductInfoPage(self.driver)
        self.cart_page = ShoppingCartPage(self.driver)

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
        if product_name == "iMac":
            self.logger.info(f"Navigating to product detail page for '{product_name}'")
            self.search_page.clickOnImacImage()

        elif product_name == 'Apple Cinema 30"':
            self.logger.info(f"Navigating to product detail page for '{product_name}'")
            self.search_page.click_on_apple_cinema_image()

        else:
            return None

    def add_to_cart_and_check(self, quantity):
        self.product_page.input_quantity(quantity)
        self.product_page.click_on_add_to_cart_button()
        # self.product_page.scroll_element_into_shopping_link_view()
        element_result = self.product_page.get_success_message_box()
        if element_result:
            self.logger.info("The product has been successfully added")
        self.product_page.click_on_shopping_cart_link()

    def submit_review(self, product_name, reviewer_name, review_text):
        product_name = product_name
        reviewer_name = reviewer_name
        review_text = review_text

        self.logger.info(f"Test started: validating product review submission for '{product_name}'")

        # Step 1: Open product detail page
        self.search_and_open_product(product_name)

        # Step 2: Fill out and submit review
        self.logger.info("Writing review...")
        self.product_page.click_reviews_button()
        self.product_page.input_name_reviewer(reviewer_name)
        self.product_page.input_review(review_text)
        self.product_page.select_radio_button_rating()
        self.product_page.click_continue_button_reviews()

    @pytest.mark.skip(reason="Just skipped it right now")
    def test_product_detail_displays_name_brand_and_code(self):
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
                actual_product_code,
                expected_product_code,
                f"Product code mismatch: expected '{expected_product_code}', but got '{actual_product_code}'"
            )
            self.logger.info("Product code validation passed")

        except AssertionError as e:
            self._log_failure("product_code_error", "Product code validation failed", e)

    @pytest.mark.skip(reason="Just skipped it right now")
    def test_default_quantity_is_one_when_minimum_not_set(self):
        self.logger.info("Test started: validating that default product quantity is set to 1.")

        # Search and open product detail page
        self.search_and_open_product("iMac")

        # Validate default quantity is 1
        expected_quantity = 1
        actual_quantity = int(self.product_page.get_quantity_input_field_attribute())

        self.logger.info(f"Checking default quantity: expected '{expected_quantity}', found '{actual_quantity}'")
        try:
            self.assertEqual(
                actual_quantity,
                expected_quantity,
                f"Default quantity mismatch: expected '{expected_quantity}', got '{actual_quantity}'"
            )
            self.logger.info("Default quantity validation passed.")

        except AssertionError as e:
            self._log_failure("default_quantity_error.png", "Default quantity validation failed", e)

        # Increase quantity and add to cart
        increase_by = 4
        self.logger.info(f"Increasing quantity by {increase_by} and adding product to cart.")
        self.product_page.increase_product_quantity(increase_by)
        self.product_page.click_on_add_to_cart_button()

        # Validate success message after adding product
        expected_success = "Success: You have added iMac to your shopping cart!\n×"
        actual_success = self.product_page.get_success_message_text()
        self.logger.info(f"Validating success message after adding product: '{actual_success}'")

        try:
            self.assertEqual(
                actual_success,
                expected_success,
                f"success message mismatch: expected '{expected_success}', but got '{actual_success}'"
            )
            self.logger.info("Success message validation passed.")

        except AssertionError as e:
            self._log_failure("add_to_cart_error.png",
                              "Success message validation failed after adding product.",
                              e)

        # Validate updated quantity shown in cart icon
        expected_total_quantity = increase_by
        actual_cart_quantity = int(self.product_page.split_black_item_button_text())

        try:
            self.assertEqual(
                actual_cart_quantity,
                expected_total_quantity,
                f"Cart quantity mismatch: expected'{expected_total_quantity}', but got '{actual_cart_quantity}'"
            )
            self.logger.info("Cart quantity validation passed.")

        except (IndexError, ValueError, AssertionError) as e:
            self._log_failure("cart_icon_quantity_error.png",
                              "Cart quantity validation failed – either due to unreadable cart icon format or mismatch.",
                              e)

    @pytest.mark.skip(reason="Just skipped it right now")
    def test_product_minimum_quantity_is_correctly_set(self):
        self.logger.info("Test started: validating that default product quantity is set to 1.")

        # Search and open product detail page
        product_name = 'Apple Cinema 30"'
        self.search_and_open_product(product_name)

        # Validate minimum quantity and associated message
        expected_quantity = 2
        actual_quantity = int(self.product_page.get_quantity_input_field_attribute())

        expected_info_text = "This product has a minimum quantity of 2"
        actual_info_text = self.product_page.get_minimum_quantity_text()

        try:
            self.assertEqual(
                actual_quantity,
                expected_quantity,
                f"Minimum quantity mismatch: expected '{expected_quantity}' but got '{actual_quantity}'"
            )
            self.assertEqual(
                actual_info_text,
                expected_info_text,
                f"Minimum quatity text are not same: expected'{expected_info_text}' but got '{actual_info_text}'"
            )
            self.logger.info("Minimum quantity and information text validated successfully.")

        except AssertionError as e:
            self._log_failure(
                "minimum_quantity_error.png",
                "Minimum quantity validation failed – either numeric value or message text is incorrect.",
                e)

        # Fill mandatory fields
        self.logger.info("Filling mandatory fields on product display page.")
        self.product_page.fill_mandatory_fields_product_display()

        # Try adding below minimum quantity
        self.add_to_cart_and_check(1)

        expected_warning = 'Minimum order amount for Apple Cinema 30" is 2!'
        actual_warning = self.cart_page.get_warning_message_text()
        try:
            self.assertEqual(actual_warning,
                             expected_warning,
                             f"warning message mismatch expected:'{expected_warning}' but got:'{actual_warning}'")
            self.logger.info("Warning message after adding below-minimum quantity validated")

        except AssertionError as e:
            self._log_failure("waning_message_error.png",
                              "Warning message validation failed",
                              e)

        # Upload file and increase valid quantity
        self.driver.back()
        self.product_page.upload_file_()
        self.add_to_cart_and_check(5)

        warning_present = self.cart_page.check_presence_of_warning_message()
        try:
            self.assertFalse(warning_present,
                             "Warning message still present after adding valid quantity")
            self.logger.info("No warning — product added successfully with correct quantity")
        except AssertionError as e:
            self._log_failure("visibility_warning_message_error.png",
                              "Warning appeared despite valid quantity",
                              e)
        # Validate product name and quantity in cart
        product_name_valid = self.cart_page.check_product_name('Apple Cinema 30"')
        product_quantity_valid = self.cart_page.check_product_quantity(str(5))
        try:
            self.assertTrue(
                product_name_valid,
                "Product name not found in cart"
            )
            self.assertTrue(
                product_quantity_valid,
                "Product quantity not found or incorrect in cart"
            )
            self.logger.info("Product name and quantity successfully verified in cart")
        except AssertionError as e:
            self._log_failure("product_name_quantity_error.png",
                              "Either product name or quantity in cart does not match expected values ",
                              e)

    @pytest.mark.skip(reason="Just skipped it right now")
    def test_user_can_submit_product_review_on_display_page(self):
        self.logger.info("Test: Submit valid review and verify system response")

        reviewer_name = "Steph"
        review_text = "Very good product, recommended!"
        self.submit_review("iMac", reviewer_name, review_text)

        if 3 <= len(reviewer_name) <= 25 <= len(review_text) <= 1000:
            expected_success_message = "Thank you for your review. It has been submitted to the webmaster for approval."
            actual_success_message = self.product_page.get_success_message_reviews_text()

            self.logger.info(f"Received success message: '{actual_success_message}'")

            try:
                self.assertEqual(
                    actual_success_message,
                    expected_success_message,
                    f"Review success message mismatch:\nExpected: '{expected_success_message}'\nGot: '{actual_success_message}'"
                )
                self.logger.info("Review submitted successfully and confirmation message is correct.")
            except AssertionError as e:
                self._log_failure(
                    "review_submission_error.png",
                    "Review submission failed – success message did not match expected text.",
                    e
                )
        else:
            self.logger.warning("Input validation failed: reviewer name or review text length is out of bounds.")

    def test_review_text_length_outside_valid_range(self):
        self.logger.info("Test: Submit invalid review and verify warning messages")

        reviewer_name = "St"  # Zu kurz (<3)
        review_text = "Good!"  # Zu kurz (<25)

        self.submit_review("iMac", reviewer_name, review_text)

        expected_text_warning = "Warning: Review Text must be between 25 and 1000 characters!"
        expected_name_warning = "Warning: Review Name must be between 3 and 25 characters!"

        name_invalid = len(reviewer_name) < 3 or len(reviewer_name) > 25
        text_invalid = len(review_text) < 25 or len(review_text) > 1000

        self.logger.info(f"🔍 Input lengths — Name: {len(reviewer_name)}, Text: {len(review_text)}")

        if name_invalid and not text_invalid:
            actual_name_warning = self.product_page.get_warning_review_name_message()
            self.logger.info(f" Received name warning: '{actual_name_warning}'")

            try:
                self.assertEqual(
                    actual_name_warning,
                    expected_name_warning,
                    f"Name warning mismatch:\nExpected: '{expected_name_warning}'\nGot: '{actual_name_warning}'"
                )
                self.logger.info("✅ Correct warning message for reviewer name length.")
            except AssertionError as e:
                self._log_failure("review_name_warning_error.png",
                                  "Reviewer name length validation failed.",
                                  e)

        elif text_invalid:
            actual_text_warning = self.product_page.get_warning_review_text_message()
            self.logger.info(f"Received text warning: '{actual_text_warning}'")

            try:
                self.assertEqual(
                    actual_text_warning,
                    expected_text_warning,
                    f"Text warning mismatch:\nExpected: '{expected_text_warning}'\nGot: '{actual_text_warning}'"
                )
                self.logger.info("Correct warning message for review text length.")
            except AssertionError as e:
                self._log_failure("review_text_warning_error.png",
                                  "Review text length validation failed.",
                                  e)
        else:
            self.logger.warning("Reviewer name and review text length are valid — no warning expected.")


