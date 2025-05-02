from selenium.webdriver.common.by import By

from base.base_driver import Base_driver
from utilities.locators.wishListPageLocators import WishListPageLocators


class WishListPage(Base_driver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = WishListPageLocators

    def getNumberTotalOfRows(self):
        Trows = len(self.locators.numbers_of_rows)
        return Trows

    def clickOnAddToCartIcon(self, currentProductName):
        for row in range(1, self.getNumberTotalOfRows() + 1):
            productName = self.driver.find_element(By.XPATH,
                                                   "//div[@class='table-responsive']//table//tbody//tr[" + str(
                                                       row) + "]//td[2]//a").text
            if productName == currentProductName:
                self.wait_for_element_visible(self.locators.add_to_cart_icon).click()
            break

    def getShoppingCartHeaderIcon(self):
        return self.wait_for_element_visible(self.locators.shopping_cart_header_icon)

    # def clickOnAddToCartIcon(self):
    #     self.getAddToCartIcon().click()

    def clickOnShoppingCartHeaderIcon(self):
        self.getShoppingCartHeaderIcon().click()
