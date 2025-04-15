from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import WebDriverWait
from base.base_driver import Base_driver
from selenium.webdriver.common.keys import Keys
from utilities.locators.loginPageLocators import LoginPageLocators


class LoginPage(Base_driver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.my_locators = LoginPageLocators

    def getEmailField(self):
        return self.wait_for_element_visible(self.my_locators.eMail)

    def getPasswordField(self):
        return self.wait_for_element_visible(self.my_locators.password)

    def getLoginButton(self):
        return self.wait_for_element_visible(self.my_locators.loginButton)

    def getErrorMessageBox(self):
        return self.wait_text_to_be_present_in_element(self.my_locators.login_error_message, "Warning")

    def getForgottenPasswordText(self):
        return self.wait_for_element_visible(self.my_locators.forgotten_password_text)

    def input_eMail(self, email):
        self.getEmailField().clear()
        self.getEmailField().send_keys(email)

    def input_password(self, password):
        self.getPasswordField().clear()
        self.getPasswordField().send_keys(password)

    def click_login_button(self):
        self.getLoginButton().click()

    def check_error_message(self):
        try:
            return self.getErrorMessageBox()
        except:
            return False

    def click_on_forgotten_password_text(self):
        self.getForgottenPasswordText().click()

    def log_me_in(self, email, password):
        self.input_eMail(email)
        self.input_password(password)
        self.click_login_button()

    def log_me_in_using_keyboard(self, email, password):
        self.input_eMail(email)
        self.getEmailField().send_keys(Keys.TAB)
        self.input_password(password)
        self.getPasswordField().send_keys(Keys.TAB)
        self.getLoginButton().send_keys(Keys.ENTER)