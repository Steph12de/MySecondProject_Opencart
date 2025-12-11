import os
from unittest import TestCase


class Helpers:
    def __init__(self, driver, logger, home_page, login_page, my_account, wish_list, search_page, product_page,
                 cart_page, logout_page):
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

    def verify_password_change_successful(self, expected_success_message, ):
        pass

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

    def open_product_detail(self, product_name):
        self.logger.info("Opens the product detail page based on product name")
        if product_name == "iMac":
            self.logger.info(f"Navigating to product detail page for '{product_name}'")
            self.search_page.click_product_image()

        elif product_name == 'Apple Cinema 30"':
            self.logger.info(f"Navigating to product detail page for '{product_name}'")
            self.search_page.click_on_apple_cinema_image()

        else:
            self.logger.warning(f"No click action defined for product: '{product_name}'")
            return None

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

        # Step 2: Verify product presence in cart with error handling
        try:
            assert self.cart_page.check_product_name(product_name), (
                f"Product '{product_name}' not found in cart after adding from '{source}'"
            )
            self.logger.info(f"Product '{product_name}' successfully verified in shopping cart")
        except AssertionError as e:
            screenshot_name = f"{source}_cart_validation_error.png"
            self.log_failure(
                screenshot_name,
                f"Cart validation failed – product '{product_name}' not found (source: {source})",
                e
            )

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

        # Step 2: Validate success message starts with expected text
        try:
            assert success_message.startswith(expected_start), "Success message does not start with expected text"
            self.logger.info(f"Success message starts with expected text: '{expected_start}'")

            # Step 3: Validate success message contains product name
            assert product_name in success_message, f"Success message does not contain product name '{product_name}'"
            self.logger.info(f"Success message contains correct product name: '{product_name}'")

        except AssertionError as e:
            screenshot_name = f"{source}_success_message_validation_error.png"
            self.log_failure(
                screenshot_name,
                f"Success message validation failed for product '{product_name}' (source: {source}) – {str(e)}",
                e
            )

    def add_to_cart_and_check(self, quantity):
        self.product_page.input_quantity(quantity)
        self.product_page.click_on_add_to_cart_button()

        try:
            element_result = self.product_page.get_success_message_box()
            if element_result is not None:
                self.logger.info("Success box has been successfully displayed")
            else:
                self.logger.warning("No success message box found after adding to cart")
        except Exception as e:
            self.logger.error(f"Failed to locate success message box: {e}")

        self.product_page.click_on_shopping_cart_link()

    def submit_review(self, product_name, reviewer_name, review_text, rating_value):
        # product_name = product_name
        # reviewer_name = reviewer_name
        # review_text = review_text

        self.logger.info(f"Test started: validating product review submission for '{product_name}'")

        # Step 1: Open product detail page
        self.search_for_product(product_name)
        self.open_product_detail(product_name)

        # Step 2: Fill out and submit review
        self.logger.info("Writing review...")
        self.product_page.click_reviews_button()
        self.product_page.input_name_reviewer(reviewer_name)
        self.product_page.input_review(review_text)
        self.product_page.select_radio_button_rating(rating_value)
        self.product_page.click_continue_button_reviews()
