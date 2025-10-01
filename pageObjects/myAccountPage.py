from base.base_driver import BaseDriver
from utilities.locators.myAccountPageLocators import MyAccountPageLocators


class MyAccountPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = MyAccountPageLocators

    def get_search_input_field(self):
        return self.wait_for_element_visible(self.locators.search_input_field)

    def get_search_button(self):
        return self.wait_for_element_visible(self.locators.search_button)

    def get_wishList_button(self):
        return self.wait_for_element_visible(self.locators.wish_list_button)

    def get_password_button(self):
        return self.wait_for_element_visible(self.locators.password_button)

    def get_success_message_password_text(self):
        success_message = self.wait_for_element_visible(self.locators.success_message_password_update).text
        return success_message

    def get_logout_right_hand_menu(self):
        list_elements = self.wait_for_elements_visible(self.locators.right_side_elements_MA)
        for list_element in list_elements:
            if list_element.text == "Logout":
                return list_element

    def input_search_element(self, element):
        self.get_search_input_field().clear()
        self.get_search_input_field().send_keys(element)

    def click_search_button(self):
        self.get_search_button().click()

    def click_wishList_button(self):
        self.get_wishList_button().click()

    def click_password_button(self):
        self.get_password_button().click()

    def click_logout_button(self):
        self.get_logout_right_hand_menu().click()

    def check_presence_of_title(self, title):
        return self.wait_for_title_to_be_visible(title)





