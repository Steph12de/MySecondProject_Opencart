from selenium.webdriver.common.by import By


class HomePageLocators:
    my_account_button = (By.XPATH, "//a[@title='My Account']")
    my_account_login = (By.LINK_TEXT, "Login")

