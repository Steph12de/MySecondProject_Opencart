from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base_driver():
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_visible(self, element):
        my_Wait = WebDriverWait(self.driver, 5)
        return my_Wait.until(EC.visibility_of_element_located(element))

    def wait_text_to_be_present_in_element(self, element, text):
        my_Wait = WebDriverWait(self.driver, 5)
        return my_Wait.until(EC.text_to_be_present_in_element(element, text))

