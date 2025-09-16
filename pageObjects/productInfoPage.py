from selenium.webdriver.support.select import Select

from base.base_driver import BaseDriver
from utilities.custom_logger import LogGen
from utilities.locators.productinfoPageLocators import ProductInfoPageLocators
from pynput.keyboard import Key, Controller
import time


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

    def get_success_message_box(self):
        element = self.wait_for_element_visible(self.locators.success_message)
        if element is not str:
            return True
        else:
            return False

    def getShoppingCartLink(self):
        return self.wait_for_element_to_be_clickable(self.locators.shopping_cart_link)

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
        return self.wait_for_element_visible(self.locators.button_upload_file)

    def get_date_picker_icon(self):
        return self.wait_for_element_visible(self.locators.calendar_date_picker_icon)

    def get_month_year_date_button(self):
        return self.wait_for_element_visible(self.locators.month_year_date_button)

    def get_right_arrow_button(self):
        return self.wait_for_element_visible(self.locators.right_arrow_button)

    def get_left_arrow_button(self):
        return self.wait_for_element_visible(self.locators.left_arrow_button)

    def get_calendar_days(self):
        return self.wait_for_elements_visible(self.locators.calendar_days)

    def get_calendar_time_picker_icon(self):
        return self.wait_for_element_visible(self.locators.calendar_time_picker_icon)

    def get_calendar_hour_box(self):
        return self.wait_for_element_visible(self.locators.calendar_hour_box)

    def get_calendar_minutes_box(self):
        return self.wait_for_element_visible(self.locators.calendar_minutes_box)

    def get_calendar_hour_arrow_button_up(self):
        return self.wait_for_element_visible(self.locators.calendar_hour_arrow_button_up)

    def get_calendar_minutes_arrow_button_up(self):
        return self.wait_for_element_visible(self.locators.calendar_minutes_arrow_button_up)

    def get_calendar_hour_arrow_button_down(self):
        return self.wait_for_element_visible(self.locators.calendar_hour_arrow_button_down)

    def get_calendar_minutes_arrow_button_down(self):
        return self.wait_for_element_visible(self.locators.calendar_minutes_arrow_button_down)

    def get_calendar_date_time_icon(self):
        return self.wait_for_element_visible(self.locators.calendar_date_time_icon)

    def get_date_time_month_year_button(self):
        return self.wait_for_element_visible(self.locators.date_time_month_year_button)

    def get_date_time_right_arrow_button(self):
        return self.wait_for_element_visible(self.locators.date_time_right_arrow_button)

    def get_date_time_left_arrow_button(self):
        return self.wait_for_element_visible(self.locators.date_time_left_arrow_button)

    def get_date_time_calendar_days(self):
        return self.wait_for_elements_visible(self.locators.date_time_calendar_days)

    def get_date_time_hour_button(self):
        return self.wait_for_element_visible(self.locators.date_time_hour_button)

    def get_date_time_hour_box(self):
        return self.wait_for_element_visible(self.locators.date_time_hour_box)

    def get_date_time_minutes_box(self):
        return self.wait_for_element_visible(self.locators.date_time_minutes_box)

    def get_date_time_hour_arrow_button_up(self):
        return self.wait_for_element_visible(self.locators.date_time_hour_arrow_button_up)

    def get_date_time_minutes_arrow_button_up(self):
        return self.wait_for_element_visible(self.locators.date_time_minutes_arrow_button_up)

    def get_date_time_hour_arrow_button_down(self):
        return self.wait_for_element_visible(self.locators.date_time_hour_arrow_button_down)

    def get_date_time_minutes_arrow_button_down(self):
        return self.wait_for_element_visible(self.locators.date_time_minutes_arrow_button_down)

    def get_reviews_button(self):
        return self.wait_for_element_visible(self.locators.reviews_button)

    def get_name_input_reviews(self):
        return self.wait_for_element_visible(self.locators.name_input_reviews)

    def get_review_message_box(self):
        return self.wait_for_element_visible(self.locators.reviews_message)

    def get_radio_button_reviews(self):
        return self.wait_for_elements_visible(self.locators.radio_buttons_reviews)

    def get_continue_button_reviews(self):
        return self.wait_for_element_visible(self.locators.continue_button_reviews)

    def get_success_message_reviews_text(self):
        return self.wait_for_element_visible(self.locators.success_message_reviews).text

    def get_warning_review_text_message(self):
        return self.wait_for_element_visible(self.locators.warning_review_text_message).text

    def get_warning_review_name_message(self):
        return self.wait_for_element_visible(self.locators.warning_review_name_message).text

    def scroll_element_into_shopping_link_view(self):
        print(type(self.locators.shopping_cart_link))
        self.scroll_element_into_view(self.locators.shopping_cart_link)

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
        scroll_position = self.scroll_at_the_top()
        while scroll_position != 0:
            # print(f"scroll position: {scroll_position}")
            scroll_position = self.scroll_at_the_top()

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
        self.get_upload_file_button().click()
        time.sleep(3)

        keyboard = Controller()
        keyboard.type("C:\\Test\\Test.pdf")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        self.wait_for_alert_to_be_present()
        self.driver.switch_to.alert.accept()

    def choose_calendar_date(self, day, month, year, get_icon, get_date_label, get_arrow_left, get_arrow_right,
                             get_day_elements):
        get_icon().click()

        while True:
            current_text = get_date_label().text
            actual_month, actual_year = current_text.split(" ")[0], current_text.split(" ")[-1]
            if actual_month == month and actual_year == year:
                break
            else:
                get_arrow_left().click()
            # get_arrow_right.click()

        for element in get_day_elements():
            if element.text == day:
                element.click()
                break

    def choose_time(self, hour, minutes, open_picker, get_hour, get_minute, hour_up, hour_down, minute_up, minute_down,
                    close_picker):
        open_picker().click()

        while True:
            actual_hour = get_hour().text
            if actual_hour > hour:
                hour_down().click()
            elif actual_hour < hour:
                hour_up().click()
            else:
                break

        while True:
            actual_minutes = get_minute().text
            if actual_minutes > minutes:
                minute_down().click()
            elif actual_minutes < minutes:
                minute_up().click()
            else:
                break

        close_picker().click()

    def choose_date_and_time(self, day, month, year,
                             date_icon, date_label, date_arrow_left, date_arrow_right, date_days,
                             hour, minute, time_icon, get_hour, get_minute,
                             hour_up, hour_down, minute_up, minute_down,
                             close_time_picker):
        # Choose date
        self.choose_calendar_date(
            day=day,
            month=month,
            year=year,
            get_icon=date_icon,
            get_date_label=date_label,
            get_arrow_left=date_arrow_left,
            get_arrow_right=date_arrow_right,
            get_day_elements=date_days
        )

        # Choose time
        self.choose_time(
            hour=hour,
            minutes=minute,
            open_picker=time_icon,
            get_hour=get_hour,
            get_minute=get_minute,
            hour_up=hour_up,
            hour_down=hour_down,
            minute_up=minute_up,
            minute_down=minute_down,
            close_picker=close_time_picker
        )

    def fill_mandatory_fields_product_display(self):
        self.click_on_radio_button_medium()
        self.click_on_checkbox_three()
        self.input_text_in_text_field()
        self.select_checkbox_value_green()
        self.input_text_in_text_area()
        self.upload_file_()
        self.choose_calendar_date(
            day="20",
            month="August",
            year="2010",
            get_icon=self.get_date_picker_icon,
            get_date_label=self.get_month_year_date_button,
            get_arrow_left=self.get_left_arrow_button,
            get_arrow_right=self.get_right_arrow_button,
            get_day_elements=self.get_calendar_days
        )
        self.choose_time(
            hour="23", minutes="00",
            open_picker=self.get_calendar_time_picker_icon,
            get_hour=self.get_calendar_hour_box,
            get_minute=self.get_calendar_minutes_box,
            hour_up=self.get_calendar_hour_arrow_button_up,
            hour_down=self.get_calendar_hour_arrow_button_down,
            minute_up=self.get_calendar_minutes_arrow_button_up,
            minute_down=self.get_calendar_minutes_arrow_button_down,
            close_picker=self.get_calendar_time_picker_icon
        )
        self.choose_date_and_time(
            day="1", month="February", year="2011",
            date_icon=self.get_calendar_date_time_icon,
            date_label=self.get_date_time_month_year_button,
            date_arrow_left=self.get_date_time_left_arrow_button,
            date_arrow_right=self.get_date_time_right_arrow_button,
            date_days=self.get_date_time_calendar_days,
            time_icon=self.get_date_time_hour_button,
            hour="20", minute="59",
            get_hour=self.get_date_time_hour_box,
            get_minute=self.get_date_time_minutes_box,
            hour_up=self.get_date_time_hour_arrow_button_up,
            hour_down=self.get_date_time_hour_arrow_button_down,
            minute_up=self.get_date_time_minutes_arrow_button_up,
            minute_down=self.get_date_time_minutes_arrow_button_down,
            close_time_picker=self.get_calendar_date_time_icon
        )

    def click_reviews_button(self):
        self.get_reviews_button().click()

    def input_name_reviewer(self, name):
        self.get_name_input_reviews().send_keys(name)

    def input_review(self, message):
        self.get_review_message_box().send_keys(message)

    def select_radio_button_rating(self):
        ratings = self.get_radio_button_reviews()
        for rating in ratings:
            if rating.get_attribute("value") == str(4):
                rating.click()

    def click_continue_button_reviews(self):
        self.get_continue_button_reviews().click()
