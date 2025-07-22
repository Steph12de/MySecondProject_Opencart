from selenium.webdriver.support.select import Select

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

    def get_quantity_input_field_attribute(self):
        quantity_value = self.get_quantity_input_field().get_attribute("value")
        return quantity_value

    # def get_add_to_cart_display_page_button(self):
    #     return self.wait_for_element_visible(self.locators.add_to_cart_product_page)

    def get_product_name_text(self):
        return self.wait_for_element_visible(self.locators.product_name).text

    def get_product_brand_text(self):
        return self.wait_for_element_visible(self.locators.product_brand).text

    def get_product_code_text(self):
        return self.wait_for_element_visible(self.locators.product_code).text

    def get_success_message_text(self):
        success_message = self.wait_for_element_visible(self.locators.success_message).text
        return success_message

    def get_black_item_button_text(self):
        return self.wait_for_element_visible(self.locators.black_item_button_text).text

    def get_minimum_quantity_text(self):
        return self.wait_for_element_visible(self.locators.minimum_quantity_text_box).text

    def get_radio_button_medium(self):
        return self.wait_for_element_visible(self.locators.medium_radio)

    def get_checkbox_three(self):
        return self.wait_for_element_visible(self.locators.checkbox_three)

    def get_text_input_field(self):
        return self.wait_for_element_visible(self.locators.text_input_field)

    def get_dropdown_button(self):
        return self.wait_for_element_visible(self.locators.dropdown_button)

    def get_text_input_area(self):
        return self.wait_for_element_visible(self.locators.text_input_area)

    def get_upload_file_button(self):
        return self.wait_for_element_visible(self.locators.upload_file_button)

    def split_black_item_button_text(self):
        return self.get_black_item_button_text().split(" ")[0].strip()

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

    def increase_product_quantity(self, quantity):
        self.get_quantity_input_field().clear()
        self.get_quantity_input_field().send_keys(quantity)

    def click_on_radio_button_medium(self):
        self.get_radio_button_medium().click()

    def click_on_checkbox_three(self):
        self.get_checkbox_three().click()

    def input_text_in_text_field(self):
        self.get_text_input_field().clear()
        self.get_text_input_field().send_keys("This is a test")

    def select_checkbox_value_green(self):
        checkbox_values = Select(self.get_dropdown_button())
        checkbox_values.select_by_value("1")

    def input_text_in_text_area(self):
        self.get_text_input_area().clear()
        self.get_text_input_area().send_keys("You have to enter something in this text area")

    def upload_file_(self):
        self.get_upload_file_button().send_keys("C:\\Python-Selenium\\Software Testing_QA Atomation\\Manual Software Testing\\OpenCart -FRS.pdf")

    def fill_mandatory_fields_product_display(self):
        self.click_on_radio_button_medium()
        self.click_on_checkbox_three()
        self.input_text_in_text_field()
        self.select_checkbox_value_green()
        self.input_text_in_text_area()
        self.upload_file_()




