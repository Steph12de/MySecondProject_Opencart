import os
import time
import unittest

import pytest

from pageObjects.loginPage import LoginPage
from pageObjects.homePage import HomePage
from pageObjects.forgottenPasswordPage import ForgottenPasswordPage
from pageObjects.myAccountPage import MyAccountPage
from pageObjects.wishListPage import WishListPage
from utilities.custom_logger import LogGen
from utilities.utils import Utils
from ddt import ddt, data, unpack


@ddt
class Test_001_login(unittest.TestCase):
    logger = LogGen.loggen()

    @pytest.fixture(autouse=True)
    def class_setup(self, setUp):
        self.driver = setUp
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.fpassword_page = ForgottenPasswordPage(self.driver)
        self.my_account = MyAccountPage(self.driver)
        self.wishlist = WishListPage(self.driver)

    @pytest.mark.sanity
    @data(*Utils.read_data_from_excel(
        "C:\\\\Python-Selenium\\QA-Automation-Learning\\MySecondProject_Opencart\\testdata\\testdataexcel.xlsx",
        "Tabelle1"))
    @unpack
    def test_login_with_multiple_combi(self, email, password, title, error):
        self.home_page.bring_me_to_login_page()
        self.logger.info("Starting login Test with multiple combination")
        self.login_page.log_me_in(email, password)
        current_title = self.driver.title
        actual_error = self.login_page.check_error_message()
        # print(type(actual_error))
        # print(type(error))
        try:
            assert error == str(actual_error) and current_title == title, (
                f"Login failed!\n"
                f"Expected error: {error}, but got: {actual_error}\n"
                f"Expected title: '{title}', but got: '{current_title}'"
            )
            self.logger.info(f"Login successful - Email: {email}, Expected Title: '{title}'")
        except AssertionError as e:
            self.logger.error(f"Test failed: {e}")
            self.driver.save_screenshot(".\\Screenshots\\login_error_screenshot.png")
            raise

        self.driver.quit()

    # @pytest.mark.regression
    def test_presence_of_forgotten_password_text(self):
        self.home_page.bring_me_to_login_page()
        self.login_page.click_on_forgotten_password_text()
        result_text = self.fpassword_page.check_presence_of_forgot_password_text()
        try:
            assert result_text is True, (
                f"Test failed: Expected forgotten password text to be present, but it was not found\n"
                f"Expected: True, Actual: {result_text}\n"
            )
            self.logger.info(f"Forgotten password text is displayed correctly.")
        except AssertionError as e:
            self.logger.error(f"Error Details: {e}")
            self.driver.save_screenshot(os.path.join(os.getcwd(), "forgot_password_error.png"))
            raise

        self.driver.close()

    # @pytest.mark.regression
    def test_login_using_keyboard_keys(self):
        self.home_page.bring_me_to_login_page()
        self.logger.info("Starting login Test using keyboard keys")
        self.login_page.log_me_in_using_keyboard("username@gmail.de", "admin")
        current_title = self.driver.title
        try:
            assert current_title == "My Account", (
                f"Login failed!\n"
                f"Expected page title: 'My Account', but got: '{current_title}'"
            )
            self.logger.info(f"Login successful - User redirected to '{current_title}'")
        except AssertionError as e:
            self.logger.error(
                f"Login test using keyboard keys failed!\n"
                f"Error details: {e}"
            )
            self.driver.save_screenshot(os.path.join(os.getcwd(), "login_error.png"))
            raise
        self.driver.close()

    #@pytest.mark.regression
    def test_existing_of_placeholder_text_in_email_password_field(self):
        self.home_page.bring_me_to_login_page()
        self.logger.info("Navigated to login page")
        self.logger.info("Starting the placeholder check test process ")
        placeholder_text_emailB = self.login_page.check_placeholder_text_in_email_field()
        placeholder_text_passwordB = self.login_page.check_placeholder_text_in_password_field()
        try:
            assert placeholder_text_emailB == True and placeholder_text_passwordB == True, (
                f"Test failed: Placeholder text is missing in one or both fields.\n"
                f"Expected placeholders to be present in both fields.\n"
                f"Expected: Email field Boolean value (True), but got: {placeholder_text_emailB}\n"
                f"Expected: Password field Boolean value (True), but got: {placeholder_text_passwordB}"
            )
            self.logger.info("Placeholder text is correctly displayed in both email and password fields.")
        except AssertionError as e:
            self.logger.error(
                f"Placeholder text validation failed!\n"
                f"Error details: {e}\n"
            )
            self.driver.save_screenshot(".\\Screenshots\\placeholderText.png")
            raise

        self.driver.close()

    #@pytest.mark.regression
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
                f"Password visibility test failed!\n"
                f"Error details: {e}"
            )
            raise
        self.driver.close()

    # @pytest.mark.regression
    @data(("username@gmail.de", "admin1"))
    @unpack
    def test_login_via_right_hand_menu(self, email, password):
        self.home_page.bring_me_to_login_page()
        self.login_page.click_login_button_right_hand_menu()
        self.login_page.log_me_in(email, password)
        current_title = self.driver.title
        try:
            assert current_title == "My Account", f"Test failed: User wasn't logged in, the title is wrong"
            self.logger.info("User logged successfully in by using login at the right-hand-menu")
        except AssertionError as e:
            self.logger.error(f"Login via right hand menu wasn't successfully: {e}. Actual Title: {current_title}")
            assert False

    @pytest.mark.regression
    @data(("username@gmail.de", "admin1"))
    @unpack
    def test_login_logout(self, email, password):
        self.home_page.bring_me_to_login_page()
        self.logger.info("Starting the Login and Logout test execution")
        self.login_page.click_login_button_right_hand_menu()
        self.login_page.log_me_in(email, password)
        current_title = self.driver.title
        try:
            assert current_title == "My Account", (
                f"Login failed!\n"
                f"Expected page title: 'My Account', but got: '{current_title}'"
            )
            self.logger.info(f"Login successful - User redirected to '{current_title}'")
        except AssertionError as e:
            self.logger.error(
                f"Login test was not successful!" "The login/logout test cannot be proceeded.\n"
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
                f"Logout failed!\n"
                f"Expected page title: 'My Account', but got: '{second_current_title}"
            )
            self.logger.info(f"Logout was successful as expected. Actual title: {second_current_title}.")
        except AssertionError as e:
            self.driver.save_screenshot(os.path.join(os.getcwd(), "logout.png"))
            self.logger.error(
                f"The logout functionality is not working as expected."
                f"Error details: {e} "
            )
            raise
        self.driver.close()

    @data(("username@gmail.de", "admin1"))
    @unpack
    def test_change_password_after_login(self, email, password):
        self.home_page.bring_me_to_login_page()
        self.logger.info("Starting the change password test after login.")
        self.login_page.log_me_in(email, password)
        current_title = self.driver.title
        try:
            assert current_title == "My Account", (
                f"Login failed!\n"
                f"Expected page title: 'My Account', but got: '{current_title}'"
            )
            self.logger.info(f"Login successful - User redirected to '{current_title}'")
        except AssertionError as e:
            self.logger.error(
                f"Login test was not successful!" "The change password after login test cannot be proceeded.\n"
                f"Error details: {e} "
            )
            raise
        self.my_account.clickOnPasswordButton()

