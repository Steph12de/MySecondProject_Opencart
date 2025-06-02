from base.base_driver import BaseDriver

from utilities.locators.comparisonPageLocators import ComparisonPageLocators


class ComparisonPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = ComparisonPageLocators

    def getNumberOfRows(self):
        Trows = len(self.wait_for_element_visible(self.locators.number_of_rows))
        return Trows

    def getAddToCartIpodClassic(self):
        if self.wait_for_element_visible(self.locators.add_to_cart_ipod_classic).get_attribute("href") == "https://awesomeqa.com/ui/index.php?route=product/compare&remove=40":
            self.wait_for_element_visible(self.locators.add_to_cart_ipod_classic).click()
        else:
            return False


