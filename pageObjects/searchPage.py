from base.base_driver import BaseDriver
from utilities.locators.searchPageLocators import SearchPageLocators


class SearchPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = SearchPageLocators

    def get_imac_image(self):
        return self.wait_for_element_visible(self.locators.imac_image)

    def get_add_to_cart_button(self):
        return self.wait_for_element_visible(self.locators.add_to_cart_button)

    def get_success_message_text(self):
        success_message_text = self.wait_for_element_visible(self.locators.success_message).text
        return success_message_text

    def get_apple_cinema_image(self):
        return self.wait_for_element_visible(self.locators.apple_cinema_image)

    def get_view_cart_button(self):
        return self.wait_for_element_visible(self.locators.view_cart_button)

    def get_black_cart_button(self):
        return self.wait_for_element_visible(self.locators.black_card_button)

    def get_card_total_text(self):
        try:
            element = self.wait_for_element_visible(self.locators.item_card_total)
            return element.text
        except Exception as e:
            return False

    def click_product_image(self):
        self.get_imac_image().click()

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()

    def click_black_card_button(self):
        self.get_black_cart_button().click()

    def click_view_cart_button(self):
        self.get_view_cart_button().click()

    def click_on_apple_cinema_image(self):
        self.get_apple_cinema_image().click()
