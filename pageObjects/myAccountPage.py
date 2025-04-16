from base.base_driver import Base_driver
from utilities.locators.myAccountPageLocators import MyAccountPageLocators


class MyAccountPage(Base_driver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = MyAccountPageLocators

    def get_search_input_field(self):
        return self.wait_for_element_visible(self.locators.search_input_field)

    def get_search_button(self):
        return self.wait_for_element_visible(self.locators.search_button)

    def input_search_element(self, element):
        self.get_search_input_field().clear()
        self.get_search_input_field().send_keys(element)

    def click_on_search_button(self):
        self.get_search_button().click()


