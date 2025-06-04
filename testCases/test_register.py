import os.path
import random
import time
import unittest
import mysql.connector

import pytest

from pageObjects.accountCreatedPage import AccountCreatedPage
from pageObjects.homePage import HomePage
from pageObjects.registerPage import RegisterPage
from utilities.custom_logger import LogGen
from utilities.utils import Utils


class Test_001_Register(unittest.TestCase):
    logger = LogGen.loggen()
    random_mail = Utils.random_email()

    @pytest.fixture(autouse=True)
    def class_setup(self, setUp):
        self.driver = setUp
        self.home_page = HomePage(self.driver)
        self.register_page = RegisterPage(self.driver)
        self.created_page = AccountCreatedPage(self.driver)

    @classmethod
    def setup_class(cls):
        try:
            cls.logger.info("🔄 Establishing database connection...")
            cls.mydb = (mysql.connector.connect
                        (host="localhost",
                         port="3306",
                         user="root",
                         password="MyPassword1234",
                         database="mydb")
                        )
            cls.cursor = cls.mydb.cursor()
            cls.logger.info("✅ Database connection established successfully.")
        except mysql.connector.Error as e:
            cls.logger.error(f"❌ Database connection failed: {e}")
            raise

    @classmethod
    def teardown_class(cls):
        if hasattr(cls, 'cursor') and hasattr(cls, 'mydb'):
            cls.cursor.close()
            cls.mydb.close()
            cls.logger.info("🔄 Database connection closed.")

    def test_register_via_my_account(self):
        self.logger.info("🔄 Starting test: Register via 'My Account'")

        self.home_page.bring_me_to_register_page()
        self.logger.info("✅ Navigated to the registration page.")

        self.logger.info("🔍 Fetching data from 'Registration' table.")
        self.cursor.execute("SELECT * FROM Registration")
        result = self.cursor.fetchone()

        if result:
            self.logger.info(f"✅ Retrieved registration data: {result}")
            self.register_page.register_without_newsletter(result[1], result[2], self.random_mail, result[4],
                                                           result[5], result[6]
            )
            self.logger.info("✅ Registration process completed.")

            current_title = self.driver.title
            expected_title = "Your Account Has Been Created!"
            try:
                assert current_title == expected_title, (
                    f"❌ Title mismatch: Expected '{expected_title}', but got '{current_title}'."
                )
                self.logger.info("✅ Registration page test passed.")
            except AssertionError as e:
                self.driver.save_screenshot(os.path.join(os.getcwd(), "Screenshots", "Registration_page_error.png"))
                self.logger.error(
                    "Registration via 'My Account' failed\n"
                    f"Error details: {e} "
                )
                raise

            # Proceed to the account page
            self.created_page.click_on_continue_button()
            self.logger.info("🔄 Redirecting to 'My Account' page.")

            # Verify account page title
            current_title = self.driver.title
            expected_title = "My Account"
            try:
                assert current_title == expected_title, (
                    f"❌ Title mismatch: Expected '{expected_title}', but got '{current_title}'."
                )
                self.logger.info("✅ My Account page test passed.")
            except AssertionError as e:
                self.driver.save_screenshot(os.path.join(os.getcwd(), "Screenshots", "My_Account_page_error.png"))
                self.logger.error(
                    "Account verification page failed\n"
                    f"Error details: {e} "
                )
                raise
        else:
            self.logger.warning("⚠️ No registration data found in the database.")

        self.driver.close()