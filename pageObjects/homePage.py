
from utilities.locators.homePageLocators import HomePageLocators
from base.base_driver import Base_driver

class HomePage(Base_driver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = HomePageLocators

    def getMyAccountButtonHomePage(self):
        return self.wait_for_element_visible(self.locators.my_account_button)

    def getLoginButtonHomePage(self):
        return self.wait_for_element_visible(self.locators.my_account_login)

    def click_my_account(self):
        self.getMyAccountButtonHomePage().click()

    def click_my_account_login_HomePage(self):
        self.getLoginButtonHomePage().click()

    def bring_me_to_login_page(self):
        self.click_my_account()
        self.click_my_account_login_HomePage()
