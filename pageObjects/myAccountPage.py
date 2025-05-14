from base.base_driver import Base_driver
from utilities.locators.myAccountPageLocators import MyAccountPageLocators


class MyAccountPage(Base_driver):
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


    def inputSearchElement(self, element):
        self.getSearchInputField().clear()
        self.getSearchInputField().send_keys(element)

    def clickOnSearchButton(self):
        self.getSearchButton().click()

    def clickOnWishListButton(self):
        self.getWishListButton().click()




