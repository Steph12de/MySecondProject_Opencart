from base.base_driver import BaseDriver
from utilities.locators.productDisplayPageLocators import ProductDisplayPageLocators


class ProductDisplayPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = ProductDisplayPageLocators

    def get_quantity_input_field(self):
        return self.wait_for_element_visible(self.locators.quantity_input_field)

    def get_add_to_cart_display_page_button(self):
        return self.wait_for_element_visible(self.locators.add_to_cart_product_page)

    def input_quantity(self, quantity):
        self.get_quantity_input_field().clear()
        self.get_quantity_input_field().send_keys(quantity)

    def click_on_add_to_cart_display_page_button(self):
        self.get_add_to_cart_display_page_button().click()
