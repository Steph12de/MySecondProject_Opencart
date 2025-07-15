from selenium.webdriver.common.by import By


class ProductInfoPageLocators:
    addToCart_button = (By.XPATH, "//button[@id='button-cart']")
    black_item_button = (By.XPATH, "//button[@class='btn btn-inverse btn-block btn-lg dropdown-toggle']")
    success_message = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    shopping_cart_link = (By.LINK_TEXT, "shopping cart")
    quantity_input_field = (By.XPATH, "//input[@id='input-quantity']")
    add_to_cart_product_page = (By.XPATH, "//button[@id='button-cart']")
    product_name = (By.XPATH, "//div[@class='col-sm-4']//h1")
    # product_list_elements =(By.XPATH, "//div[@class='col-sm-4']//ul[1]//li")
    product_brand = (By.XPATH, "//div[@class='col-sm-4']//ul//li//a")
    product_code = (By.XPATH, "//ul//li[text()='Product Code: Product 14']") # "//ul//li[contains(text(), 'Product Code:')]"
