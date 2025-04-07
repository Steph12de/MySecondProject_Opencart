import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage
from pageObjects.homePage import HomePage


class Test_001_login:
    base_URL = "https://awesomeqa.com/ui"
    email = "username@gmail.de"
    password = "admin"
    invalid_email = "username@gmail123.de"
    invalid_password = "admin123"
    title = "My Account"

    def test_login_with_valid_credentials(self, setUp):
        driver = setUp
        driver.get(self.base_URL)
        driver.maximize_window()
        home_page = HomePage(driver)
        home_page.click_my_account()
        home_page.click_my_account_login()
        login_page = LoginPage(driver)
        login_page.input_eMail(self.email)
        login_page.input_password(self.password)
        login_page.click_login_button()
        current_title = driver.title
        if current_title == self.title:
            assert True
            driver.close()
        else:
            assert False

    def test_login_with_invalid_credentials(self, setUp):
        driver = setUp
        driver.get(self.base_URL)
        driver.maximize_window()
        home_page = HomePage(driver)
        home_page.click_my_account()
        home_page.click_my_account_login()
        login_page = LoginPage(driver)
        login_page.input_eMail(self.invalid_email)
        login_page.input_password(self.invalid_password)
        login_page.click_login_button()
        if login_page.check_error_message():
            assert True
            driver.close()
        else:
            assert False

    def test_login_with_invalid_email_(self, setUp):
        driver = setUp
        driver.get(self.base_URL)
        driver.maximize_window()
        home_page = HomePage(driver)
        home_page.click_my_account()
        home_page.click_my_account_login()
        login_page = LoginPage(driver)
        login_page.input_eMail(self.invalid_email)
        login_page.input_password(self.password)
        login_page.click_login_button()
        if login_page.check_error_message():
            assert True
            driver.close()
        else:
            assert False

    def test_login_with_invalid_password(self, setUp):
        driver = setUp
        driver.get(self.base_URL)
        driver.maximize_window()
        home_page = HomePage(driver)
        home_page.click_my_account()
        home_page.click_my_account_login()
        login_page = LoginPage(driver)
        login_page.input_eMail(self.email)
        login_page.input_password(self.invalid_password)
        login_page.click_login_button()
        if login_page.check_error_message():
            assert True
            driver.close()
        else:
            assert False
