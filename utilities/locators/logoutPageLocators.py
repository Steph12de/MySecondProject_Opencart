from selenium.webdriver.common.by import By


class LogoutPageLocators:
    continue_button = (By.LINK_TEXT, "Continue")
    right_side_elements_LO = (By.XPATH, "//div[@class='list-group']//a")