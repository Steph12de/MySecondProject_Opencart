from selenium.webdriver.common.by import By


class ProductInfoPageLocators:
    addToCart_button = (By.XPATH, "//button[@id='button-cart']")
    item_button = (By.XPATH, "//span[@id='cart-total']")
    success_message = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
