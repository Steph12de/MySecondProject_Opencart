from base.base_driver import Base_driver
from utilities.custom_logger import LogGen
from utilities.locators.productinfoPageLocators import ProductInfoPageLocators


class ProductInfoPage(Base_driver):
    logger = LogGen.loggen()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = ProductInfoPageLocators

    def getAddtoCartButton(self):
        return self.wait_for_element_visible(self.locators.addToCart_button)

    def getItemButton(self, count):
        expected_text = count + " item"
        return self.wait_text_to_be_present_in_element(self.locators.item_button, expected_text)

    def getSuccessAddedMessage(self):
        return self.wait_text_to_be_present_in_element(self.locators.success_message, "Success: You have added")

    def getShoppingCartLink(self):
        return self.wait_for_element_visible(self.locators.shopping_cart_link)

    def click_on_add_to_cart_button(self):
        self.getAddtoCartButton().click()

    def click_on_item_button(self):
        self.getItemButton().click()

    def check_success_message(self):
        if self.getSuccessAddedMessage():
            self.logger.info("***The Message is displayed***")
            return True
        else:
            self.logger.error("***The Message isn't displayed***")
            return False

    def click_on_shopping_cart_link(self):
        self.getShoppingCartLink().click()




