from base.base_driver import BaseDriver
from selenium.webdriver.common.keys import Keys
from utilities.locators.loginPageLocators import LoginPageLocators
from utilities.custom_logger import LogGen


class LoginPage(BaseDriver):

    # logger = LogGen.loggen()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.my_locators = LoginPageLocators

    def get_email_field(self):
        return self.wait_for_element_visible(self.my_locators.eMail)

    def get_password_field(self):
        return self.wait_for_element_visible(self.my_locators.password)

    def get_login_button(self):
        return self.wait_for_element_visible(self.my_locators.loginButton)

    def get_login_button_right_hand_menu(self):
        return self.wait_for_element_visible(self.my_locators.loginButtonRightHandMenu)

    def get_error_message_box(self):
        return self.wait_text_to_be_present_in_element(self.my_locators.login_error_message,
                                                       "Warning")

    # def get_error_text(self):
    #     return self.wait_for_element_visible(self.my_locators.login_error_message).text

    def get_forgotten_password_text(self):
        return self.wait_for_element_visible(self.my_locators.forgotten_password_text)

    def get_continue_button(self):
        return self.wait_for_element_visible(self.my_locators.continue_button)

    def input_eMail(self, email):
        self.get_email_field().clear()
        self.get_email_field().send_keys(email)

    def input_password(self, password):
        self.get_password_field().clear()
        self.get_password_field().send_keys(password)

    def click_login_button(self):
        self.get_login_button().click()

    def click_login_button_right_hand_menu(self):
        self.get_login_button_right_hand_menu().click()

    def click_on_continue_button(self):
        self.get_continue_button().click()

    def check_error_message(self):
        return self.get_error_message_box()

    def click_on_forgotten_password_text(self):
        self.get_forgotten_password_text().click()

    def log_me_in(self, email, password):
        self.input_eMail(email)
        self.input_password(password)
        self.click_login_button()

    def log_me_in_using_keyboard(self, email, password):
        self.input_eMail(email)
        self.get_email_field().send_keys(Keys.TAB)
        self.input_password(password)
        self.get_password_field().send_keys(Keys.TAB)
        self.get_login_button().send_keys(Keys.ENTER)

    def check_placeholder_text_in_email_field(self):
        if self.get_email_field().get_attribute("placeholder") == "E-Mail Address":
            return True
        else:
            return False

    def check_placeholder_text_in_password_field(self):
        if self.get_password_field().get_attribute("placeholder") == "Password":
            return True
        else:
            return False

    def check_visibility_of_password_text(self):
        if self.get_password_field().get_attribute("type") == "password":
            return True
        else:
            return False

    def select_option_right_hand_menu(self):
        elements = self.wait_for_elements_visible(self.my_locators.right_hand_menu_elements)
        for element in elements:
            if element.text == "Register":
                print(element.text)
                element.click()
                break
        return False
