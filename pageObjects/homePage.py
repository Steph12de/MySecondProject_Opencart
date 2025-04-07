from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.locators.homePageLocators import HomePageLocators

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.locators = HomePageLocators
        self.my_wait = WebDriverWait(self.driver, 10)

    def wait_for_element_visible(self, element):
        return self.my_wait.until(EC.visibility_of_element_located(element))

    def click_my_account(self):
        self.wait_for_element_visible(self.locators.my_account_button).click()

    def click_my_account_login(self):
        self.wait_for_element_visible(self.locators.my_account_login).click()