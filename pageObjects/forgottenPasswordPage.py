from utilities.locators.forgottenPasswordPageLocators import ForgottenPasswordPageLocators
from base.base_driver import BaseDriver


class ForgottenPasswordPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = ForgottenPasswordPageLocators

    def get_forgotten_password_heading(self):
        return self.wait_for_element_visible(self.locators.forgotten_password_text)

    # def check_forgotten_password_heading(self):
    #     return self.get_forgotten_password_heading()

    def get_forgotten_password_heading_text(self):
        return self.get_forgotten_password_heading().text
