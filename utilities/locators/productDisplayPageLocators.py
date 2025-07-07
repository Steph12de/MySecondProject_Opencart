from selenium.webdriver.common.by import By


class ProductDisplayPageLocators:
    quantity_input_field = (By.XPATH, "//input[@id='input-quantity']")
    add_to_cart_product_page = (By.XPATH, "//button[@id='button-cart']")

