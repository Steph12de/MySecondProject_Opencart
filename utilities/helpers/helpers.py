import os
from unittest import TestCase


class Helpers:
    def __init__(self, driver, logger, home_page, login_page, my_account, wish_list, search_page, product_page, cart_page, logout_page):
        self.driver = driver
        self.logger = logger
        self.home_page = home_page
        self.login_page = login_page
        self.my_account = my_account
        self.wish_list = wish_list
        self.search_page = search_page
        self.product_page = product_page
        self.cart_page = cart_page
        self.logout_page = logout_page

    def log_failure(self, screenshot_name, message, exception):
        screenshot_path = os.path.join("screenshots", screenshot_name)
        self.driver.save_screenshot(screenshot_path)
        self.logger.error(
            f"{message}\n"
            f"Screenshot saved at: {screenshot_path}\n"
            f"Details: {exception}"
        )
        raise exception

    def navigate_and_optional_login(self, email, password, expected_title="My Account", want_to_login=False,
                                    via_menu=False, using_keyboard=False):
        self.logger.info("Starting Re/login process")

        # Step 1: Navigate to login page
        self.home_page.open_login_page()
        self.logger.info("Navigated to login page")

        if not want_to_login:
            self.logger.info("Login skipped — only navigation performed")
        else:
            # Step 2: Choose login method
            if via_menu:
                self.login_page.click_login_button_right_hand_menu()
                self.logger.info("Triggered login via right-hand menu")

            if using_keyboard:
                self.login_page.log_me_in_using_keyboard(email, password)
                self.logger.info("Submitted credentials using keyboard navigation")
            else:
                self.login_page.log_me_in(email, password)
                self.logger.info("Submitted credentials using standard form submission")

            # Step 3: Wait for expected title to appear
            try:
                self.my_account.check_presence_of_title(expected_title)
                self.logger.info(f"Expected title '{expected_title}' was found")
            except Exception as e:
                self.logger.error(f"Expected title '{expected_title}' not found — possible login failure")
                self.logger.exception(e)

        # Step 4: Return current page title
        actual_title = self.driver.title
        self.logger.info(f"Actual page title after login: '{actual_title}'")

        return actual_title

    def verify_login_successful(self, actual_title, expected_title, method="standard"):
        assert actual_title == expected_title, (
            f"Login using {method} failed\nExpected title: '{expected_title}'\nGot: '{actual_title}'"
        )
        self.logger.info(f"Login using {method} successful — user redirected to '{actual_title}'")

    def verify_logout_successful(self, expected_title):
        self.logout_page.check_presence_of_title(expected_title)
        actual_title = self.driver.title
        self.logger.info(f"Logout page title: '{actual_title}'")
        assert actual_title == expected_title, (
            f"Logout failed — expected title: '{expected_title}', but got: '{actual_title}'"
        )
        self.logger.info("Logout successful")

    def verify_access_restriction_redirect(self, expected_title):
        self.login_page.check_presence_of_title(expected_title)
        actual_title = self.driver.title
        self.logger.info(f"Redirect page title after logout: '{actual_title}'")
        assert actual_title == expected_title, (
            f"Access restriction failed — expected redirect to '{expected_title}', but got: '{actual_title}'"
        )
        self.logger.info("Access restriction after logout verified successfully")

    def search_for_product(self, product_name):
        self.logger.info(f"Initiating search for product: '{product_name}'")
        self.home_page.input_search_element(product_name)
        self.home_page.click_Search_icon()
        self.logger.info(f"Search triggered for '{product_name}'")

    def verify_product_in_cart(self, product_name, source="wishlist"):
        self.logger.info(f"Verifying product '{product_name}' in cart (source: {source})")

        # Step 1: Navigate to cart based on source
        if source.lower() == "wishlist":
            self.wish_list.click_shopping_cart_header_icon()
            self.logger.info("Navigated to cart via wishlist header icon")

        elif source.lower() == "search_results":
            self.search_page.click_black_cart_icon()
            self.search_page.click_view_cart_button()
            self.logger.info("Navigated to cart via search results")

        elif source.lower() == "product_display":
            self.product_page.click_on_shopping_cart_link()
            self.logger.info("Navigated to cart via product display page")

        else:
            self.logger.warning(f"Unknown source '{source}' — defaulting to product page cart link")
            self.product_page.click_on_shopping_cart_link()

        # Step 2: Verify product presence in cart
        assert self.cart_page.check_product_name(product_name), (
            f"Product '{product_name}' not found in cart after adding from '{source}'"
        )
        self.logger.info(f"Product '{product_name}' successfully verified in shopping cart")

    def verify_success_message_contains_product(self, expected_start, product_name, source="product_display"):
        self.logger.info(f"Verifying success message after adding '{product_name}' to cart (source: {source})")

        # Step 1: Get success message based on source
        if source.lower() == "wishlist":
            success_message = self.wish_list.get_success_message_text()
            self.logger.info("Retrieved success message from wishlist flow")

        elif source.lower() == "search_results":
            success_message = self.search_page.get_success_message_text()
            self.logger.info("Retrieved success message from search results flow")

        elif source.lower() == "product_display":
            success_message = self.product_page.get_success_message_text()
            self.logger.info("Retrieved success message from product display flow")

        else:
            self.logger.warning(f"Unknown source '{source}' — defaulting to product page")
            success_message = self.product_page.get_success_message_text()

        # Check if success message starts with expected text
        assert success_message.startswith(expected_start), "Success message does not start with expected text"
        self.logger.info(f"Success message starts with expected text: '{expected_start}'")

        # Check if product name is included
        assert product_name in success_message, f"Success message does not contain product name '{product_name}'"
        self.logger.info(f"Success message contains correct product name: '{product_name}'")
