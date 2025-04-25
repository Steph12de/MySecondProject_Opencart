import unittest

import pytest

from pageObjects.loginPage import LoginPage
from pageObjects.homePage import HomePage
from pageObjects.forgottenPasswordPage import ForgottenPasswordPage
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

    # @pytest.mark.parametrize("email, password, title, error",
    #                          [
    #                              ("username@gmail.de", "admin", "My Account", False),
    #                              ("username@gmail123.de", "admin123", "Account Login", True),
    #                              ("username@gmail.de123", "admin", "Account Login", True),
    #                              ("username@gmail.de", "admin123", "Account Login", True),
    #                              ("", "", "Account Login", True),
    #                          ]
    #
    #                          )
    @pytest.mark.sanity
    @data(*Utils.read_data_from_excel("C:\\\\Python-Selenium\\QA-Automation-Learning\\MySecondProject_Opencart\\testdata\\testdataexcel.xlsx", "Tabelle1"))
    @unpack
    def test_login_with_multiple_combi(self, email, password, title, error):
        self.home_page.bring_me_to_login_page()
        self.login_page.log_me_in(email, password)
        current_title = self.driver.title
        actual_error = self.login_page.check_error_message()
        if error == str(actual_error) and current_title == title:
            assert True
        else:
            assert False

        self.driver.close()

    @pytest.mark.regression
    def test_presence_of_forgotten_password_text(self):
        self.logger.info("*****Check the presence of forgotten password text test is started*****")
        home_page = HomePage(self.driver)
        login_page_result = home_page.bring_me_to_login_page()
        fpassword_page_result = login_page_result.click_on_forgotten_password_text()
        if fpassword_page_result.check_presence_of_forgot_password_text():
            assert True
            self.logger.info("*******Forgotten Password Text Test is passed*********")
        else:
            self.logger.error("*******Forgotten Password Text Test is failed*********")
            assert False

        self.driver.close()

    @pytest.mark.regression
    def test_login_using_keyboard_keys(self):
        self.logger.info("*****Login using keyboard keys test is started*****")
        self.home_page.bring_me_to_login_page()
        self.login_page.log_me_in_using_keyboard("username@gmail.de", "admin")
        current_title = self.driver.title
        assert current_title == "My Account"
        self.driver.close()

    @pytest.mark.regression
    def test_existing_of_placeholder_text_in_email_password_field(self):
        self.logger.info("*****Checking existing of placeholder text test is started*****")
        if self.login_page.check_placeholder_text_in_email_field() and self.login_page.check_placeholder_text_in_password_field():
            assert True
            self.logger.info("*******The placeholder texts exist in the fields*********")
        else:
            self.logger.info("*******The placeholder texts aren't available in the fields*********")
            assert False

        self.driver.close()

    @pytest.mark.regression
    def test_password_text_is_hidden(self):
        self.logger.info("*****Checking visibility text of password test is started*****")
        self.home_page.bring_me_to_login_page()
        if self.login_page.check_visibility_of_password_text():
            assert True
            self.logger.info("*****The password is hidden*****")
        else:
            self.logger.info("*****The password isn't hidden*****")
            assert False

        self.driver.close()

