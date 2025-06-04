from base.base_driver import BaseDriver
from utilities.locators.accountCreatedPageLocators import AccountCreatedPageLocators


class AccountCreatedPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = AccountCreatedPageLocators

    def get_continue_button(self):
        return self.wait_for_element_visible(self.locators.continue_button)

    def click_on_continue_button(self):
        self.get_continue_button().click()