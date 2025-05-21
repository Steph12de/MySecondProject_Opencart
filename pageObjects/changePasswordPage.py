from base.base_driver import BaseDriver
from utilities.locators.changePasswordLocators import ChangePasswordLocators


class ChangePasswordPage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = ChangePasswordLocators

    def getPasswordField(self):
        return self.wait_for_element_visible(self.locators.password_field)

    def getConfirmPasswordField(self):
        return self.wait_for_element_visible(self.locators.password_confirm_field)

    def getContinueButton(self):
        return self.wait_for_element_visible(self.locators.continue_button)

    def input_new_password(self, password):
        self.getPasswordField().send_keys(password)

    def input_confirm_new_password(self, password):
        self.getConfirmPasswordField().send_keys(password)

    def click_on_continue_button(self):
        self.getContinueButton().click()
