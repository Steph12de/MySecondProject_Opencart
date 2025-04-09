import pytest
from pageObjects.loginPage import LoginPage
from pageObjects.homePage import HomePage
from pageObjects.forgottenPasswordPage import ForgottenPasswordPage

class Test_001_login:
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
        home_page.click_my_account()
        home_page.click_my_account_login()
        login_page = LoginPage(self.driver)
        login_page.input_eMail(email)
        login_page.input_password(password)
        login_page.click_login_button()
        current_title = self.driver.title
        if error == login_page.check_error_message() and current_title == title:
            assert True
        else:
            assert False

        self.driver.close()

    def test_presence_of_forgotten_password_text(self, setUp):
        self.driver = setUp
        home_page = HomePage(self.driver)
        home_page.click_my_account()
        home_page.click_my_account_login()
        login_page = LoginPage(self.driver)
        login_page.click_on_forgotten_password_text()
        fpassword_page = ForgottenPasswordPage(self.driver)
        if fpassword_page.check_presence_of_forgot_password_text():
            assert True
        else:
            assert False

        self.driver.close()
