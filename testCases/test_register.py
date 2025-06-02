import unittest
import mysql.connector

import pytest

from pageObjects.homePage import HomePage
from utilities.custom_logger import LogGen


class Test_001_Register(unittest.TestCase):
    logger = LogGen.loggen()

    @pytest.fixture(autouse=True)
    def class_setup(self, setUp):
        self.driver = setUp
        self.home_page = HomePage(self.driver)

    def test_register_via_my_account(self):
        self.home_page.bring_me_to_register_page()
        try:
            mydb = mysql.connector.connect(host="localhost", port="3306", user="root", password="MyPassword1234", database="mydb")
            cursor = mydb.cursor()
            cursor.execute("SELECT * FROM Registration")
        except:
            print("Connection unsuccessfully...")
