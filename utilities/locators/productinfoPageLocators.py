from selenium.webdriver.common.by import By


class ProductInfoPageLocators:
    addToCart_button = (By.XPATH, "//button[@id='button-cart']")
    black_item_button = (By.XPATH, "//button[@class='btn btn-inverse btn-block btn-lg dropdown-toggle']")
    success_message = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    shopping_cart_link = (By.LINK_TEXT, "shopping cart")
