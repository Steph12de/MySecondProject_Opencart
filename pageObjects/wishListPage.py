from base.base_driver import Base_driver
from utilities.locators.wishListPageLocators import WishListPageLocators


class WishListPage(Base_driver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = WishListPageLocators

    def getAddToCartIcon(self):
        return self.wait_for_element_visible(self.locators.add_to_cart_icon)

    def getShoppingCartHeaderIcon(self):
        return self.wait_for_element_visible(self.locators.shopping_cart_header_icon)

    def clickOnAddToCartIcon(self):
        self.getAddToCartIcon().click()

    def clickOnShoppingCartHeaderIcon(self):
        self.getShoppingCartHeaderIcon().click()
