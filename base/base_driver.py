from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.custom_logger import LogGen


class BaseDriver():
    def __init__(self, driver):
        self.driver = driver
        self.my_Wait = WebDriverWait(self.driver, 5)
        self.logger = LogGen.loggen()

    def wait_for_element_visible(self, locator):
        return self.my_Wait.until(EC.visibility_of_element_located(locator))

    def wait_text_to_be_present_in_element(self, locator, text):
        return self.my_Wait.until(EC.text_to_be_present_in_element(locator, text))

    def wait_for_element_located(self, locator):
        return self.my_Wait.until(EC.presence_of_element_located(locator))

    def wait_for_elements_visible(self, locator):
        return self.my_Wait.until(EC.visibility_of_all_elements_located(locator))


