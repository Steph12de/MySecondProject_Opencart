from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.locators.loginPageLocators import LoginPageLocators

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.my_locators = LoginPageLocators

    def input_eMail(self, email):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.my_locators.eMail)).send_keys(email)

    def input_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.my_locators.password)).send_keys(password)

    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.my_locators.loginButton)).click()

