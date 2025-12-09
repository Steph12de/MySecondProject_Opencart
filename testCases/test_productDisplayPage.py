import os
import time
import unittest

import pytest

from pageObjects.comparisonPage import ComparisonPage
from pageObjects.homePage import HomePage
from pageObjects.loginPage import LoginPage
from pageObjects.logoutPage import LogoutPage
from pageObjects.myAccountPage import MyAccountPage
from pageObjects.productInfoPage import ProductInfoPage
from pageObjects.searchPage import SearchPage
from pageObjects.shoppingCartPage import ShoppingCartPage
from pageObjects.subcategoryDesktopsPage import SubcategoryDesktopsPage
from pageObjects.wishListPage import WishListPage
from utilities.custom_logger import LogGen
from utilities.helpers.helpers import Helpers


class Test_003_productDisplayPage(unittest.TestCase):
    logger = LogGen.loggen()

    @pytest.fixture(autouse=True)
    def class_setup(self, setUp):
        self.driver = setUp
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.myAccount_page = MyAccountPage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.product_page = ProductInfoPage(self.driver)
        self.wishList_page = WishListPage(self.driver)
        self.cart_page = ShoppingCartPage(self.driver)
        self.desktops_page = SubcategoryDesktopsPage(self.driver)
        self.comparison_page = ComparisonPage(self.driver)
        self.logout_page = LogoutPage(self.driver)
        self.helper = Helpers(self.driver, self.logger, self.home_page, self.login_page, self.myAccount_page,
                              self.wishList_page,
                              self.search_page, self.product_page, self.cart_page, self.logout_page)

    # def add_to_cart_and_check(self, quantity):
    #     self.product_page.input_quantity(quantity)
    #     self.product_page.click_on_add_to_cart_button()
    #     # self.product_page.scroll_element_into_shopping_link_view()
    #     element_result = self.product_page.get_success_message_box()
    #     if element_result:
    #         self.logger.info("The product has been successfully added")
    #     self.product_page.click_on_shopping_cart_link()

    def validate_field(self, expected, actual, field_name, screenshot_name):
        try:
            self.assertEqual(
                actual,
                expected,
                f"{field_name} mismatch: expected '{expected}', but got '{actual}'"
            )
            self.logger.info(f"{field_name} validation passed.")
        except AssertionError as e:
            self.helper.log_failure(screenshot_name, f"{field_name} validation failed", e)

    @pytest.mark.skip(reason="Just skipped it right now")
    def test_product_detail_displays_name_brand_and_code(self):
        self.logger.info("Test started: validating product name, brand, and code.")
        product_name = "iMac"

        # Step 1: Search for defined product
        self.helper.search_for_product(product_name)

        # Step 2: Open product detail page for defined product
        self.helper.open_product_detail(product_name)

        # Step 3: Validate product name
        expected_product_name = "iMac"
        actual_product_name = self.product_page.get_product_name_text()
        self.logger.info("Validating product name")
        self.validate_field(expected_product_name, actual_product_name, "Product name", "product_name_error.png")

        # Step 4: Validate brand
        expected_brand = "Apple"
        actual_brand = self.product_page.get_product_brand_text()
        self.logger.info("Validating brand")
        self.validate_field(expected_brand, actual_brand, "Brand", "brand_error.png")

        # Step 5: Validate product code
        expected_product_code = "Product 14"
        actual_product_code = self.product_page.split_product_code_text()
        self.logger.info("Validating product code")
        self.validate_field(expected_product_code, actual_product_code, "Product code", "product_code_error.png")

    @pytest.mark.skip(reason="Just skipped it right now")
    def test_default_quantity_is_one_when_minimum_not_set(self):
        self.logger.info("Test started: validating that default product quantity is set to 1.")
        product_name = "iMac"

        # Step 1: Search for product
        self.helper.search_for_product(product_name)
        self.logger.info(f"Search completed for product: {product_name}")

        # Step 2: Open product detail page
        self.helper.open_product_detail(product_name)
        self.logger.info(f"Opened product detail page for: {product_name}")

        # Step 3: Validate default quantity is 1
        expected_quantity = 1
        actual_quantity = int(self.product_page.get_quantity_input_field_attribute())
        self.logger.info(f"Checking default quantity: expected '{expected_quantity}', found '{actual_quantity}'")
        self.validate_field(expected_quantity, actual_quantity, "Default quantity", "default_quantity_error.png")

        # Step 4: Increase quantity and add to cart
        increase_by = 4
        self.logger.info(f"Increasing quantity by {increase_by} and adding product to cart.")
        self.product_page.increase_product_quantity(increase_by)
        self.product_page.click_on_add_to_cart_button()

        # Step 5: Validate success message after adding product
        actual_success = self.product_page.get_success_message_text()
        self.logger.info(f"Validating success message after adding product: '{actual_success}'")
        try:
            self.helper.verify_success_message_contains_product(
                "Success: You have added",
                product_name,
                "product_display")
        except AssertionError as e:
            self.helper.log_failure("default_quantity_add_to_cart_error.png",
                                    "Success message validation failed after adding product.",
                                    e)

        # Step 6: Validate updated quantity shown in cart icon
        expected_total_quantity = increase_by
        actual_cart_quantity = int(self.product_page.split_black_item_button_text())
        try:
            self.validate_field(expected_total_quantity, actual_cart_quantity, "Cart icon quantity",
                                "cart_icon_quantity_error.png"
                                )
        except (IndexError, ValueError, AssertionError) as e:
            self.helper.log_failure("cart_icon_quantity_error.png",
                                    "Cart quantity validation failed – either due to unreadable cart icon format or "
                                    "mismatch.",
                                    e)

    @pytest.mark.skip(reason="Just skipped it right now")
    def test_product_minimum_quantity_is_correctly_set(self):
        self.logger.info("Test started: validating that minimum product quantity is correctly set.")
        product_name = 'Apple Cinema 30"'

        # Step 1: Search and open product detail page
        self.helper.search_for_product(product_name)
        self.helper.open_product_detail(product_name)

        # Step 2: Validate minimum quantity and associated message
        expected_minimum_quantity_value = 2
        actual_minimum_quantity_value = int(self.product_page.get_quantity_input_field_attribute())

        expected_minimum_quantity_message = "This product has a minimum quantity of 2"
        actual_minimum_quantity_message = self.product_page.get_minimum_quantity_text()

        self.logger.info("Validating minimum quantity value and minimum quantity message")
        self.validate_field(expected_minimum_quantity_value, actual_minimum_quantity_value, "Minimum quantity",
                            "minimum_quantity_error.png")
        self.validate_field(expected_minimum_quantity_message, actual_minimum_quantity_message, "Minimum quantity info text",
                            "minimum_quantity_text_error.png")

        # Step 3: Fill mandatory fields
        self.logger.info("Filling mandatory fields on product display page.")
        self.product_page.fill_mandatory_fields_product_display()

        # Step 4: Try adding below minimum quantity
        invalid_quantity = 1
        self.helper.add_to_cart_and_check(invalid_quantity)

        expected_warning_message = f'Minimum order amount for {product_name} is {expected_minimum_quantity_value}!'
        actual_warning_message = self.cart_page.get_warning_message_text()
        self.validate_field(expected_warning_message, actual_warning_message, "Minimum quantity warning",
                            "warning_message_error.png")

        # Step 5: Upload file and increase valid quantity
        valid_quantity = 5
        self.driver.back()
        self.product_page.upload_file_()
        self.helper.add_to_cart_and_check(valid_quantity)

        warning_still_visible = self.cart_page.check_presence_of_warning_message()
        try:
            self.assertFalse(warning_still_visible,
                             "Warning message still present after adding valid quantity")
            self.logger.info("No warning — product added successfully with correct quantity")
        except AssertionError as e:
            self.helper.log_failure("visibility_warning_message_error.png",
                                    "Warning appeared despite valid quantity", e)

        # Step 6: Validate product name and quantity in cart
        product_name_in_cart = self.cart_page.check_product_name(product_name)
        product_quantity_in_cart = self.cart_page.check_product_quantity(str(valid_quantity))
        try:
            self.assertTrue(product_name_in_cart, "Product name not found in cart")
            self.assertTrue(product_quantity_in_cart, "Product quantity not found or incorrect in cart")
            self.logger.info("Product name and quantity successfully verified in cart")
        except AssertionError as e:
            self.helper.log_failure("product_name_quantity_error.png",
                                    "Either product name or quantity in cart does not match expected values ",e)


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

    # def test_review_text_length_outside_valid_range(self):
    #     self.logger.info("Test: Submit invalid review and verify warning messages")
    #
    #     reviewer_name = "St"  # Zu kurz (<3)
    #     review_text = "Good!"  # Zu kurz (<25)
    #
    #     self.submit_review("iMac", reviewer_name, review_text)
    #
    #     expected_text_warning = "Warning: Review Text must be between 25 and 1000 characters!"
    #     expected_name_warning = "Warning: Review Name must be between 3 and 25 characters!"
    #
    #     name_invalid = len(reviewer_name) < 3 or len(reviewer_name) > 25
    #     text_invalid = len(review_text) < 25 or len(review_text) > 1000
    #
    #     self.logger.info(f"🔍 Input lengths — Name: {len(reviewer_name)}, Text: {len(review_text)}")
    #
    #     if name_invalid and not text_invalid:
    #         actual_name_warning = self.product_page.get_warning_review_name_message()
    #         self.logger.info(f" Received name warning: '{actual_name_warning}'")
    #
    #         try:
    #             self.assertEqual(
    #                 actual_name_warning,
    #                 expected_name_warning,
    #                 f"Name warning mismatch:\nExpected: '{expected_name_warning}'\nGot: '{actual_name_warning}'"
    #             )
    #             self.logger.info("✅ Correct warning message for reviewer name length.")
    #         except AssertionError as e:
    #             self._log_failure("review_name_warning_error.png",
    #                               "Reviewer name length validation failed.",
    #                               e)
    #
    #     elif text_invalid:
    #         actual_text_warning = self.product_page.get_warning_review_text_message()
    #         self.logger.info(f"Received text warning: '{actual_text_warning}'")
    #
    #         try:
    #             self.assertEqual(
    #                 actual_text_warning,
    #                 expected_text_warning,
    #                 f"Text warning mismatch:\nExpected: '{expected_text_warning}'\nGot: '{actual_text_warning}'"
    #             )
    #             self.logger.info("Correct warning message for review text length.")
    #         except AssertionError as e:
    #             self._log_failure("review_text_warning_error.png",
    #                               "Review text length validation failed.",
    #                               e)
    #     else:
    #         self.logger.warning("Reviewer name and review text length are valid — no warning expected.")
