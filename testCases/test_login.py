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
    @data(*Utils.read_data_from_excel("C:\\\\Python-Selenium\\QA-Automation-Learning\\MySecondProject_Opencart\\testdata\\testdataexcel.xlsx", "Tabelle1"))
    @unpack
    def test_login_with_multiple_combi(self, email, password, title, error):
        self.home_page.bring_me_to_login_page()
        self.logger.info("Starting login Test")
        self.login_page.log_me_in(email, password)
        current_title = self.driver.title
        actual_error = self.login_page.check_error_message()
        try:
            assert error == str(actual_error) and current_title == title, "Login failed!"
            self.logger.info("Login successful")
        except AssertionError as e:
            self.logger.error(f"Login Test: {e}")
            raise AssertionError

        self.driver.close()

    #@pytest.mark.regression
    def test_presence_of_forgotten_password_text(self):
        self.home_page.bring_me_to_login_page()
        self.login_page.click_on_forgotten_password_text()
        result_text = self.fpassword_page.check_presence_of_forgot_password_text()
        try:
            assert result_text == True, "Test failed"
            self.logger.info("Forgotten password Text is available")
        except AssertionError as e:
            self.logger.error(f"Check presence of forgotten password Text: {e}")

        self.driver.close()

    #@pytest.mark.regression
    def test_login_using_keyboard_keys(self):
        self.home_page.bring_me_to_login_page()
        self.login_page.log_me_in_using_keyboard("username@gmail.de", "admin")
        current_title = self.driver.title
        try:
           assert current_title == "My Account", "Test failed"
           self.logger.info("Login using keyboard key successful")
        except AssertionError as e:
            self.logger.error(f"Test using keyboard keys: {e}")
            raise AssertionError
        self.driver.close()

    #@pytest.mark.regression
    def test_existing_of_placeholder_text_in_email_password_field(self):
        self.home_page.bring_me_to_login_page()
        placeholder_text_emailB = self.login_page.check_placeholder_text_in_email_field()
        placeholder_text_passwordB = self.login_page.check_placeholder_text_in_password_field()
        try:
            assert placeholder_text_emailB == True and placeholder_text_passwordB == True, "Test failed"
            self.logger.info("Placeholder Text are available in the fields")
        except AssertionError as e:
            self.logger.error(f"Check presence of placeholder Text: {e}")

        self.driver.close()

    #@pytest.mark.regression
    def test_password_text_is_hidden(self):
        self.home_page.bring_me_to_login_page()
        password_visibility = self.login_page.check_visibility_of_password_text()
        try:
            assert password_visibility == True, "Test failed"
            self.logger.info("Password Text is hidden")
        except AssertionError as e:
            self.logger.error(f"Check visibility of password text: {e}" )

        self.driver.close()

    #@pytest.mark.regression
    @data(("username@gmail.de", "admin"))
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
        self.login_page.click_login_button_right_hand_menu()
        self.login_page.log_me_in(email, password)
        time.sleep(3)
        self.my_account.clickOnWishListButton()
        self.wishlist.clickOnLogoutButtonRightHandMenu()
        time.sleep(2)
        self.driver.back()
        self.wishlist.clickOnpasswordRightHandMenu()
        time.sleep(2)












