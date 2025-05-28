from base.base_driver import BaseDriver
from utilities.locators.searchPageLocators import SearchPageLocators


class SearchPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = SearchPageLocators

    def getImacImage(self):
        return self.wait_for_element_visible(self.locators.imac_image)

    def getAddToCartButton(self):
        return self.wait_for_element_visible(self.locators.add_to_cart_button)

    def getSuccessMessageText(self):
        success_message_text = self.wait_for_element_visible(self.locators.success_message).text
        return success_message_text

    def getViewCartButton(self):
        return self.wait_for_element_visible(self.locators.view_cart_button)

    def getBlackCartButton(self):
        return self.wait_for_element_visible(self.locators.black_card_button)

    def getCardTotalText(self):
        try:
            element = self.wait_for_element_visible(self.locators.item_card_total)
            return element.text
        except Exception as e:
            return False

    def clickOnImacImage(self):
        self.getImacImage().click()

    def clickOnAddToCartButton(self):
        self.getAddToCartButton().click()

    def clickOnBlackCardButton(self):
        self.getBlackCartButton().click()

    def clickOnViewCartButton(self):
        self.getViewCartButton().click()
