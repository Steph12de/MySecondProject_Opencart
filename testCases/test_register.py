import os.path
import random
import time
import unittest
import mysql.connector

import pytest

from pageObjects.accountCreatedPage import AccountCreatedPage
from pageObjects.homePage import HomePage
from pageObjects.loginPage import LoginPage
from pageObjects.registerPage import RegisterPage
from utilities.custom_logger import LogGen
from utilities.utils import Utils


class Test_001_Register(unittest.TestCase):
    logger = LogGen.loggen()

    @pytest.fixture(autouse=True)
    def class_setup(self, setUp):
        self.driver = setUp
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.register_page = RegisterPage(self.driver)
        self.created_page = AccountCreatedPage(self.driver)
        self.random_mail = Utils.random_email()

    @classmethod
    def setup_class(cls):
        try:
            cls.logger.info("Establishing database connection...")
            cls.mydb = (mysql.connector.connect
                        (host="localhost",
                         port="3306",
                         user="root",
                         password="MyPassword1234",
                         database="mydb")
                        )
            cls.cursor = cls.mydb.cursor(buffered=True)
            cls.logger.info("Database connection established successfully.")
        except mysql.connector.Error as e:
            cls.logger.error(f"Database connection failed: {e}")
            raise

    @classmethod
    def teardown_class(cls):
        if hasattr(cls, 'cursor') and hasattr(cls, 'mydb'):
            cls.cursor.close()
            cls.mydb.close()
            cls.logger.info("Database connection closed.")

    # @pytest.mark.skip(reason="Just skipped it right now")
    def test_registration_via_my_account(self):
        self.logger.info("Starting test: Register via 'My Account'")

        self.home_page.bring_me_to_register_page()
        self.logger.info("Navigated to the registration page.")

        self.logger.info("Fetching data from 'Registration' table.")
        self.cursor.execute("SELECT * FROM Registration")
        result = self.cursor.fetchone()

        if result:
            self.logger.info(f"Retrieved registration data: {result}")
            self.register_page.register_with_newsletter(result[1], result[2], self.random_mail, result[4],
                                                        result[5], result[6], newsletter=False
                                                        )
            self.logger.info("Registration process completed.")

            current_title = self.driver.title
            expected_title = "Your Account Has Been Created!"
            try:
                assert current_title == expected_title, (
                    f"Title mismatch: Expected '{expected_title}', but got '{current_title}'."
                )
                self.logger.info("Registration page test via 'My Account' passed.")
            except AssertionError as e:
                self.driver.save_screenshot(os.path.join(os.getcwd(), "Screenshots", "Registration_page_error.png"))
                self.logger.error(
                    "Registration via 'My Account' failed\n"
                    f"Error details: {e} "
                )
                raise

            # Proceed to the account page
            self.created_page.click_on_continue_button()
            self.logger.info("Redirecting to 'My Account' page.")

            # Verify account page title
            current_title = self.driver.title
            expected_title = "My Account"
            try:
                assert current_title == expected_title, (
                    f"Title mismatch: Expected '{expected_title}', but got '{current_title}'."
                )
                self.logger.info("My Account page test passed.")
            except AssertionError as e:
                self.driver.save_screenshot(os.path.join(os.getcwd(), "Screenshots", "My_Account_page_error.png"))
                self.logger.error(
                    "Account verification page failed\n"
                    f"Error details: {e} "
                )

                raise
        else:
            self.logger.warning("No registration data found in the database.")

        self.driver.close()

    # @pytest.mark.skip(reason="Just skipped it right now")
    def test_registration_via_new_customer(self):
        self.logger.info("Starting test: Registration via 'New Customer'")

        # Navigate to the login page
        self.home_page.open_login_page()
        self.logger.info("Navigated to the login page.")

        # Click on the 'Continue' button for new customer registration
        self.login_page.click_on_continue_button()
        self.logger.info("Proceeding with new customer registration.")

        # Retrieve registration data from the database
        self.logger.info("Fetching registration data for person_id=2 from 'Registration' table.")
        self.cursor.execute("SELECT * FROM Registration WHERE Person_id=2")
        result = self.cursor.fetchall()

        if result:
            result = result[0]
            self.logger.info(f"Retrieved registration data: {result}")

            # Perform registration process
            self.register_page.register_with_newsletter(
                result[1], result[2], self.random_mail, result[4],
                result[5], result[6], newsletter=False
            )
            self.logger.info("Registration process completed successfully.")

            current_title = self.driver.title
            expected_title = "Your Account Has Been Created!"
            try:
                assert current_title == expected_title, (
                    f"Title mismatch: Expected '{expected_title}', but got '{current_title}'."
                )
                self.logger.info("Registration page test via 'New Customer' passed.")
            except AssertionError as e:
                self.driver.save_screenshot(
                    os.path.join(os.getcwd(), "Screenshots", "RegistrationNewCustomer_page_error.png"))
                self.logger.error(
                    "Registration via 'My Account' failed\n"
                    f"Error details: {e} "
                )
                raise

            # Proceed to the account page
            self.created_page.click_on_continue_button()
            self.logger.info("Redirecting to 'My Account' page.")

            # Verify account page title
            current_title = self.driver.title
            expected_title = "My Account"
            try:
                assert current_title == expected_title, (
                    f"Title mismatch: Expected '{expected_title}', but got '{current_title}'."
                )
                self.logger.info("My Account page test passed.")
            except AssertionError as e:
                self.logger.error("Registration form validation failed: Expected warning messages were not displayed."
                                  "Account verification page failed\n"
                                  f"Error details: {e} "
                                  )
                raise
        else:
            self.logger.warning("No registration data found in the database.")

        self.driver.close()

    # @pytest.mark.skip(reason="Just skipped it right now")
    def test_registration_without_filling_form(self):
        self.logger.info("Starting test: Registration without filling in the form")

        self.home_page.open_login_page()
        self.logger.info("Navigated to the login page.")

        self.login_page.select_option_right_hand_menu()
        self.logger.info("Initiating registration via the 'Register' option.")

        self.cursor.execute("SELECT * FROM Registration WHERE person_id=3")
        result = self.cursor.fetchall()
        if result:
            result = result[0]
            self.register_page.register_with_newsletter(
                result[1], result[2], result[3], result[4],
                result[5], result[6], privacy=False
            )
            self.logger.info("Registration form submitted without filling in the form.")

            current_title = self.driver.title
            expected_title = "Register Account"
            try:
                assert (current_title == expected_title and self.register_page.check_warning_messages()), \
                    "Registration form validation failed: Expected warning messages were not displayed."
                self.logger.info("Registration validation passed: Warning messages appeared correctly.")
            except AssertionError as e:
                self.driver.save_screenshot(
                    os.path.join(os.getcwd(), "Screenshots", "RegistrationWithoutFillingForm_page_error.png"))
                self.logger.error("Registration validation failed: Expected warning messages were missing.")
                raise
        else:
            self.logger.warning("No registration data found in the database.")

        self.driver.close()

    # @pytest.mark.skip(reason="Just skipped it right now")
    def test_registration_with_different_password(self):
        self.logger.info("Starting test: Attempting registration with mismatched passwords")

        self.home_page.bring_me_to_register_page()
        self.logger.info("User navigated to the registration page.")

        self.logger.info("Retrieving user data from the 'Registration' table for test case.")
        self.cursor.execute("SELECT * FROM Registration WHERE person_id=4")
        result = self.cursor.fetchall()

        if result:
            result = result[0]
            self.register_page.register_with_newsletter(
                result[1], result[2], self.random_mail, result[4],
                result[5], result[6], newsletter=False
            )
            self.logger.info("Registration form submitted with mismatched passwords.")

            current_title = self.driver.title
            expected_title = "Register Account"
            try:
                assert (
                        current_title == expected_title and self.register_page.check_warning_message_confirm_password()), \
                    "Registration form validation failed: Expected warning messages were not displayed."
                self.logger.info("Validation successful: Password mismatch warning message appeared correctly.")
            except AssertionError as e:
                self.driver.save_screenshot(
                    os.path.join(os.getcwd(), "Screenshots", "RegistrationMismatchedPassword.png"))
                self.logger.error(f"Validation failed: Expected password confirmation warning message was missing.")
                raise
        else:
            self.logger.warning("No registration data found in the database.")

        self.driver.close()

    # @pytest.mark.skip(reason="Just skipped it right now")
    def test_registration_without_checking_privacy_policy(self):
        self.logger.info("Starting test: Attempting registration without accepting the privacy policy.")

        self.home_page.bring_me_to_register_page()
        self.logger.info("Navigated to the registration page.")

        self.logger.info("Retrieving user data from the 'Registration' table for test case.")
        self.cursor.execute("SELECT * FROM Registration WHERE First_name = 'Alexa' ")
        result = self.cursor.fetchall()

        if result:
            result = result[0]
            self.register_page.register_with_newsletter(
                result[1], result[2], self.random_mail, result[4],
                result[5], result[6], newsletter=False, privacy=False
            )
            self.logger.info("Registration form submitted without accepting privacy policy.")

            current_title = self.driver.title
            expected_title = "Register Account"
            try:
                self.assertEqual(
                    current_title,
                    expected_title,
                    f"Unexpected page title: expected '{expected_title}', but got '{current_title}'"
                )
                warning_displayed = self.register_page.check_warning_message_privacy_policy()
                self.assertTrue(
                    warning_displayed,
                    "Privacy policy warning message was expected but not displayed."
                )
                self.logger.info("Validation successful: Privacy policy warning appeared as expected.")

            except AssertionError as e:
                screenshot_name = "RegistrationPrivacy.png"
                screenshot_path = os.path.join(os.getcwd(), "Screenshots", screenshot_name)
                self.driver.save_screenshot(screenshot_path)
                self.logger.error(f"test failed: Screenshot saved at {screenshot_path}\n"
                                  f"Error details : {e}"
                                  )
                raise
        else:
            self.logger.warning("No registration data found in the database.")

        self.driver.close()

    # @pytest.mark.skip(reason="Just skipped it right now")
    def test_registration_with_existing_eMail(self):
        self.logger.info("Starting test: Attempting registration with an already registered email address.")

        self.home_page.bring_me_to_register_page()
        self.logger.info("Navigated to the registration page.")

        self.logger.info("Retrieving user data from the 'Registration' table for test case.")
        self.cursor.execute("SELECT * FROM Registration WHERE First_name = 'Stefanie' ")
        result = self.cursor.fetchall()

        if result:
            result = result[0]
            self.register_page.register_with_newsletter(
                result[1], result[2], result[3], result[4],
                result[5], result[6], newsletter=False
            )
            self.logger.info("Submitted registration form using an existing email address.")

            current_title = self.driver.title
            expected_title = "Register Account"
            try:
                self.assertEqual(
                    current_title,
                    expected_title,
                    f"Page title mismatch: expected '{expected_title}', but got '{current_title}'"
                )
                warning_displayed = self.register_page.check_warning_message_registered_eMail()
                self.assertTrue(
                    warning_displayed,
                    "Expected warning message for already registered email was not displayed."
                )
                self.logger.info("Validation passed: Duplicate email warning appeared as expected.")

            except AssertionError as e:
                screenshot_name = "registeredEmail.png"
                screenshot_path = os.path.join(os.getcwd(), "Screenshots", screenshot_name)
                self.driver.save_screenshot(screenshot_path)
                self.logger.error(f"Error details : {e}"
                                  f"test failed: Screenshot saved at {screenshot_path}\n"
                                  )
                raise
        else:
            self.logger.warning("No registration data found in the database.")

        self.driver.close()

    # @pytest.mark.skip(reason="Just skipped it right now")
    def test_registration_providing_invalid_telephone_number(self):
        self.logger.info("Starting test: Validate behavior when providing an invalid telephone number.")

        self.home_page.bring_me_to_register_page()
        self.logger.info("Navigated to the registration page.")

        self.logger.info("Retrieving user data from the 'Registration' table for test case.")
        self.cursor.execute("SELECT * FROM Registration WHERE First_name = 'Max' ")
        result = self.cursor.fetchall()

        if result:
            result = result[0]
            self.register_page.register_with_newsletter(
                result[1], result[2], self.random_mail, result[4],
                result[5], result[6], newsletter=False
            )
            self.logger.info("Registration form submitted with an invalid telephone number.")
            # time.sleep(4)

            current_title = self.driver.title
            expected_title = "Register Account"

            try:
                self.assertEqual(current_title, expected_title,
                                 f"Page title mismatch: expected '{expected_title}', but got '{current_title}'"
                                 )
                self.assertFalse(self.register_page.check_validity_telephone_number(),
                                 "Validation failed: The telephone number contains invalid characters, but no warning "
                                 "message appeared."
                                 )
                self.logger.info("Validation passed: Validation passed: Invalid telephone number was correctly "
                                 "detected and handled.")

            except AssertionError as e:
                screenshot_name = "Invalid_number.png"
                screenshot_path = os.path.join(os.getcwd(), "Screenshots", screenshot_name)
                self.driver.save_screenshot(screenshot_path)
                self.logger.error("Registration should have failed: Invalid telephone number was accepted without "
                                  "triggering validation."
                                  f"Error details : {e}"
                                  f"test failed: Screenshot saved at {screenshot_path}\n"
                                  )
                raise

        else:
            self.logger.warning("No registration data found in the database.")

        self.driver.close()
