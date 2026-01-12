import os.path
import random
import time
import unittest
import mysql.connector

import pytest

from pageObjects.accountCreatedPage import AccountCreatedPage
from pageObjects.homePage import HomePage
from pageObjects.loginPage import LoginPage
from pageObjects.logoutPage import LogoutPage
from pageObjects.myAccountPage import MyAccountPage
from pageObjects.productInfoPage import ProductInfoPage
from pageObjects.registerPage import RegisterPage
from pageObjects.searchPage import SearchPage
from pageObjects.shoppingCartPage import ShoppingCartPage
from pageObjects.wishListPage import WishListPage
from utilities.custom_logger import LogGen
from utilities.helpers.helpers import Helpers
from utilities.utils import Utils
from utilities.helpers.database_helpers import DatabaseHelpers


@pytest.mark.usefixtures("db")
class Test_001_Register:
    logger = LogGen.loggen()

    @pytest.fixture(autouse=True)
    def class_setup(self, setUp):
        self.driver = setUp
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.register_page = RegisterPage(self.driver)
        self.created_page = AccountCreatedPage(self.driver)
        self.random_mail = Utils.random_email()
        self.database_helpers = DatabaseHelpers()
        self.myAccount_page = MyAccountPage(self.driver)
        self.wishList_page = WishListPage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.product_page = ProductInfoPage(self.driver)
        self.logout_page = LogoutPage(self.driver)
        self.cart_page = ShoppingCartPage(self.driver)
        self.helper = Helpers(self.driver, self.logger, self.home_page, self.login_page, self.myAccount_page,
                              self.wishList_page,
                              self.search_page, self.product_page, self.cart_page, self.logout_page)

    def validate_title(self, current_title, expected_title, page_name, screenshot_name):
        try:
            assert current_title == expected_title, (
                f"Expected title '{expected_title}', but got '{current_title}'."
            )
            self.logger.info(f"{page_name} validated successfully.")
        except AssertionError as e:
            self.helper.log_failure(screenshot_name,
                                    f"{page_name} validation failed.",
                                    f"Error details: {e}"
                                    )
            raise

    # @pytest.mark.skip(reason="Just skipped it right now")
    def test_registration_via_my_account(self):
        # Step 1: Navigate to registration page
        self.logger.info("Navigating to registration page via 'My Account'")
        self.home_page.bring_me_to_register_page()

        # Step 2: Fetch registration data from DB
        self.logger.info("Fetching registration data from database...")
        result = self.db.read_from_database("SELECT * FROM Registration")

        if not result:
            self.logger.warning("No registration data found in the database. Test skipped.")
            pytest.skip("Missing registration data for 'My Account' registration test.")

        self.logger.info(f"Registration data retrieved: {result}")

        # Step 3: Perform registration
        self.logger.info("Filling out registration form")
        self.register_page.register_with_newsletter(result[1], result[2], self.random_mail,
                                                    result[4], result[5], result[6], False)
        self.logger.info("Registration form submitted successfully.")

        # Step 4: Validate registration success page
        self.logger.info("Validating registration success page")
        self.validate_title(self.driver.title,
                            "Your Account Has Been Created!",
                            "Registration Success Page",
                            "Registration_my_account_success_error.png")

        # Step 5: Continue to account page
        self.logger.info("Navigating to 'My Account' page...")
        self.created_page.click_on_continue_button()

        # Step 6: Validate account page
        self.logger.info("Validating 'My Account' page")
        self.validate_title(self.driver.title,
                            "My Account",
                            "My Account Page",
                            "registration_my_account_page_error.png")

        self.logger.info("Registration via 'My Account' completed successfully.")

    # @pytest.mark.skip(reason="Just skipped it right now")
    def test_registration_via_new_customer(self):
        # Step 1: Navigate to login page
        self.logger.info("Navigating to login page for new customer registration...")
        self.home_page.open_login_page()

        # Step 2: Click on the 'Continue' button for new customer registration
        self.logger.info("Proceeding with new customer registration...")
        self.login_page.click_on_continue_button()

        # Step 3: Retrieve registration data from the database
        self.logger.info("Fetching registration data for Person_id=2...")
        result = self.db.read_from_database("SELECT * FROM Registration WHERE Person_id=2")

        if not result:
            self.logger.warning("No registration data found for Person_id=2.")
            pytest.skip("Missing registration data for new customer registration test.")

        self.logger.info(f"Registration data retrieved: {result}")

        # Step 4: Fill out registration form
        self.logger.info("Filling out registration form with retrieved data...")
        self.register_page.register_with_newsletter(
            result[1], result[2], self.random_mail, result[4],
            result[5], result[6], newsletter=False
        )
        self.logger.info("Registration process completed successfully.")

        # Step 5: Validate registration success page
        self.logger.info("Validating registration success page...")
        self.validate_title(self.driver.title,
                            "Your Account Has Been Created!",
                            "Registration Success Page",
                            "registration_new_customer_success_error.png")

        # Step 6: Continue to account page
        self.logger.info("Navigating to 'My Account' page...")
        self.created_page.click_on_continue_button()

        # Step 7: Validate 'My Account' page
        self.logger.info("Validating 'My Account' page...")
        self.validate_title(self.driver.title,
                            "My Account",
                            "My Account Page",
                            "registration_new_customer_my_account_error.png")

    # # @pytest.mark.skip(reason="Just skipped it right now")
    # def test_registration_without_filling_form(self):
    #     self.logger.info("Starting test: Registration without filling in the form")
    #
    #     self.home_page.open_login_page()
    #     self.logger.info("Navigated to the login page.")
    #
    #     self.login_page.select_option_right_hand_menu()
    #     self.logger.info("Initiating registration via the 'Register' option.")
    #
    #     self.cursor.execute("SELECT * FROM Registration WHERE person_id=3")
    #     result = self.cursor.fetchall()
    #     if result:
    #         result = result[0]
    #         self.register_page.register_with_newsletter(
    #             result[1], result[2], result[3], result[4],
    #             result[5], result[6], privacy=False
    #         )
    #         self.logger.info("Registration form submitted without filling in the form.")
    #
    #         current_title = self.driver.title
    #         expected_title = "Register Account"
    #         try:
    #             assert (current_title == expected_title and self.register_page.check_warning_messages()), \
    #                 "Registration form validation failed: Expected warning messages were not displayed."
    #             self.logger.info("Registration validation passed: Warning messages appeared correctly.")
    #         except AssertionError as e:
    #             self.driver.save_screenshot(
    #                 os.path.join(os.getcwd(), "Screenshots", "RegistrationWithoutFillingForm_page_error.png"))
    #             self.logger.error("Registration validation failed: Expected warning messages were missing.")
    #             raise
    #     else:
    #         self.logger.warning("No registration data found in the database.")
    #
    #     self.driver.close()
    #
    # # @pytest.mark.skip(reason="Just skipped it right now")
    # def test_registration_with_different_password(self):
    #     self.logger.info("Starting test: Attempting registration with mismatched passwords")
    #
    #     self.home_page.bring_me_to_register_page()
    #     self.logger.info("User navigated to the registration page.")
    #
    #     self.logger.info("Retrieving user data from the 'Registration' table for test case.")
    #     self.cursor.execute("SELECT * FROM Registration WHERE person_id=4")
    #     result = self.cursor.fetchall()
    #
    #     if result:
    #         result = result[0]
    #         self.register_page.register_with_newsletter(
    #             result[1], result[2], self.random_mail, result[4],
    #             result[5], result[6], newsletter=False
    #         )
    #         self.logger.info("Registration form submitted with mismatched passwords.")
    #
    #         current_title = self.driver.title
    #         expected_title = "Register Account"
    #         try:
    #             assert (
    #                     current_title == expected_title and self.register_page.check_warning_message_confirm_password()), \
    #                 "Registration form validation failed: Expected warning messages were not displayed."
    #             self.logger.info("Validation successful: Password mismatch warning message appeared correctly.")
    #         except AssertionError as e:
    #             self.driver.save_screenshot(
    #                 os.path.join(os.getcwd(), "Screenshots", "RegistrationMismatchedPassword.png"))
    #             self.logger.error(f"Validation failed: Expected password confirmation warning message was missing.")
    #             raise
    #     else:
    #         self.logger.warning("No registration data found in the database.")
    #
    #     self.driver.close()
    #
    # # @pytest.mark.skip(reason="Just skipped it right now")
    # def test_registration_without_checking_privacy_policy(self):
    #     self.logger.info("Starting test: Attempting registration without accepting the privacy policy.")
    #
    #     self.home_page.bring_me_to_register_page()
    #     self.logger.info("Navigated to the registration page.")
    #
    #     self.logger.info("Retrieving user data from the 'Registration' table for test case.")
    #     self.cursor.execute("SELECT * FROM Registration WHERE First_name = 'Alexa' ")
    #     result = self.cursor.fetchall()
    #
    #     if result:
    #         result = result[0]
    #         self.register_page.register_with_newsletter(
    #             result[1], result[2], self.random_mail, result[4],
    #             result[5], result[6], newsletter=False, privacy=False
    #         )
    #         self.logger.info("Registration form submitted without accepting privacy policy.")
    #
    #         current_title = self.driver.title
    #         expected_title = "Register Account"
    #         try:
    #             self.assertEqual(
    #                 current_title,
    #                 expected_title,
    #                 f"Unexpected page title: expected '{expected_title}', but got '{current_title}'"
    #             )
    #             warning_displayed = self.register_page.check_warning_message_privacy_policy()
    #             self.assertTrue(
    #                 warning_displayed,
    #                 "Privacy policy warning message was expected but not displayed."
    #             )
    #             self.logger.info("Validation successful: Privacy policy warning appeared as expected.")
    #
    #         except AssertionError as e:
    #             screenshot_name = "RegistrationPrivacy.png"
    #             screenshot_path = os.path.join(os.getcwd(), "Screenshots", screenshot_name)
    #             self.driver.save_screenshot(screenshot_path)
    #             self.logger.error(f"test failed: Screenshot saved at {screenshot_path}\n"
    #                               f"Error details : {e}"
    #                               )
    #             raise
    #     else:
    #         self.logger.warning("No registration data found in the database.")
    #
    #     self.driver.close()
    #
    # # @pytest.mark.skip(reason="Just skipped it right now")
    # def test_registration_with_existing_eMail(self):
    #     self.logger.info("Starting test: Attempting registration with an already registered email address.")
    #
    #     self.home_page.bring_me_to_register_page()
    #     self.logger.info("Navigated to the registration page.")
    #
    #     self.logger.info("Retrieving user data from the 'Registration' table for test case.")
    #     self.cursor.execute("SELECT * FROM Registration WHERE First_name = 'Stefanie' ")
    #     result = self.cursor.fetchall()
    #
    #     if result:
    #         result = result[0]
    #         self.register_page.register_with_newsletter(
    #             result[1], result[2], result[3], result[4],
    #             result[5], result[6], newsletter=False
    #         )
    #         self.logger.info("Submitted registration form using an existing email address.")
    #
    #         current_title = self.driver.title
    #         expected_title = "Register Account"
    #         try:
    #             self.assertEqual(
    #                 current_title,
    #                 expected_title,
    #                 f"Page title mismatch: expected '{expected_title}', but got '{current_title}'"
    #             )
    #             warning_displayed = self.register_page.check_warning_message_registered_eMail()
    #             self.assertTrue(
    #                 warning_displayed,
    #                 "Expected warning message for already registered email was not displayed."
    #             )
    #             self.logger.info("Validation passed: Duplicate email warning appeared as expected.")
    #
    #         except AssertionError as e:
    #             screenshot_name = "registeredEmail.png"
    #             screenshot_path = os.path.join(os.getcwd(), "Screenshots", screenshot_name)
    #             self.driver.save_screenshot(screenshot_path)
    #             self.logger.error(f"Error details : {e}"
    #                               f"test failed: Screenshot saved at {screenshot_path}\n"
    #                               )
    #             raise
    #     else:
    #         self.logger.warning("No registration data found in the database.")
    #
    #     self.driver.close()
    #
    # # @pytest.mark.skip(reason="Just skipped it right now")
    # def test_registration_providing_invalid_telephone_number(self):
    #     self.logger.info("Starting test: Validate behavior when providing an invalid telephone number.")
    #
    #     self.home_page.bring_me_to_register_page()
    #     self.logger.info("Navigated to the registration page.")
    #
    #     self.logger.info("Retrieving user data from the 'Registration' table for test case.")
    #     self.cursor.execute("SELECT * FROM Registration WHERE First_name = 'Max' ")
    #     result = self.cursor.fetchall()
    #
    #     if result:
    #         result = result[0]
    #         self.register_page.register_with_newsletter(
    #             result[1], result[2], self.random_mail, result[4],
    #             result[5], result[6], newsletter=False
    #         )
    #         self.logger.info("Registration form submitted with an invalid telephone number.")
    #         # time.sleep(4)
    #
    #         current_title = self.driver.title
    #         expected_title = "Register Account"
    #
    #         try:
    #             self.assertEqual(current_title, expected_title,
    #                              f"Page title mismatch: expected '{expected_title}', but got '{current_title}'"
    #                              )
    #             self.assertFalse(self.register_page.check_validity_telephone_number(),
    #                              "Validation failed: The telephone number contains invalid characters, but no warning "
    #                              "message appeared."
    #                              )
    #             self.logger.info("Validation passed: Validation passed: Invalid telephone number was correctly "
    #                              "detected and handled.")
    #
    #         except AssertionError as e:
    #             screenshot_name = "Invalid_number.png"
    #             screenshot_path = os.path.join(os.getcwd(), "Screenshots", screenshot_name)
    #             self.driver.save_screenshot(screenshot_path)
    #             self.logger.error("Registration should have failed: Invalid telephone number was accepted without "
    #                               "triggering validation."
    #                               f"Error details : {e}"
    #                               f"test failed: Screenshot saved at {screenshot_path}\n"
    #                               )
    #             raise
    #
    #     else:
    #         self.logger.warning("No registration data found in the database.")
    #
    #     self.driver.close()
