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

    # def get_product_table(self):
    #     element = self.wait_for_element_visible(self.locators.product_table)
    #     print(f"Element: {element}")
    #     return element is not None

    def get_bol_product_unavailability_text(self):
        return self.wait_text_to_be_present_in_element(self.locators.product_unavailability_text,
                                                       "You have not chosen any products to compare."
                                                       )

    def click_on_apple_music(self):
        self.wait_for_element_visible(self.locators.add_to_cart_apple_cinema).click()

    def get_add_to_cart_options(self):
            try:
                addToCardButtons = self.wait_for_elements_visible(self.locators.add_to_cart_buttons)
                for addToCardButton in addToCardButtons:
                    if addToCardButton.get_attribute(
                            "href") == "https://awesomeqa.com/ui/index.php?route=product/compare&remove=43":
                        addToCardButton.click()
                        break
            except Exception as e:
                return False



        # if (self.wait_for_element_visible(self.locators.add_to_cart_ipod_classic).get_attribute("href") ==
        #                              "https://awesomeqa.com/ui/index.php?route=product/compare&remove=40"):
        #     self.wait_for_element_visible(self.locators.add_to_cart_ipod_classic).click()
        # else:
        #     return False

    def get_success_message_text(self):
        success_message = self.wait_for_element_visible(self.locators.success_message_text)
        return success_message


    def get_shopping_card_link(self):
        return self.wait_for_element_visible(self.locators.shopping_cart_link)

    def click_on_shopping_card_link(self):
        self.get_shopping_card_link().click()
