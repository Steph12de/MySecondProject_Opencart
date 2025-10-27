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

    def _log_failure(self, screenshot_name, message, exception):
        screenshot_path = os.path.join("screenshots", screenshot_name)
        self.driver.save_screenshot(screenshot_path)
        self.logger.error(f"{message}\n"
                          f"Screenshot saved at: {screenshot_path}\n"
                          f"Details: {exception}")
        raise exception

    # @pytest.mark.skip(reason="Just skipped it right now")
    # @pytest.mark.regression
    def test_add_to_cart_from_product_display(self):
        product_name = "iMac"
        self.logger.info(f"Test: Add '{product_name}' to cart from product detail page")

        # Step 1: Search and navigate to product
        self.home_page.input_search_element(product_name)
        self.home_page.click_Search_button()
        self.logger.info(f"Searching for '{product_name}'")

        self.search_page.click_product_image()
        self.logger.info(f"Navigated to '{product_name}' product detail page")

        # Step 2: Add product to cart
        self.product_page.click_on_add_to_cart_button()
        self.logger.info(f"Attempting to add '{product_name}' to shopping cart")

        try:
            self.assertTrue(
                self.product_page.check_success_message(),
                "Failed to display success message after adding product"
            )
            self.logger.info("Success message displayed correctly after adding the product")
        except AssertionError as error:
            self._log_failure(
                "add_to_cart_missing_success.png.png",
                "Success message missing after adding product to cart",
                error
            )

        # Step 3: Verify product in cart
        self.product_page.click_on_shopping_cart_link()
        self.logger.info("Navigating to shopping cart for verification")

        try:
            self.assertTrue(
                self.cart_page.check_product_name(product_name),
                f"Product '{product_name}' not found in cart"
            )
            self.logger.info(f"Product verification successful — '{product_name}' is in the shopping cart")
        except AssertionError as error:
            self._log_failure(
                "cart_page_product_verification_failed.png",
                f"Product '{product_name}' missing in cart",
                error
            )
        self.driver.close()
        self.logger.info("Test execution completed - Browser closed.")

    @pytest.mark.skip(reason="Just skipped it right now")
    # @pytest.mark.regression
    def test_add_to_cart_from_wish_list(self):
        self.logger.info("Starting test: Add product to wish list.")

        self.home_page.clickOnWishListButton()
        self.logger.info("Navigating to Login section.")

        self.login_page.log_me_in(self.email, self.password)
        self.logger.info("Logging in to proceed with adding product from wish list.")

        self.wishList_page.clickOnAddToCartIcon("Samsung SyncMaster 941BW")
        self.logger.info("Attempting to add 'Samsung SyncMaster 941BW' to shopping cart from wish list.")

        try:
            assert self.product_page.check_success_message() is True, (
                "Success message validation failed!\n"
                "Expected success message was not displayed after adding product to cart."
            )
            self.logger.info("Success message correctly displayed after adding product.")
        except AssertionError as e:
            screenshot_path = os.path.join(os.getcwd(), "Screenshots",
                                           "failed_wishlist_add_to_cart_success_message.png")
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(
                "Error: Success message was not shown after adding product from wish list.\n"
                f"Screenshot saved at: {screenshot_path}\n"
                f"Error details: {e}"
            )
            raise

        self.wishList_page.clickOnShoppingCartHeaderIcon()
        self.logger.info("Navigating to shopping cart to verify product presence.")

        try:
            assert self.cart_page.check_product_name("Samsung SyncMaster 941BW") is True, (
                "Error: 'Samsung SyncMaster 941BW' not found in shopping cart after adding from wish list.\n"
            )
            self.logger.info("'Samsung SyncMaster 941BW' was successfully added to the shopping cart.")
        except AssertionError as e:
            screenshot_path = os.path.join(os.getcwd(), "Screenshots", "failed_wishlist_product_cart_verification.png")
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(
                f"Screenshot saved at: {screenshot_path}\n"
                f"Error details: {e}"
            )
            raise

        self.driver.close()
        self.logger.info("Test execution completed - Browser closed.")

    @pytest.mark.skip(reason="Just skipped it right now")
    # @pytest.mark.regression
    def test_add_to_cart_from_search_result(self):
        self.logger.info("Starting test: Add product to cart from search results.")

        self.home_page.inputSearchElement("iMac")
        self.logger.info("Searching for 'iMac'.")

        self.home_page.clickOnSearchButton()
        text_before = self.search_page.getCardTotalText()
        self.search_page.clickOnAddToCartButton()

        expected_success_message = "Success: You have added iMac to your shopping cart!"

        try:
            assert expected_success_message in self.search_page.getSuccessMessageText(), (
                "Add to cart validation failed!\n"
                "Expected success message was not displayed after adding product.\n"
                f"Expected message: '{expected_success_message}'\n"
                f"Actual message: '{self.search_page.getSuccessMessageText()}'"
            )
            self.logger.info("Success message displayed correctly after adding the product.")
        except AssertionError as e:
            screenshot_path = os.path.join(os.getcwd(), "Screenshots", "failed_add_to_cart_success_message.png")
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(
                f"Error message Screenshot saved at: {screenshot_path}\n"
                f"Error details: {e}"
            )
            raise

        self.logger.info(f"Waiting for shopping cart count to change from '{text_before}' to a new updated value.")
        text_after = text_before
        while text_after == text_before:
            text_after = self.search_page.getCardTotalText()

        self.logger.info(f"Cart item count updated. Previous: '{text_before}', New: '{text_after}'")

        self.search_page.clickOnBlackCardButton()
        self.search_page.clickOnViewCartButton()

        try:
            assert self.cart_page.check_product_name("iMac") is True, (
                "Shopping cart verification failed!\n"
                "'iMac' was expected in the cart but was not found."
            )
            self.logger.info("'iMac' was successfully added to the shopping cart.")
        except AssertionError as e:
            screenshot_path = os.path.join(os.getcwd(), "Screenshots", "failed_cart_product_verification.png")
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(
                f"Screenshot saved at: {screenshot_path}\n"
                f"Error details: {e}"
            )
            raise

        self.driver.close()
        self.logger.info("Test execution completed - Browser closed.")

    @pytest.mark.skip(reason="Just skipped it right now")
    @pytest.mark.regression
    def test_add_to_cart_via_product_comparison_page(self):
        # Step 1: Navigate to login page and log in
        self.logger.info("Navigating to login page.")
        self.home_page.open_login_page()

        self.logger.info("Attempting to log in with provided credentials.")
        self.login_page.log_me_in(self.email, self.password)

        current_title = self.driver.title
        try:
            assert current_title == "My Account", (
                f"Login failed. Expected title: 'My Account', but got: '{current_title}'")
            self.logger.info(f"Login successful - User redirected to '{current_title}'")

        except AssertionError as e:
            self.logger.error(f"Login validation failed. Details: {e}")
            raise

        # Step 2: Navigate to Desktops category and select product for comparison
        self.logger.info("Navigating to Desktops category.")
        self.home_page.go_to_desktops()

        self.logger.info("Clicking on a product (Apple Music) to add it to comparison.")
        self.comparison_page.click_on_apple_music()

        self.logger.info("Clicking on 'Product Compare' link.")
        self.desktops_page.clickOnProductCompareLink()

        # Step 3: Verify that products are available on the comparison page
        try:
            result = self.comparison_page.get_bol_product_unavailability_text()
            print(f"result: {result}")
            self.assertFalse(
                self.comparison_page.get_bol_product_unavailability_text(),
                "Comparison table is empty. No products found."
            )
            self.logger.info("Product comparison list contains items.")
        except AssertionError as e:
            self.logger.error(f"No products available for comparison. Details: {e}")
            raise

        # Step 4: Add product from comparison page to cart
        self.logger.info("Attempting to add product from comparison page to cart.")
        self.comparison_page.get_add_to_cart_options()
        time.sleep(3)

        expected_success_message = "Success: You have added MacBook to your shopping cart!"
        try:
            actual_message = self.comparison_page.get_success_message_text()
            self.logger.info(f"Received success message: '{actual_message}'")

            self.assertIn(expected_success_message, actual_message,
                          (
                              "Add to cart failed.\n"
                              f"Expected message: '{expected_success_message}'\n"
                              f"Actual message: '{actual_message}'"
                          ))

            self.logger.info("Success message was displayed correctly after adding product to cart.")
        except AssertionError as e:
            screenshot_name = "AddToCartComparisonPageError.png"
            screenshot_path = os.path.join(os.getcwd(), "Screenshots", screenshot_name)
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"Add to cart validation failed. Screenshot saved to: {screenshot_path}\n"
                              f"Details: {e}")
            raise

        self.comparison_page.click_on_shopping_card_link()
