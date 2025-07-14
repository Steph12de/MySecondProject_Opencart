from base.base_driver import BaseDriver
from utilities.custom_logger import LogGen
from utilities.locators.productinfoPageLocators import ProductInfoPageLocators


class ProductInfoPage(BaseDriver):
    # logger = LogGen.loggen()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = ProductInfoPageLocators

    def getAddToCartButton(self):
        return self.wait_for_element_visible(self.locators.addToCart_button)

    def waitUntilItemInCart(self, count):
        expected_text = f" {str(count)} item(s) - ${(count*122)}.00"
        try:
            self.wait_text_to_be_present_in_element(self.locators.black_item_button, expected_text)
        except:
            return False

    def getBlackItemButton(self):
        return self.wait_for_element_visible(self.locators.black_item_button)

    def getSuccessAddedMessage(self):
        return self.wait_text_to_be_present_in_element(self.locators.success_message, "Success: You have added")

    def getShoppingCartLink(self):
        return self.wait_for_element_visible(self.locators.shopping_cart_link)

    def get_quantity_input_field(self):
        return self.wait_for_element_visible(self.locators.quantity_input_field)

    def get_add_to_cart_display_page_button(self):
        return self.wait_for_element_visible(self.locators.add_to_cart_product_page)

    def get_product_name_text(self):
        return self.wait_for_element_visible(self.locators.product_name).text

    def get_product_brand_text(self):
        return self.wait_for_element_visible(self.locators.product_brand).text

    def get_product_code_text(self):
        return self.wait_for_element_visible(self.locators.product_code).text

    def split_product_code_text(self):
        return self.get_product_code_text().split(":")[-1].strip()

    def click_on_add_to_cart_button(self):
        self.getAddToCartButton().click()

    def click_on_black_item_button(self):
        self.getBlackItemButton().click()

    def check_success_message(self):
        try:
            return self.getSuccessAddedMessage()
        except:
            return False

    def click_on_shopping_cart_link(self):
        self.getShoppingCartLink().click()

    def input_quantity(self, quantity):
        self.get_quantity_input_field().clear()
        self.get_quantity_input_field().send_keys(quantity)

    def click_on_add_to_cart_display_page_button(self):
        self.get_add_to_cart_display_page_button().click()

