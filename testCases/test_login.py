import pytest
from pageObjects.loginPage import LoginPage
from pageObjects.homePage import HomePage
from pageObjects.forgottenPasswordPage import ForgottenPasswordPage
from utilities.custom_logger import LogGen


class Test_001_login:

    logger = LogGen.loggen()
    @pytest.mark.parametrize("email, password, title, error",
                             [
                                 ("username@gmail.de", "admin", "My Account", False),
                                 ("username@gmail123.de", "admin123", "Account Login", True),
                                 ("username@gmail.de123", "admin", "Account Login", True),
                                 ("username@gmail.de", "admin123", "Account Login", True),
                                 ("", "", "Account Login", True),
                             ]
                             )
    def test_login_with_multiple_combi(self, setUp, email, password, title, error):
        self.driver = setUp
        home_page = HomePage(self.driver)
        home_page.bring_me_to_login_page()
        login_page = LoginPage(self.driver)
        login_page.log_me_in(email, password)
        current_title = self.driver.title
        if error == login_page.check_error_message() and current_title == title:
            assert True
        else:
            assert False

        self.driver.close()

    def test_presence_of_forgotten_password_text(self, setUp):
        self.logger.info("*****Check the presence of forgotten password text test is started*****")
        self.driver = setUp
        home_page = HomePage(self.driver)
        home_page.bring_me_to_login_page()
        login_page = LoginPage(self.driver)
        login_page.click_on_forgotten_password_text()
        fpassword_page = ForgottenPasswordPage(self.driver)
        if fpassword_page.check_presence_of_forgot_password_text():
            assert True
            self.logger.info("*******Forgotten Password Text Test is passed*********")
        else:
            self.logger.error("*******Forgotten Password Text Test is failed*********")
            assert False

        self.driver.close()

    def test_login_using_keyboard_keys(self, setUp):
        self.logger.info("*****Login using keyboard keys test is started*****")
        self.driver = setUp
        home_page = HomePage(self.driver)
        home_page.bring_me_to_login_page()
        login_page = LoginPage(self.driver)
        login_page.log_me_in_using_keyboard("username@gmail.de", "admin")
        current_title = self.driver.title
        if current_title == "My Account":
            assert True
            self.logger.info("*******The login test using keyboard keys is passed*********")
        else:
            self.logger.info("*******The login test using keyboard keys is failed*********")
            assert False

        self.driver.close()
