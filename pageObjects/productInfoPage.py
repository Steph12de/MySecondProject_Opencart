from base.base_driver import Base_driver
from utilities.custom_logger import LogGen
from utilities.locators.productinfoPageLocators import ProductInfoPageLocators


class ProductInfoPage(Base_driver):
    logger = LogGen.loggen()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = ProductInfoPageLocators

    def get_add_to_cart_button(self):
        return self.wait_for_element_visible(self.locators.addToCart_button)

    def get_item_button(self, count):
        expected_text = count + " item"
        return self.wait_text_to_be_present_in_element(self.locators.item_button, expected_text)

    def get_success_added_message(self):
        return self.wait_text_to_be_present_in_element(self.locators.success_message, "Success: You have added")

    def click_on_add_to_cart_button(self):
        self.get_add_to_cart_button().click()

    def click_on_going_to_cart(self):
        self.get_item_button().click()

    def check_success_message(self):
        if self.get_success_added_message():
            return True
        else:
            return False




