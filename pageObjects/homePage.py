import time

from selenium.webdriver import ActionChains

from utilities.locators.homePageLocators import HomePageLocators
from base.base_driver import BaseDriver
from utilities.custom_logger import LogGen


class HomePage(BaseDriver):
    # logger = LogGen.loggen()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = HomePageLocators

    def get_my_account_button_homePage(self):
        return self.wait_for_element_visible(self.locators.my_account_button)

    def get_login_button_home_page(self):
        return self.wait_for_element_visible(self.locators.my_account_login)

    def get_register_button_home_page(self):
        return self.wait_for_element_visible(self.locators.my_account_register)

    def get_desktops_button(self):
        return self.wait_for_element_visible(self.locators.desktop_button)

    def get_search_input_field(self):
        return self.wait_for_element_visible(self.locators.search_input_field)

    def get_wish_list_button(self):
        return self.wait_for_element_visible(self.locators.wish_list_button)

    def get_search_button(self):
        return self.wait_for_element_visible(self.locators.search_button)

    def get_show_all_desktops_button(self):
        return self.wait_for_element_visible(self.locators.show_all_desktops_button)

    def click_my_account(self):
        self.get_my_account_button_homePage().click()

    def click_my_account_login_HomePage(self):
        self.get_login_button_home_page().click()

    def click_my_account_register_homePage(self):
        self.get_register_button_home_page().click()

    def open_login_page(self):
        self.click_my_account()
        self.click_my_account_login_HomePage()

    def bring_me_to_register_page(self):
        self.click_my_account()
        self.click_my_account_register_homePage()

    def go_to_desktops(self):
        action_chain = ActionChains(self.driver)
        action_chain.move_to_element(self.get_desktops_button()).perform()
        # time.sleep(2)
        # print(self.getDesktopsButton().text)
        self.get_show_all_desktops_button().click()

    def inputSearchElement(self, element):
        self.get_search_input_field().clear()
        self.get_search_input_field().send_keys(element)

    def clickOnWishListButton(self):
        self.get_wish_list_button().click()

    def clickOnSearchButton(self):
        self.get_search_button().click()
