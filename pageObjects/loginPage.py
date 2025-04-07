from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.locators.loginPageLocators import LoginPageLocators

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.my_locators = LoginPageLocators

    def wait_for_element_visible(self, element):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element))

    def text_to_be_present_in_element(self, element, text):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(element))


    def input_eMail(self, email):
        self.wait_for_element_visible(self.my_locators.eMail).send_keys(email)

    def input_password(self, password):
        self.wait_for_element_visible(self.my_locators.password).send_keys(password)

    def click_login_button(self):
        self.wait_for_element_visible(self.my_locators.loginButton).click()

    def check_error_message(self):
         return self.text_to_be_present_in_element(self.my_locators.login_error_message, "Warning")

