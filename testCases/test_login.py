import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage
from pageObjects.homePage import HomePage

class Test_001_login:
    # base_URL = "https://awesomeqa.com/ui"
    # email = "username@gmail.de"
    # password = "admin"
    # invalid_email = "username@gmail123.de"
    # invalid_password = "admin123"
    # title = "My Account"
    # logger = LogGen.loggen()

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
        driver = setUp
        home_page = HomePage(driver)
        home_page.click_my_account()
        home_page.click_my_account_login()
        login_page = LoginPage(driver)
        login_page.input_eMail(email)
        login_page.input_password(password)
        login_page.click_login_button()
        current_title = driver.title
        print(login_page.check_error_message())
        print(current_title)
        # if current_title == self.title:
        if error == login_page.check_error_message() and current_title == title:
            assert True
        else:
            assert False

        driver.close()