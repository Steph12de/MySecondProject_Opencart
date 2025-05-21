from base.base_driver import BaseDriver
from utilities.locators.myAccountPageLocators import MyAccountPageLocators


class MyAccountPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = MyAccountPageLocators

    def getSearchInputField(self):
        return self.wait_for_element_visible(self.locators.search_input_field)

    def getSearchButton(self):
        return self.wait_for_element_visible(self.locators.search_button)

    def getWishListButton(self):
        return self.wait_for_element_visible(self.locators.wish_list_button)

    def getPasswordButton(self):
        return self.wait_for_element_visible(self.locators.password_button)

    def getSuccessMessagePasswordUpdate(self):
        success_message = self.wait_for_element_visible(self.locators.success_message_password_update).text
        return success_message

    def getLogoutRightHandMenu(self):
        list_elements = self.wait_for_elements_visible(self.locators.right_side_elements_MA)
        for list_element in list_elements:
            if list_element.text == "Logout":
                return list_element

    def inputSearchElement(self, element):
        self.getSearchInputField().clear()
        self.getSearchInputField().send_keys(element)

    def clickOnSearchButton(self):
        self.getSearchButton().click()

    def clickOnWishListButton(self):
        self.getWishListButton().click()

    def clickOnPasswordButton(self):
        self.getPasswordButton().click()

    def clickOnLogoutButton(self):
        self.getLogoutRightHandMenu().click()





