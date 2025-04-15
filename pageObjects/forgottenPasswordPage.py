from utilities.locators.forgottenPasswordPageLocators import ForgottenPasswordPageLocators
from base.base_driver import Base_driver


class ForgottenPasswordPage(Base_driver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = ForgottenPasswordPageLocators

    def getForgottenPasswordText(self):
        return self.wait_text_to_be_present_in_element(self.locators.forgotten_password_text, "Forgot Your Password?")

    def check_presence_of_forgot_password_text(self):
        try:
            return self.getForgottenPasswordText()
        except:
            return False
