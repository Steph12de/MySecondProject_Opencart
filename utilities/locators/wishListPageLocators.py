from selenium.webdriver.common.by import By


class WishListPageLocators:
    add_to_cart_icon = (By.XPATH, "//button[@class='btn btn-primary']")
    shopping_cart_header_icon = (By.XPATH, "//a[@title='Shopping Cart']")