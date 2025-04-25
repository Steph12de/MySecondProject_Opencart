from selenium.webdriver.common.by import By


class ShoppingCartLocators:
    product_name = (By.XPATH, "//div[@class='table-responsive']//table//tbody//tr//td[2]//a")
