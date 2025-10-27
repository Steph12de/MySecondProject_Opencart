from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
from utilities.locators.wishListPageLocators import WishListPageLocators


class WishListPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = WishListPageLocators

    def get_total_rows_number(self):
        rows = self.wait_for_elements_visible(self.locators.numbers_of_rows)
        Trows = len(rows)
        return Trows

    def click_add_to_cart_icon(self, current_product_name):
        for row in range(1, self.get_total_rows_number() + 1):
            product_name = self.driver.find_element(By.XPATH,
                                                   "//div[@class='table-responsive']//table//tbody//tr[" + str(
                                                       row) + "]//td[2]//a").text
            if product_name == current_product_name:
                self.wait_for_element_visible(self.locators.add_to_cart_icon).click()

        return False

    def get_shopping_cart_header_icon(self):
        return self.wait_for_element_visible(self.locators.shopping_cart_header_icon)

    def get_logout_button_right_hand_menu(self):
        return self.wait_for_element_visible(self.locators.logout_right_hand_menu)

    def get_password_button_right_hand_menu(self):
        return self.wait_for_element_visible(self.locators.password_right_hand_menu)

    def click_shopping_cart_header_icon(self):
        self.get_shopping_cart_header_icon().click()

    def click_logout_button_right_hand_menu(self):
        self.get_logout_button_right_hand_menu().click()

    def click_password_right_hand_menu(self):
        self.get_password_button_right_hand_menu().click()
