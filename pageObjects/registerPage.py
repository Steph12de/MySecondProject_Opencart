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

    def get_presence_warning_message_privacy_policy(self):
        element = self.wait_for_element_visible(self.locators.warning_message)
        return element is not None

    def get_presence_warning_message_first_name(self):
        return self.wait_text_to_be_present_in_element(self.locators.first_name_warning_message,
                                                       "First Name must be between 1 and 32 characters!"
                                                       )

    def get_presence_warning_message_last_name(self):
        return self.wait_text_to_be_present_in_element(self.locators.last_name_warning_message,
                                                       "Last Name must be between 1 and 32 characters!"
                                                       )

    def get_presence_warning_message_eMail(self):
        return self.wait_text_to_be_present_in_element(self.locators.eMail_warning_message,
                                                       "E-Mail Address does not appear to be valid!"
                                                       )

    def get_presence_warning_message_telephone(self):
        return self.wait_text_to_be_present_in_element(self.locators.telephone_warning_message,
                                                       "Telephone must be between 3 and 32 characters!"
                                                       )

    def get_presence_password_message_password(self):
        return self.wait_text_to_be_present_in_element(self.locators.password_warning_message,
                                                       "Password must be between 4 and 20 characters! test"
                                                       )

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

    def input_user_details(self, firstName, lastName, email, telephone, password, password_confirm):
        self.input_first_name(firstName)
        self.input_last_name(lastName)
        self.input_email(email)
        self.input_telephone_number(telephone)
        self.input_password(password)
        self.input_password_confirmation(password_confirm)

    def register_with_newsletter(self, firstName, lastName, email, telephone, password,
                                 password_confirm, newsletter=True, privacy=True):
        self.input_user_details(firstName, lastName, email, telephone, password, password_confirm)
        if newsletter:
            self.click_on_subscribe_button()
        else:
            self.click_on_unsubscribe_button()

        if privacy:
            self.click_on_privacy_checkBox()

        self.click_on_continue_button()

    def check_warning_message_privacy_policy(self):
        try:
            # self.logger.info("Checking presence of privacy policy warning message.")
            return self.get_presence_warning_message_privacy_policy()
        except Exception as e:
            # self.logger.error(f"Privacy policy warning message check failed: {e}")
            return False

    def check_warning_message_first_name(self):
        try:
            # self.logger.info("Checking presence of first name warning message.")
            return self.get_presence_warning_message_first_name()
        except Exception as e:
            # .logger.error(f"first name warning message check failed: {e}")
            return False

    def check_warning_message_last_name(self):
        try:
            # self.logger.info("Checking presence of last name warning message.")
            return self.get_presence_warning_message_last_name()
        except Exception as e:
            # self.logger.error(f"last name warning message check failed: {e}")
            return False

    def check_warning_message_eMail(self):
        try:
            # self.logger.info("Checking presence of eMail warning message.")
            return self.get_presence_warning_message_eMail()
        except Exception as e:
            # self.logger.error(f"eMail warning message check failed: {e}")
            return False

    def check_warning_message_telephone(self):
        try:
            # self.logger.info("Checking presence of telephone warning message.")
            return self.get_presence_warning_message_telephone()
        except Exception as e:
            # self.logger.error(f"telephone warning message check failed: {e}")
            return False

    def check_warning_message_password(self):
        try:
            # self.logger.info("Checking presence of password warning message.")
            return self.get_presence_password_message_password()
        except Exception as e:
            # self.logger.error(f"password warning message check failed: {e}")
            return False

    def check_warning_messages(self):
        return (self.check_warning_message_privacy_policy() and
                self.check_warning_message_first_name() and
                self.check_warning_message_last_name() and
                self.check_warning_message_eMail() and
                self.check_warning_message_telephone() and
                self.check_warning_message_password())
