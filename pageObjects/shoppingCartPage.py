from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
from utilities.locators.shoppingCartLocators import ShoppingCartLocators


class ShoppingCartPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = ShoppingCartLocators

    def getTableProductName(self):
        return self.wait_for_element_visible(self.locators.product_name)

    def getNumberTotalOfRows(self):
        rows = self.wait_for_elements_visible(self.locators.numbers_of_rows)
        Trows = len(rows)
        return Trows

    def get_warning_message_text(self):
        return self.wait_for_element_visible(self.locators.warning_message).text.split("\n")[0].strip()

    def check_product_name(self, currentProductName):
        # print(f"getNumberTotalOfRows: {self.getNumberTotalOfRows()}")
        for row in range(1, self.getNumberTotalOfRows() + 1):
            productName = self.driver.find_element(By.XPATH,
                                                   "//div[@class='table-responsive']//table//tbody//tr[" + str(
                                                       row) + "]//td[2]//a").text
            # print(f"expected name: {currentProductName} , actual name: {productName}")
            if productName == currentProductName:
                return True

        return False

    def check_presence_of_warning_message(self):
        return self.wait_for_element_located(self.locators.warning_message)
