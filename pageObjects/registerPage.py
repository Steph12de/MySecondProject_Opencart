from base.base_driver import BaseDriver
from utilities.locators.registerPageLocators import RegisterPageLocators


class RegisterPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = RegisterPageLocators

    def get_first_nameInput(self):
        return self.wait_for_element_visible(self.locators.first_name_input)

    def get_last_nameInput(self):
        return self.wait_for_element_visible(self.locators.last_name_input)

    def get_email_input(self):
        return self.wait_for_element_visible(self.locators.eMail_input)

    def get_telephone_input(self):
        return self.wait_for_element_visible(self.locators.telephone_input)

    def get_password_input(self):
        return self.wait_for_element_visible(self.locators.password_input)

    def get_password_confirmation(self):
        return self.wait_for_element_visible(self.locators.password_confirm_input)

    def get_subscribe_button(self):
        return self.wait_for_element_visible(self.locators.newsletter_subscribe)

    def get_unsubscribe_button(self):
        return self.wait_for_element_visible(self.locators.newsletter_unsubschribe)

    def get_privacy_checkBox(self):
        return self.wait_for_element_visible(self.locators.privacy_policy_check)

    def get_continue_button(self):
        return self.wait_for_element_visible(self.locators.continue_button)

    def input_first_name(self, firstName):
        self.get_first_nameInput().clear()
        self.get_first_nameInput().send_keys(firstName)

    def input_last_name(self, lastName):
        self.get_last_nameInput().clear()
        self.get_last_nameInput().send_keys(lastName)

    def input_telephone_number(self, number):
        self.get_telephone_input().clear()
        self.get_telephone_input().send_keys(number)

    def input_email(self, email):
        self.get_email_input().clear()
        self.get_email_input().send_keys(email)

    def input_password(self, password):
        self.get_password_input().clear()
        self.get_password_input().send_keys(password)

    def input_password_confirmation(self, password_confirm):
        self.get_password_confirmation().clear()
        self.get_password_confirmation().send_keys(password_confirm)

    def click_on_subscribe_button(self):
        self.get_subscribe_button().click()

    def click_on_unsubscribe_button(self):
        self.get_unsubscribe_button().click()

    def click_on_privacy_checkBox(self):
        return self.get_privacy_checkBox().click()

    def click_on_continue_button(self):
        self.get_continue_button().click()

    def register_without_newsletter(self, firstName, lastName, email, telephone, password, password_confirm):
        self.input_first_name(firstName)
        self.input_last_name(lastName)
        self.input_email(email)
        self.input_telephone_number(telephone)
        self.input_password(password)
        self.input_password_confirmation(password_confirm)
        self.click_on_unsubscribe_button()
        self.click_on_privacy_checkBox()
        self.click_on_continue_button()

    def register_with_newsletter(self, firstName, lastName, email, telephone, password, password_confirm):
        self.input_first_name(firstName)
        self.input_last_name(lastName)
        self.input_email(email)
        self.input_telephone_number(telephone)
        self.input_password(password)
        self.input_password_confirmation(password_confirm)
        self.click_on_subscribe_button()
        self.click_on_privacy_checkBox()
        self.click_on_continue_button()



