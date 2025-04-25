import time

import pytest

from pageObjects.homePage import HomePage
from pageObjects.loginPage import LoginPage
from pageObjects.myAccountPage import MyAccountPage
from pageObjects.productInfoPage import ProductInfoPage
from pageObjects.searchPage import SearchPage
from pageObjects.shoppingCartPage import ShoppingCartPage
from utilities.custom_logger import LogGen
from ddt import ddt, data, unpack
import unittest


@ddt
class Test_002_addToCart(unittest.TestCase):
    logger = LogGen.loggen()

    @pytest.fixture(autouse=True)
    def class_setup(self, setUp):
        self.driver = setUp
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.myAccount_page = MyAccountPage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.product_page = ProductInfoPage(self.driver)

    @data(("username@gmail.de", "admin"))
    @unpack
    def test_add_to_cart_from_product_display(self, email, password):
        self.home_page.bring_me_to_login_page()
        self.login_page.log_me_in(email, password)
        self.myAccount_page.input_search_element("imac")
        self.myAccount_page.click_on_search_button()
        self.search_page.click_on_imac_image()
        self.product_page.click_on_add_to_cart_button()
        assert self.product_page.check_success_message() == True
        self.product_page.click_on_shopping_cart_link()
        cart_page = ShoppingCartPage(self.driver)
        assert cart_page.check_product_name() == True

        self.driver.close()
