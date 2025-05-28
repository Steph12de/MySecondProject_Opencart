from base.base_driver import BaseDriver
from utilities.locators.subcategoryDesktopsPageLocators import SubcategoryDesktopsPageLocators


class SubcategoryDesktopsPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = SubcategoryDesktopsPageLocators

    def getProductCompareLink(self):
        return self.wait_for_element_visible(self.locators.product_compare_button)

    def clickOnProductCompareLink(self):
        self.getProductCompareLink().click()
