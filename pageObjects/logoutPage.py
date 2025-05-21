from base.base_driver import BaseDriver
from utilities.locators.logoutPageLocators import LogoutPageLocators


class LogoutPage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = LogoutPageLocators

    def getLoginButton(self):
        elements = self.wait_for_elements_visible(self.locators.right_side_elements_LO)
        for element in elements:
            if element.text == "Login":
                return element

    def clickOnLoginButton(self):
        self.getLoginButton().click()