import time

import pytest

from pageObjects.homePage import HomePage
from pageObjects.loginPage import LoginPage
from pageObjects.myAccountPage import MyAccountPage
from pageObjects.productInfoPage import ProductInfoPage
from pageObjects.searchPage import SearchPage
from pageObjects.shoppingCartPage import ShoppingCartPage
from pageObjects.wishListPage import WishListPage
from utilities.custom_logger import LogGen
from ddt import ddt, data, unpack
import unittest

from utilities.readProperties import ReadConfig


@ddt
class Test_004_addToCart(unittest.TestCase):
    logger = LogGen.loggen()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()

    @pytest.fixture(autouse=True)
    def class_setup(self, setUp):
        self.driver = setUp
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.myAccount_page = MyAccountPage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.product_page = ProductInfoPage(self.driver)
        self.wishList_page = WishListPage(self.driver)
        self.cart_page = ShoppingCartPage(self.driver)

    # @pytest.mark.regression
    def test_add_to_cart_from_product_display(self):
        self.home_page.bring_me_to_login_page()
        self.login_page.log_me_in(self.email, self.password)
        self.myAccount_page.inputSearchElement("imac")
        self.myAccount_page.clickOnSearchButton()
        self.search_page.click_on_imac_image()
        self.product_page.click_on_add_to_cart_button()
        try:
            assert self.product_page.check_success_message() == True, "Test failed"
            self.logger.info("successful message is displayed")
        except AssertionError as e:
            self.logger.error(f"Test felgeschlagen: {e}")

        self.product_page.click_on_shopping_cart_link()
        time.sleep(10)
        try:
            assert self.cart_page.check_product_name("iMac") == True, "Test failed"
            self.logger.info("The product is successfully added")
        except AssertionError as e:
            self.logger.error(f"Test felgeschlagen: {e}")

        self.driver.close()

    # @pytest.mark.regression
    def test_add_product_to_wish_list(self):
        self.home_page.bring_me_to_login_page()
        self.login_page.log_me_in(self.email, self.password)
        self.myAccount_page.clickOnWishListButton()
        self.wishList_page.clickOnAddToCartIcon("Samsung SyncMaster 941BW")
        try:
            assert self.product_page.check_success_message() == True, "Test failed"
            self.logger.info("successful message is displayed")
        except AssertionError as e:
            self.logger.error(f"Test felgeschlagen: {e}")

        self.wishList_page.clickOnShoppingCartHeaderIcon()
        try:
            assert self.cart_page.check_product_name("Samsung SyncMaster 941BW") == True, "Test failed"
            self.logger.info("The product is successfully added")
        except AssertionError as e:
            self.logger.error(f"Test felgeschlagen: {e}")

        self.driver.close()

    @pytest.mark.regression
    def test_add_to_cart_from_desktops(self):
        self.home_page.go_to_desktops()
        self.driver.close()
