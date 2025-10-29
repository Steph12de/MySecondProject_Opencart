import os
import time

import pytest

from pageObjects.comparisonPage import ComparisonPage
from pageObjects.homePage import HomePage
from pageObjects.loginPage import LoginPage
from pageObjects.myAccountPage import MyAccountPage
from pageObjects.productInfoPage import ProductInfoPage
from pageObjects.searchPage import SearchPage
from pageObjects.shoppingCartPage import ShoppingCartPage
from pageObjects.subcategoryDesktopsPage import SubcategoryDesktopsPage
from pageObjects.wishListPage import WishListPage
from utilities.custom_logger import LogGen
from ddt import ddt, data, unpack
import unittest
from utilities.helpers.helpers import Helpers

from utilities.readProperties import ReadConfig


@ddt
class Test_004_addToCart(unittest.TestCase):
    logger = LogGen.loggen()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()

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
        self.helper = Helpers(self.driver, self.logger, self.home_page, self.login_page, self.myAccount_page,
                              self.wishList_page,
                              self.search_page, self.product_page, self.cart_page)

    # @pytest.mark.skip(reason="Just skipped it right now")
    # @pytest.mark.regression
    def test_add_displayed_product_to_cart(self):
        product_name = "iMac"
        self.logger.info(f"Test: Add '{product_name}' to cart from product detail page")

        # Step 1: Search and navigate to product
        self.helper.search_for_product(product_name)
        self.search_page.click_product_image()
        self.logger.info(f"Navigated to '{product_name}' product detail page")

        # Step 2: Add product to cart
        self.product_page.click_on_add_to_cart_button()
        self.logger.info(f"Attempting to add '{product_name}' to shopping cart")

        # Step 3: Verify success message

        try:
            self.helper.verify_success_message_contains_product(
                "Success: You have added",
                product_name,
                "product_display"
            )
        except AssertionError as error:
            self.helper.log_failure(
                "product_display_success_validation_failed.png",
                f"Validation failed for success message after adding '{product_name}' from product display page",
                error
            )

        # Step 4: Verify product in cart
        try:
            self.helper.verify_product_in_cart(product_name, "product_display")
        except AssertionError as error:
            self.helper.log_failure(
                "product_display_cart_verification_failed.png",
                f"Product '{product_name}' missing in cart",
                error
            )

    # @pytest.mark.skip(reason="Just skipped it right now")
    # @pytest.mark.regression
    def test_add_wishlist_product_to_cart(self):
        product_name = "Samsung SyncMaster 941BW"
        self.logger.info(f"Test: Add '{product_name}' to cart from wishlist")

        # Step 1: Navigate to wishlist and login
        self.home_page.click_wishlist_icon()
        self.logger.info("Navigated to wishlist login section")

        self.login_page.log_me_in(self.email, self.password)

        # Step 2: Verify product presence in wishlist
        try:
            self.assertTrue(
                self.wishList_page.is_product_in_wishlist(product_name),
                f"Product '{product_name}' not found in wishlist. Please add it first"
            )
            self.logger.info(f"Product '{product_name}' is available in the wishlist")

        except AssertionError as error:
            self.helper.log_failure(
                "wishlist_product_missing.png",
                f"Product '{product_name}' not found in wishlist",
                error
            )

        # Step 3: Add product to cart
        self.wishList_page.click_add_to_cart_icon(product_name)
        self.logger.info(f"Attempting to add '{product_name}' to cart from wishlist")

        # Step 4: Verify success message
        try:
            self.helper.verify_success_message_contains_product(
                "Success: You have added",
                product_name,
                "wishlist"
            )

        except AssertionError as error:
            self.helper.log_failure(
                "wishlist_success_message_validation_failed.png",
                f"Validation failed for success message after adding '{product_name}' from wishlist",
                error
            )

        # Step 5: Verify product in cart
        try:
            self.helper.verify_product_in_cart(product_name, "wishlist")
        except AssertionError as error:
            self.helper.log_failure(
                "wishlist_cart_verification_failed.png",
                f"Product '{product_name}' missing in cart after wishlist add",
                error
            )

    # @pytest.mark.skip(reason="Just skipped it right now")
    # @pytest.mark.regression
    def test_add_to_cart_from_search_result(self):
        product_name = "iMac"
        expected_success_message = f"Success: You have added {product_name} to your shopping cart!"

        self.logger.info(f"Test: Add '{product_name}' to cart from search results")

        # Step 1: Search for product
        self.helper.search_for_product(product_name)

        cart_count_before = self.search_page.get_cart_total_text()
        self.logger.info(f"Cart count before add: '{cart_count_before}'")

        # Step 2: Add product to cart
        self.search_page.click_add_to_cart_button()
        self.logger.info(f"Clicked 'Add to Cart' for '{product_name}'")

        # Step 3: Verify success message
        try:
            self.helper.verify_success_message_contains_product(
                "Success: You have added",
                product_name,
                "search_results"
            )
        except AssertionError as error:
            self.helper.log_failure(
                "search_result_success_message_failed.png",
                f"Success message mismatch after adding '{product_name}' from search results",
                error
            )

        # Step 4: Wait for cart count to update
        self.logger.info(
            f"Waiting for shopping cart count to change from '{cart_count_before}' to a new updated value.")
        cart_count_after = cart_count_before
        while cart_count_after == cart_count_before:
            cart_count_after = self.search_page.get_cart_total_text()

        self.logger.info(f"Cart count updated: before='{cart_count_before}', after='{cart_count_after}'")

        # Step 5: Verify product in cart
        try:
            self.helper.verify_product_in_cart(product_name, "search_results")
        except AssertionError as error:
            self.helper.log_failure(
                "search_result_cart_verification_failed.png",
                f"Product '{product_name}' missing in cart after search result add",
                error
            )

    # @pytest.mark.skip(reason="Just skipped it right now")
    # @pytest.mark.regression
    # def test_add_to_cart_via_product_comparison_page(self):
    #     # Step 1: Navigate to login page and log in
    #     self.logger.info("Navigating to login page.")
    #     self.home_page.open_login_page()
    #
    #     self.logger.info("Attempting to log in with provided credentials.")
    #     self.login_page.log_me_in(self.email, self.password)
    #
    #     current_title = self.driver.title
    #     try:
    #         assert current_title == "My Account", (
    #             f"Login failed. Expected title: 'My Account', but got: '{current_title}'")
    #         self.logger.info(f"Login successful - User redirected to '{current_title}'")
    #
    #     except AssertionError as e:
    #         self.logger.error(f"Login validation failed. Details: {e}")
    #         raise
    #
    #     # Step 2: Navigate to Desktops category and select product for comparison
    #     self.logger.info("Navigating to Desktops category.")
    #     self.home_page.go_to_desktops()
    #
    #     self.logger.info("Clicking on a product (Apple Music) to add it to comparison.")
    #     self.comparison_page.click_on_apple_music()
    #
    #     self.logger.info("Clicking on 'Product Compare' link.")
    #     self.desktops_page.clickOnProductCompareLink()
    #
    #     # Step 3: Verify that products are available on the comparison page
    #     try:
    #         result = self.comparison_page.get_bol_product_unavailability_text()
    #         print(f"result: {result}")
    #         self.assertFalse(
    #             self.comparison_page.get_bol_product_unavailability_text(),
    #             "Comparison table is empty. No products found."
    #         )
    #         self.logger.info("Product comparison list contains items.")
    #     except AssertionError as e:
    #         self.logger.error(f"No products available for comparison. Details: {e}")
    #         raise
    #
    #     # Step 4: Add product from comparison page to cart
    #     self.logger.info("Attempting to add product from comparison page to cart.")
    #     self.comparison_page.get_add_to_cart_options()
    #     time.sleep(3)
    #
    #     expected_success_message = "Success: You have added MacBook to your shopping cart!"
    #     try:
    #         actual_message = self.comparison_page.get_success_message_text()
    #         self.logger.info(f"Received success message: '{actual_message}'")
    #
    #         self.assertIn(expected_success_message, actual_message,
    #                       (
    #                           "Add to cart failed.\n"
    #                           f"Expected message: '{expected_success_message}'\n"
    #                           f"Actual message: '{actual_message}'"
    #                       ))
    #
    #         self.logger.info("Success message was displayed correctly after adding product to cart.")
    #     except AssertionError as e:
    #         screenshot_name = "AddToCartComparisonPageError.png"
    #         screenshot_path = os.path.join(os.getcwd(), "Screenshots", screenshot_name)
    #         self.driver.save_screenshot(screenshot_path)
    #         self.logger.error(f"Add to cart validation failed. Screenshot saved to: {screenshot_path}\n"
    #                           f"Details: {e}")
    #         raise
    #
    #     self.comparison_page.click_on_shopping_card_link()
