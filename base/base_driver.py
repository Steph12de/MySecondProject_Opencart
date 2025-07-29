from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions

from utilities.custom_logger import LogGen


class BaseDriver():
    def __init__(self, driver):
        self.driver = driver
        self.my_Wait = WebDriverWait(self.driver, 5)
        # self.logger = LogGen.loggen()

    def wait_for_element_visible(self, locator):
        try:
            return self.my_Wait.until(EC.visibility_of_element_located(locator))
        except Exception as e:
            return "Element not visible"
            #raise Exception("Element not visible")

    def wait_text_to_be_present_in_element(self, locator, text):
        try:
            return self.my_Wait.until(EC.text_to_be_present_in_element(locator, text))
        except Exception as e:
            return False

    def wait_for_element_located(self, locator):
        try:
            return self.my_Wait.until(EC.presence_of_element_located(locator))
        except Exception as e:
            return False

    def wait_for_elements_visible(self, locator):
        try:
            return self.my_Wait.until(EC.visibility_of_all_elements_located(locator))
        except Exception as e:
            return "Elements not visible"

    def wait_for_alert_to_be_present(self):
        try:
            return self.my_Wait.until(expected_conditions.alert_is_present())
        except Exception as e:
            return "Element not visible"


