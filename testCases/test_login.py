from selenium import webdriver
from pageObjects.loginPage import LoginPage

class Test_001_login:
    base_URL = "https://demo.opencart.com/"
    email = "username@gmail.de"
    password = "admin"

    def test_login_with_valid_credentials(self):
        driver = webdriver.Chrome()
        driver.get(self.base_URL)
        driver.maximize_window()
        login_page = LoginPage(driver)
        login_page.input_eMail(self.email)
        login_page.input_password(self.password)
        login_page.click_login_button()
