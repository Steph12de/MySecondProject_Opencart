import time

from selenium.webdriver import ActionChains

from utilities.locators.homePageLocators import HomePageLocators
from base.base_driver import BaseDriver
from utilities.custom_logger import LogGen
from selenium.webdriver.common.by import By


class HomePage(BaseDriver):
    #logger = LogGen.loggen()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = HomePageLocators

    def getMyAccountButtonHomePage(self):
        return self.wait_for_element_visible(self.locators.my_account_button)

    def getLoginButtonHomePage(self):
        return self.wait_for_element_visible(self.locators.my_account_login)

    def getDesktopsButton(self):
        return self.wait_for_element_visible(self.locators.desktop_button)
        #element  = self.wait_for_element_visible(self.locators.desktop_button)
        #return self.driver.find_element(By.XPATH, "//a[@class='dropdown-toggle' and text()='Desktops']")

    def getSearchInputField(self):
        return self.wait_for_element_visible(self.locators.search_input_field)

    def getWishListButton(self):
        return self.wait_for_element_visible(self.locators.wish_list_button)

    def getSearchButton(self):
        return self.wait_for_element_visible(self.locators.search_button)

    def getShowAllDesktopsButton(self):
        return self.wait_for_element_visible(self.locators.show_all_desktops_button)

    def click_my_account(self):
        self.getMyAccountButtonHomePage().click()

    def click_my_account_login_HomePage(self):
        self.getLoginButtonHomePage().click()

    def bring_me_to_login_page(self):
        self.click_my_account()
        self.click_my_account_login_HomePage()

    def go_to_desktops(self):
        action_chain = ActionChains(self.driver)
        action_chain.move_to_element(self.getDesktopsButton()).perform()
        self.logger.info("Move hover to Desktops")
        time.sleep(5)
        #print(self.getDesktopsButton().text)
        self.getShowAllDesktopsButton().click()
        time.sleep(3)
        #print(self.getShowAllDesktopsButton())

    def inputSearchElement(self, element):
        self.getSearchInputField().clear()
        self.getSearchInputField().send_keys(element)

    def clickOnWishListButton(self):
        self.getWishListButton().click()

    def clickOnSearchButton(self):
        self.getSearchButton().click()

