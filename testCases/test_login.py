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
from pageObjects.wishListPage import WishListPage
from utilities.custom_logger import LogGen
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
        self.fpassword_page = ForgottenPasswordPage(self.driver)
        self.my_account = MyAccountPage(self.driver)
        self.wishlist = WishListPage(self.driver)
        self.changePassword_page = ChangePasswordPage(self.driver)
        self.logout_page = LogoutPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def _log_failure(self, screenshot_name, message, exception):
        screenshot_path = os.path.join("screenshots", screenshot_name)
        self.driver.save_screenshot(screenshot_path)
        self.logger.error(f"{message}\n"
                          f"Screenshot saved at: {screenshot_path}\n"
                          f"Details: {exception}")
        raise exception

    @pytest.mark.sanity
    @data(*Utils.read_data_from_excel(
        "C:\\\\Python-Selenium\\QA-Automation-Learning\\MySecondProject_Opencart\\testdata\\testdataexcel.xlsx",
        "Tabelle1"))
    @unpack
    def test_login_with_multiple_combi(self, email, password, expected_title, expected_error):
        self.logger.info("Starting login test with data-driven combinations")
        self.logger.info(f"Credentials — Email: '{email}', Password: '{password}'")

        # Step 1: Navigate to login page
        self.home_page.bring_me_to_login_page()

        # Step 2: Perform login
        self.login_page.log_me_in(email, password)

        actual_title = self.driver.title
        print(f"Actual title: '{actual_title}'")
        print(f"Expected title: '{expected_title}")

        actual_error = str(self.login_page.check_error_message())

        # Step 4: Validate results
        try:
            self.assertEqual(
                actual_title,
                expected_title,
                f"Title mismatch:\n Expected: '{expected_title}'\nGot:'{actual_title}'"
            )
            self.assertEqual(
                actual_error,
                expected_error,
                f"Error message mismatch:\nExpected: '{expected_error}'\nGot: '{actual_error}'"
            )
            self.logger.info(f"Login test passed with expected title and error message.")
        except AssertionError as e:
            self._log_failure(
                "login_test_failure.png",
                "Login test failed — mismatch in title or error message.",
                e
            )

    @pytest.mark.skip(reason="Just skipped it right now")
    # @pytest.mark.regression
    def test_presence_of_forgotten_password_text(self):
        self.home_page.bring_me_to_login_page()
        self.login_page.click_on_forgotten_password_text()
        result_text = self.fpassword_page.check_presence_of_forgot_password_text()
        try:
            assert result_text is True, (
                "Test failed: Expected forgotten password text to be present, but it was not found\n"
                f"Expected: True, Actual: {result_text}\n"
            )
            self.logger.info("Forgotten password text is displayed correctly.")
        except AssertionError as e:
            self.logger.error(f"Error Details: {e}")
            self.driver.save_screenshot(os.path.join(os.getcwd(), "forgot_password_error.png"))
            raise

        self.driver.close()

    # @pytest.mark.regression
    @pytest.mark.skip(reason="Just skipped it right now")
    def test_login_using_keyboard_keys(self):
        self.home_page.bring_me_to_login_page()
        self.logger.info("Starting login Test using keyboard keys")
        self.login_page.log_me_in_using_keyboard("username@gmail.de", "admin")
        current_title = self.driver.title
        try:
            assert current_title == "My Account", (
                "Login failed!\n"
                f"Expected page title: 'My Account', but got: '{current_title}'"
            )
            self.logger.info(f"Login successful - User redirected to '{current_title}'")
        except AssertionError as e:
            self.logger.error(
                "Login test using keyboard keys failed!\n"
                f"Error details: {e}"
            )
            self.driver.save_screenshot(os.path.join(os.getcwd(), "login_error.png"))
            raise
        self.driver.close()

    # @pytest.mark.regression
    @pytest.mark.skip(reason="Just skipped it right now")
    def test_existing_of_placeholder_text_in_email_password_field(self):
        self.home_page.bring_me_to_login_page()
        self.logger.info("Navigated to login page")
        self.logger.info("Starting the placeholder check test process ")
        placeholder_text_emailB = self.login_page.check_placeholder_text_in_email_field()
        placeholder_text_passwordB = self.login_page.check_placeholder_text_in_password_field()
        try:
            assert placeholder_text_emailB == True and placeholder_text_passwordB == True, (
                "Test failed: Placeholder text is missing in one or both fields.\n"
                "Expected placeholders to be present in both fields.\n"
                f"Expected: Email field Boolean value (True), but got: {placeholder_text_emailB}\n"
                f"Expected: Password field Boolean value (True), but got: {placeholder_text_passwordB}"
            )
            self.logger.info("Placeholder text is correctly displayed in both email and password fields.")
        except AssertionError as e:
            self.logger.error(
                "Placeholder text validation failed!\n"
                f"Error details: {e}\n"
            )
            self.driver.save_screenshot(".\\Screenshots\\placeholderText.png")
            raise

        self.driver.close()

    # @pytest.mark.regression
    @pytest.mark.skip(reason="Just skipped it right now")
    def test_password_text_is_hidden(self):
        self.home_page.bring_me_to_login_page()
        self.logger.info("Navigated to login page")
        self.logger.info("Starting password visibility check test execution")
        password_visibility = self.login_page.check_visibility_of_password_text()
        try:
            assert password_visibility == True, (
                "Test failed: Password field is not hidden.\n"
                f"Expected: Hidden (True), but got: {password_visibility}"
            )
            self.logger.info("Password field is correctly masked.")
        except AssertionError as e:
            self.logger.error(
                "Password visibility test failed!\n"
                f"Error details: {e}"
            )
            raise
        self.driver.close()

    # @pytest.mark.regression
    @pytest.mark.skip(reason="Just skipped it right now")
    @data(("username@gmail.de", "admin1"))
    @unpack
    def test_login_via_right_hand_menu(self, email, password):
        self.home_page.bring_me_to_login_page()
        self.login_page.click_login_button_right_hand_menu()
        self.login_page.log_me_in(email, password)
        current_title = self.driver.title
        try:
            assert current_title == "My Account", "Test failed: User wasn't logged in, the title is wrong"
            self.logger.info("User logged successfully in by using login at the right-hand-menu")
        except AssertionError as e:
            self.logger.error(f"Login via right hand menu wasn't successfully: {e}. Actual Title: {current_title}")
            assert False

    # @pytest.mark.regression
    @pytest.mark.skip(reason="Just skipped it right now")
    def test_login_logout(self):
        self.home_page.bring_me_to_login_page()
        self.logger.info("Starting the Login and Logout test execution")
        self.login_page.click_login_button_right_hand_menu()
        self.login_page.log_me_in(self.email, self.password)
        current_title = self.driver.title

        try:
            assert current_title == "My Account", (
                "Login failed!\n"
                f"Expected page title: 'My Account', but got: '{current_title}'"
            )
            self.logger.info(f"Login successful - User redirected to '{current_title}'")
        except AssertionError as e:
            self.logger.error(
                "Login test was not successful!" "The login/logout test cannot be proceeded.\n"
                f"Error details: {e} "
            )
            raise

        self.my_account.clickOnWishListButton()
        self.wishlist.clickOnLogoutButtonRightHandMenu()
        time.sleep(2)
        self.driver.back()
        self.wishlist.clickOnpasswordRightHandMenu()
        second_current_title = self.driver.title

        try:
            assert second_current_title == "Account Login", (
                "Logout failed!\n"
                f"Expected page title: 'My Account', but got: '{second_current_title}"
            )
            self.logger.info(f"Logout was successful as expected. Actual title: {second_current_title}.")
        except AssertionError as e:
            self.driver.save_screenshot(os.path.join(os.getcwd(), "logout.png"))
            self.logger.error(
                "The logout functionality is not working as expected."
                f"Error details: {e} "
            )
            raise
        self.driver.close()

    # @pytest.mark.regression
    @pytest.mark.skip(reason="Just skipped it right now")
    def test_change_password_after_login(self):
        self.home_page.bring_me_to_login_page()
        self.logger.info("Starting the change password test after login.")
        self.login_page.log_me_in(self.email, self.password)
        current_title = self.driver.title
        try:
            assert current_title == "My Account", (
                "Login failed!\n"
                f"Expected page title: 'My Account', but got: '{current_title}'"
            )
            self.logger.info(f"Login successful - User redirected to '{current_title}'")
        except AssertionError as e:
            self.logger.error(
                "Login test was not successful!" "The change password after login test cannot be proceeded.\n"
                f"Error details: {e} "
            )
            raise
        self.my_account.clickOnPasswordButton()
        self.changePassword_page.input_new_password(self.new_password)
        self.changePassword_page.input_confirm_new_password(self.new_password)
        self.changePassword_page.click_on_continue_button()
        current_success_message = self.my_account.getSuccessMessagePasswordUpdate()
        success_message = "Success: Your password has been successfully updated."
        current_title = self.driver.title

        try:
            assert current_title == "My Account" and success_message in current_success_message, (
                "Password update validation failed!\n"
                f"Expected page title: 'My Account', but got: '{current_title}'\n"
                f"Expected error message: '{success_message}', Actual error message: '{self.my_account.getSuccessMessagePasswordUpdate()}'\n"
            )
            self.logger.info("Password change was successful. User is on 'My Account' page.")
        except AssertionError as e:
            self.logger.error(
                "Password change verification failed!\n"
                f"Error details: {e} "
            )
            raise

        self.logger.info("Proceeding with logout and re-login verification after password change.")
        self.my_account.clickOnLogoutButton()
        self.logout_page.clickOnLoginButton()
        self.login_page.log_me_in(self.email, self.password)
        current_title = self.driver.title
        expected_title = "Account Login"

        try:
            assert current_title == expected_title, (
                "Login verification failed!\n"
                f"Expected page title: '{expected_title}', but got: '{current_title}'"
            )
            self.logger.info(f"Test passed: Login unsuccessful as expected - User was not redirected to 'My Account'.")
        except AssertionError as e:
            self.driver.save_screenshot(os.path.join(os.getcwd(), "Screenshots", "passwordChangeLogin.png"))
            self.logger.error(
                "Unexpected login success despite incorrect password!\n"
                f"Error details: {e}"
            )
            raise
        self.driver.close()

    @pytest.mark.skip(reason="Just skipped it right now")
    def test_change_password_after_login_negative_test(self):
        self.home_page.bring_me_to_login_page()
        self.logger.info("Starting negative test for password change after login.")

        self.login_page.log_me_in(self.email, self.new_password)
        current_title = self.driver.title

        try:
            assert current_title == "My Account", (
                "Login failed!\n"
                f"Expected page title: 'My Account', but got: '{current_title}'"
            )
            self.logger.info(f"Login successful - User redirected to '{current_title}'")
        except AssertionError as e:
            self.logger.error(
                "Login test was not successful!" "The change password after login test cannot be proceeded.\n"
                f"Error details: {e} "
            )
            raise

        self.my_account.clickOnPasswordButton()
        self.changePassword_page.input_new_password(self.new_password)
        self.changePassword_page.input_confirm_new_password(self.wrong_password)
        self.changePassword_page.click_on_continue_button()

        actual_error_message = self.changePassword_page.getErrorMessage()
        expected_error_message = "Password confirmation does not match password!"
        current_title = self.driver.title
        expected_title = "Change Password"

        try:
            assert current_title == expected_title and expected_error_message in actual_error_message, (
                "Mismatch was not handled correctly.\n"
                f"Expected page title: '{expected_title}', but got: '{current_title}'.\n"
                #f"Expected error message: '{expected_error_message}', but received: '{actual_error_message}'."
            )
            self.logger.info(f"Test passed: Password mismatch correctly detected - Error message: '{actual_error_message}'.")
        except AssertionError as e:
            self.driver.save_screenshot(os.path.join(os.getcwd(), "Screenshots", "wrongpassword.png"))
            self.logger.error(
                "Negative test for password change failed!\n"
                f"Error details: {e} "
            )
            raise

        self.driver.close()
