from base.base_driver import Base_driver
from utilities.locators.searchPageLocators import SearchPageLocators


class SearchPage(Base_driver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = SearchPageLocators

    def get_imac_image(self):
        return self.wait_for_element_visible(self.locators.imac_image)

    def click_on_imac_image(self):
        self.get_imac_image().click()
