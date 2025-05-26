from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
from utilities.locators.wishListPageLocators import WishListPageLocators


class WishListPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = WishListPageLocators

    def getNumberTotalOfRows(self):
        rows = self.wait_for_elements_visible(self.locators.numbers_of_rows)
        Trows = len(rows)
        return Trows

    def clickOnAddToCartIcon(self, currentProductName):
        for row in range(1, self.getNumberTotalOfRows() + 1):
            productName = self.driver.find_element(By.XPATH,
                                                   "//div[@class='table-responsive']//table//tbody//tr[" + str(
                                                       row) + "]//td[2]//a").text
            if productName == currentProductName:
                self.wait_for_element_visible(self.locators.add_to_cart_icon).click()

        return False

    def getShoppingCartHeaderIcon(self):
        return self.wait_for_element_visible(self.locators.shopping_cart_header_icon)

    def getLogoutButtonRightHandMenu(self):
        return self.wait_for_element_visible(self.locators.logout_right_hand_menu)

    def getpasswordButtonRightHandMenu(self):
        return self.wait_for_element_visible(self.locators.password_right_hand_menu)

    def clickOnShoppingCartHeaderIcon(self):
        self.getShoppingCartHeaderIcon().click()

    def clickOnLogoutButtonRightHandMenu(self):
        self.getLogoutButtonRightHandMenu().click()

    def clickOnpasswordRightHandMenu(self):
        self.getpasswordButtonRightHandMenu().click()
