import os
import time
import unittest

import pytest

from pageObjects.changePasswordPage import ChangePasswordPage
from pageObjects.loginPage import LoginPage
from pageObjects.homePage import HomePage
from pageObjects.forgottenPasswordPage import ForgottenPasswordPage
from pageObjects.logoutPage import LogoutPage
from pageObjects.myAccountPage import MyAccountPage
from pageObjects.productInfoPage import ProductInfoPage
from pageObjects.searchPage import SearchPage
from pageObjects.shoppingCartPage import ShoppingCartPage
from pageObjects.wishListPage import WishListPage
from utilities.custom_logger import LogGen
from utilities.helpers.helpers import Helpers
from utilities.readProperties import ReadConfig
from utilities.utils import Utils
from ddt import ddt, data, unpack


@ddt
class Test_002_login(unittest.TestCase):
    logger = LogGen.loggen()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    new_password = ReadConfig.getNewPassword()
    wrong_password = ReadConfig.getWrongPassword()

    @pytest.fixture(autouse=True)
    def class_setup(self, setUp):
        self.driver = setUp
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.myAccount_page = MyAccountPage(self.driver)
        self.fpassword_page = ForgottenPasswordPage(self.driver)
        self.my_account = MyAccountPage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.product_page = ProductInfoPage(self.driver)
        self.cart_page = ShoppingCartPage(self.driver)
        self.wishList_page = WishListPage(self.driver)
        self.change_password_page = ChangePasswordPage(self.driver)
        self.logout_page = LogoutPage(self.driver)
        self.helper = Helpers(self.driver, self.logger, self.home_page, self.login_page, self.myAccount_page,
                              self.wishList_page,
                              self.search_page, self.product_page, self.cart_page, self.logout_page)

    def tearDown(self):
        self.driver.quit()

    def submit_password_change(self, new_password, confirm_password, context=""):
        self.change_password_page.input_new_password(new_password)
        self.change_password_page.input_confirm_new_password(confirm_password)
        self.change_password_page.click_on_continue_button()
        self.logger.info(f"Submitted password change — {context}")

    @pytest.mark.skip(reason="Just skipped it right now")
    @pytest.mark.sanity
    @data(*Utils.read_data_from_excel(
        "C:\\\\Python-Selenium\\QA-Automation-Learning\\MySecondProject_Opencart\\testdata\\testdataexcel.xlsx",
        "Tabelle1"))
    @unpack
    def test_login_with_multiple_combi(self, email, password, expected_title, expected_error, test_case_label):
        self.logger.info(f"Starting login test: {test_case_label}")
        self.logger.info(f"Credentials — Email: '{email}', Password: '{password}'")

        # Step 1: Navigate to login page and perform login
        actual_title = self.helper.navigate_and_optional_login(email, password, expected_title, True)
        actual_error = str(self.login_page.check_error_message())
        print(self.login_page.get_error_text())

        # Step 2: Validate results
        try:
            self.helper.verify_login_successful(actual_title, expected_title)
            self.assertEqual(
                actual_error,
                expected_error,
                f"Error message mismatch:\nExpected: '{expected_error}'\nGot: '{actual_error}'"
            )
            self.logger.info(f"Login test passed: {test_case_label}")
        except AssertionError as error:
            self.helper.log_failure(
                f"login_failed_{test_case_label}.png",
                f"Login test failed — {test_case_label}\n"
                f"Expected Title: '{expected_title}'\nExpected Error: '{expected_error}'\n"
                f"Actual Title: '{actual_title}'\nActual Error: '{actual_error}'",
                error
            )

    # @pytest.mark.skip(reason="Just skipped it right now")
    # @pytest.mark.regression
    def test_presence_of_forgotten_password_link(self):
        self.logger.info("Test: Verify presence of 'Forgotten Password' text")

        # Step 1: Navigate to login page
        self.helper.navigate_and_optional_login(self.email, self.password)

        # Step 2: Click on 'Forgotten Password'
        self.login_page.click_forgotten_password_link()

        # Step 3: Check if the expected text is present
        heading_text = self.fpassword_page.get_forgotten_password_heading_text()
        expected_text = "Forgot Your Password?"

        self.logger.info(f"Retrieved heading text: '{heading_text}'")

        # Step 4: Validate heading text
        try:
            self.assertEqual(
                heading_text,
                expected_text,
                f"Heading text mismatch:\nExpected: '{expected_text}'\nGot: '{heading_text}'"
            )
            self.logger.info("Navigation via 'Forgotten Password' link successful — heading text verified.")
        except AssertionError as e:
            self.helper.navigate_and_optional_login(
                "forgotten_password_link_not_found.png",
                "'Forgotten Password' link failed — either navigation was incorrect or heading text is "
                "missing/mismatched.",
                e
            )

    # @pytest.mark.regression
    # @pytest.mark.skip(reason="Just skipped it right now")
    def test_login_using_keyboard_keys(self):
        self.logger.info("Test: Login using keyboard navigation")

        # Step 1: Define expected title
        expected_title = "My Account"

        # Step 2: Perform login using keyboard navigation
        actual_title = self.helper.navigate_and_optional_login(self.email, self.password, expected_title, True,
                                                               using_keyboard=True)

        # Step 3: Verify login success
        try:
            self.helper.verify_login_successful(actual_title, expected_title, "keyboard")
            self.logger.info(f"Login using keyboard successful — user redirected to '{actual_title}'")
        except AssertionError as error:
            self.helper.log_failure(
                "login_using_keyboard_failure.png",
                "Login test using keyboard keys failed — title mismatch.",
                error
            )

    # @pytest.mark.regression
    # @pytest.mark.skip(reason="Just skipped it right now")
    def test_existing_of_placeholder_text_in_email_password_field(self):
        self.logger.info("Test: Verify placeholder text in email and password fields")

        # Step 1: Navigate to login page
        self.helper.navigate_and_optional_login(self.email, self.password)

        # Step 2: Check placeholder presence
        email_has_placeholder = self.login_page.field_has_email_placeholder()
        password_has_placeholder = self.login_page.field_has_password_placeholder()

        self.logger.info(f"Email placeholder present: {email_has_placeholder}")
        self.logger.info(f"Password placeholder present: {password_has_placeholder}")

        # Step 3: Validate presence of placeholders in both fields
        try:
            self.assertTrue(
                email_has_placeholder,
                f"Email field placeholder is either missing or does not match the expected display."
            )
            self.assertTrue(
                password_has_placeholder,
                f"Password field placeholder is either missing or does not match the expected display."
            )
            self.logger.info("Placeholder text is correctly displayed in both fields.")
        except AssertionError as e:
            self.helper.log_failure(
                "placeholder_text_failure.png",
                f"Placeholder text validation failed in login fields.",
                e
            )

    # @pytest.mark.regression
    # @pytest.mark.skip(reason="Just skipped it right now")
    def test_password_field_is_masked(self):
        self.logger.info("Test: Verify that password input is masked")

        # Step 1: Navigate to login page
        self.helper.navigate_and_optional_login(self.email, self.password)

        # Step 2: Check if password field is masked (type='password')
        is_password_masked = self.login_page.is_password_field_masked()
        self.logger.info(f"password field masked: {is_password_masked}")

        # Step 3: Validate masking
        try:
            self.assertTrue(
                is_password_masked,
                "Password field is either visible or not properly masked (expected type='password').")
            self.logger.info("Password field is correctly masked.")
        except AssertionError as e:
            self.helper.log_failure(
                "password_visibility_error",
                "Password masking validation failed — field appears visible or incorrectly configured.",
                e
            )

    @pytest.mark.regression
    # @pytest.mark.skip(reason="Just skipped it right now")
    @data(("testmueller@gmail.de", "admin"))
    @unpack
    def test_login_via_right_hand_menu(self, email, password):
        self.logger.info("Test: Login via right-hand menu")

        # Step 1: Define expected title
        expected_title = "My Account"

        # Step 1: Navigate to login page
        actual_title = self.helper.navigate_and_optional_login(email, password, expected_title, True, True)

        # Step 3: Validate login success
        try:
            self.helper.verify_login_successful(actual_title, expected_title, "right_hand_menu")
        except AssertionError as error:
            self.helper.log_failure(
                "login_right_menu_error.png",
                "Login via right-hand menu failed — page title mismatch.",
                error)

    # @pytest.mark.regression
    # @pytest.mark.skip(reason="Just skipped it right now")
    def test_login_logout_flow(self):
        self.logger.info("Test: Full login/logout flow with access restriction check")

        # Step 1: Login
        expected_title = "My Account"
        actual_login_title = self.helper.navigate_and_optional_login(self.email, self.password, expected_title, True)

        try:
            self.helper.verify_login_successful(actual_login_title, expected_title)
        except AssertionError as error:
            self.helper.log_failure(
                "login_logout_error.png",
                "Login failed — page title mismatch.",
                error)

        # Step 2: Perform logout
        self.logger.info("Performing logout from user account")
        self.my_account.click_logout_button()

        # Step 3: Verify logout success
        try:
            expected_logout_title = "Account Logout"
            self.helper.verify_logout_successful(expected_logout_title)
        except AssertionError as error:
            self.helper.log_failure(
                "logout_error.png",
                "Logout failed — page title mismatch.",
                error)

        # Step 4: Attempt to access protected page after logout
        self.logger.info("Step 5: Attempting to access protected page (wishlist) after logout")
        self.driver.back()
        self.my_account.click_wishList_button()

        # Step 5: Verify redirection to login page
        try:
            expected_redirect_title = "Account Login"
            self.helper.verify_access_restriction_redirect(expected_redirect_title)
        except AssertionError as error:
            self.helper.log_failure(
                "access_restriction_error.png",
                "Access restriction after logout failed — user was not redirected to login page.",
                error)

    # @pytest.mark.regression
    # @pytest.mark.skip(reason="Just skipped it right now")
    def test_change_password_after_login(self):
        self.logger.info("Test: change password after logging")

        # Step 1: Define expected title after login
        expected_title = "My Account"

        # Step 2: Perform login and verify success
        actual_title = self.helper.navigate_and_optional_login(self.email, self.password, expected_title, True)

        try:
            self.helper.verify_login_successful(actual_title, expected_title)
        except AssertionError as error:
            self.helper.log_failure(
                "change_password_login_title_mismatch.png",
                "Login failed — page title mismatch.",
                error)

        # Step 3: Navigate to password page
        self.my_account.click_password_button()
        self.logger.info("Navigated to change password page")

        # Step 4: Submit new password
        self.submit_password_change(self.new_password, self.new_password, "matching passwords")

        # Step 5: Verify password change successful
        expected_success_message = "Success: Your password has been successfully updated."
        actual_success_message = self.my_account.get_success_message_password_text()
        self.my_account.check_presence_of_title(expected_title)
        title_after_password_change = self.driver.title

        try:
            self.assertEqual(
                title_after_password_change,
                expected_title,
                f"Title mismatch after password change - Expected Title: '{expected_title}'\nGot: '{title_after_password_change}'"
            )
            self.assertEqual(
                actual_success_message,
                expected_success_message,
                f"Password change message mismatch — expected: '{expected_success_message}'\nGot: '{actual_success_message}'"
            )
            self.logger.info("Password successfully changed — user redirected to 'My Account'")
        except AssertionError as error:
            self.helper.log_failure(
                "password_change_error.png",
                "Password change verification failed!",
                error
            )
        # Step 6: Perform logout and re-login
        self.logger.info("Logging out after password change")
        self.my_account.click_logout_button()

        # Step 7: Verify logout success

        try:
            expected_logout_title = "Account Logout"
            self.helper.verify_logout_successful(expected_logout_title)
        except AssertionError as error:
            self.helper.log_failure(
                "logout_after_password_change_error.png",
                "Logout failed — page title mismatch.",
                error)

        # Step 8: Re-login with new password
        self.logout_page.click_login_button()
        expected_title = "Account Login"
        actual_title = self.helper.navigate_and_optional_login(self.email, self.password,
                                                               expected_title, True)

        try:
            self.helper.verify_login_successful(actual_title, expected_title)
            self.logger.info("Access denied as expected — old password no longer valid after change")
        except AssertionError as error:
            self.helper.log_failure(
                "change_password_re-login_error.png",
                "Re-login after password change failed — page title mismatch.",
                f"Re-login with old password unexpectedly succeeded — user landed on '{actual_title}'",
            )

    # @pytest.mark.skip(reason="Just skipped it right now")
    def test_change_password_after_login_negative_test(self):
        self.logger.info("Negative Test: Attempt to change password with mismatched confirmation")

        # Step 1: Define expected title after login
        expected_title = "My Account"

        # Step 2: Perform login and verify success
        actual_title = self.helper.navigate_and_optional_login(self.email, self.password, expected_title, want_to_login=True)

        try:
            self.helper.verify_login_successful(actual_title, expected_title)
        except AssertionError as error:
            self.helper.log_failure(
                "change_password_negative_test_login_failure.png",
                "Login failed — page title mismatch.",
                error)

        # Step 3: Navigate to change password page
        self.my_account.click_password_button()
        self.logger.info("Navigated to change password page")

        # Step 4: Submit mismatched password confirmation
        self.submit_password_change(self.new_password, self.wrong_password, "mismatched confirmation")

        # Verify password change was rejected
        expected_error_message = "Password confirmation does not match password!"
        actual_error_message = self.change_password_page.getErrorMessage()

        expected_title_after_failure = "Change Password"
        self.my_account.check_presence_of_title(expected_title_after_failure)
        actual_title_after_failure = self.driver.title

        try:
            self.assertEqual(
                actual_title_after_failure,
                expected_title_after_failure,
                f"Unexpected redirect — expected to stay on '{expected_title_after_failure}', but landed on '{actual_title_after_failure}'"
            )
            self.assertEqual(
                actual_error_message,
                expected_error_message,
                f"Error message mismatch — expected: '{expected_error_message}', got: '{actual_error_message}'"
            )
            self.logger.info("Password change rejected as expected — error message displayed correctly")
        except AssertionError as error:
            self.helper.log_failure(
                "password_mismatch_error.png",
                "Negative password change test failed — mismatch not handled correctly",
                error
            )
