from base.base_driver import Base_driver
from utilities.locators.shoppingCartLocators import ShoppingCartLocators


class ShoppingCartPage(Base_driver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = ShoppingCartLocators

    def getTableProductName(self):
        return self.wait_for_element_visible(self.locators.product_name)

    def click_on_shopping_cart_link(self):
        self.getTableProductName().click()

    def check_product_name(self):
        if self.getTableProductName().text == "iMac":
            return True
        else:
            return False






    #     return self.wait_for_element_visible(self.locators.product_name)
    #
    # def click_on_product_name(self):
    #     self.getProductName().click()
    #
    # def check_product_name(self):
    #     if self.getProductName().text == "iMac":
    #         print(self.getProductName().text)
    #         return True
    #     else:
    #         return False
