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
        expected_text = f" {str(count)} item(s) - ${(count * 122)}.00"
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

    def get_date_picker_icon(self):
        return self.wait_for_element_visible(self.locators.calendar_date_picker_icon)

    def get_month_year_date_button(self):
        return self.wait_for_element_visible(self.locators.month_year_date_button)

    def get_left_arrow_button(self):
        return self.wait_for_element_visible(self.locators.left_arrow_button)

    def get_right_arrow_button(self):
        return self.wait_for_element_visible(self.locators.right_arrow_button)

    def get_calendar_days(self):
        return self.wait_for_elements_visible(self.locators.calendar_days)

    def get_calendar_time_picker_icon(self):
        return self.wait_for_element_visible(self.locators.calendar_time_picker_icon)

    def get_calendar_hour_box(self):
        return self.wait_for_element_visible(self.locators.calendar_hour_box)

    def get_calendar_minutes_box(self):
        return self.wait_for_element_visible(self.locators.calendar_minutes_box)

    def get_calendar_hour_arrow_button(self):
        return self.wait_for_element_visible(self.locators.calendar_hour_arrow_button)

    def get_calendar_minutes_arrow_button(self):
        return self.wait_for_element_visible(self.locators.calendar_minutes_arrow_button)

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
        script = """
        var input = document.getElementById('input-option222');
        input.setAttribute('type', 'file');
        """
        self.driver.execute_script(script)
        self.get_upload_file_button().send_keys(
            "C:\\Python-Selenium\\Software Testing_QA Atomation\\Manual Software Testing\\OpenCart -FRS.pdf")

    def choose_a_date(self):
        my_selected_day = "20"
        my_selected_month = "August"
        my_selected_year = "2010"
        self.get_date_picker_icon().click()
        while True:
            actual_date_year = self.get_month_year_date_button().text.split(" ")[-1].strip()
            actual_date_month = self.get_month_year_date_button().text.split(" ")[0].strip()
            if actual_date_month == my_selected_month and actual_date_year == my_selected_year:
                break
            else:
                self.get_right_arrow_button().click()
            # self.get_left_arrow_button().click()

        available_days = self.get_calendar_days()
        for day in available_days:
            if day.text == my_selected_day:
                day.click()
                break

    def choose_a_time(self):
        time_hour = "23"
        time_minutes = "00"
        self.get_calendar_time_picker_icon().click()
        while True:
            actual_hour = self.get_calendar_hour_box().text
            # actual_minutes = self.get_calendar_minutes_box().text
            if actual_hour == time_hour:
                break
            else:
              self.get_calendar_hour_arrow_button().click()

        while True:
            # actual_hour = self.get_calendar_hour_box().text
            actual_minutes = self.get_calendar_minutes_box().text
            if actual_minutes == time_minutes:
                break
            else:
              self.get_calendar_minutes_arrow_button().click()

    def fill_mandatory_fields_product_display(self):
        self.click_on_radio_button_medium()
        self.click_on_checkbox_three()
        self.input_text_in_text_field()
        self.select_checkbox_value_green()
        self.input_text_in_text_area()
        self.upload_file_()
        self.choose_a_date()
        self.choose_a_time()
