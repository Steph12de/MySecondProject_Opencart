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

    @pytest.mark.skip(reason="Just skipped it right now")
    @pytest.mark.sanity
    @data(*Utils.read_data_from_excel(
        "C:\\\\Python-Selenium\\QA-Automation-Learning\\MySecondProject_Opencart\\testdata\\testdataexcel.xlsx",
        "Tabelle1"))
    @unpack
    def test_login_with_multiple_combi(self, email, password, expected_title, expected_error):
        self.logger.info("Starting login test with data-driven combinations")
        self.logger.info(f"Credentials — Email: '{email}', Password: '{password}'")

        # Step 1: Navigate to login page
        self.home_page.open_login_page()

        # Step 2: Perform login
        self.login_page.log_me_in(email, password)
        self.login_page.check_presence_of_title(expected_title)
        actual_title = self.driver.title

        self.logger.info(f"Actual title: '{actual_title}'")
        self.logger.info(f"Expected title: '{expected_title}")

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
    def test_presence_of_forgotten_password_link(self):
        self.logger.info("Test: Verify presence of 'Forgotten Password' text")

        # Step 1: Navigate to login page
        self.home_page.open_login_page()

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
            self._log_failure(
                "forgot_password_error.png",
                "'Forgotten Password' link failed — either navigation was incorrect or heading text is "
                "missing/mismatched.",
                e
            )

    # @pytest.mark.regression
    @pytest.mark.skip(reason="Just skipped it right now")
    def test_login_using_keyboard_keys(self):
        self.logger.info("Test: Login using keyboard navigation")

        # Step 1: Navigate to login page
        self.home_page.open_login_page()

        # Step 2: Perform login using keyboard keys
        email = "username@gmail.de"
        password = "admin"
        self.login_page.log_me_in_using_keyboard(email, password)

        # Step 3: Verify page title after login
        expected_title = "My Account"
        self.login_page.check_presence_of_title(expected_title)
        actual_title = self.driver.title

        self.logger.info(f"Verifying page title after login: '{actual_title}'")

        try:
            self.assertEqual(
                actual_title,
                expected_title,
                f"Login using keyboard failed\nExpected title: '{expected_title}'\nGot: '{actual_title}'"
            )
            self.logger.info(f"Login using keyboard successful — user redirected to '{actual_title}'")
        except AssertionError as error:
            self._log_failure(
                "login_using_keyboard_failure.png",
                "Login test using keyboard keys failed — title mismatch.",
                error
            )

    # @pytest.mark.regression
    # @pytest.mark.skip(reason="Just skipped it right now")
    def test_existing_of_placeholder_text_in_email_password_field(self):
        self.logger.info("Test: Verify placeholder text in email and password fields")

        # Step 1: Navigate to login page
        self.home_page.open_login_page()

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
            self._log_failure(
                "placeholder_text_failure.png",
                f"Placeholder text validation failed in login fields.",
                e
            )

    # @pytest.mark.regression
    @pytest.mark.skip(reason="Just skipped it right now")
    def test_password_text_is_hidden(self):
        self.home_page.open_login_page()
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
        self.home_page.open_login_page()
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
        self.home_page.open_login_page()
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
        self.home_page.open_login_page()
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
        self.home_page.open_login_page()
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
                # f"Expected error message: '{expected_error_message}', but received: '{actual_error_message}'."
            )
            self.logger.info(
                f"Test passed: Password mismatch correctly detected - Error message: '{actual_error_message}'.")
        except AssertionError as e:
            self.driver.save_screenshot(os.path.join(os.getcwd(), "Screenshots", "wrongpassword.png"))
            self.logger.error(
                "Negative test for password change failed!\n"
                f"Error details: {e} "
            )
            raise

        self.driver.close()
