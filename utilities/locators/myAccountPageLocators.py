from selenium.webdriver.common.by import By


class MyAccountPageLocators:
    search_input_field = (By.XPATH, "//input[@placeholder='Search']")
    search_button = (By.XPATH, "//button[@class='btn btn-default btn-lg']")
    wish_list_button = (By.XPATH, "//a[@id='wishlist-total']")
    password_button = (By.LINK_TEXT, "Password")