from selenium.webdriver.common.by import By


class SearchPageLocators:
    # imac_image = (By.XPATH, "//img[@title='iMac']")
    imac_image = (By.XPATH, "//img[@title='iMac' and @class='img-responsive']")
