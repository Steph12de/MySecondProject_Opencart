from selenium.webdriver.common.by import By


class ShoppingCartLocators:
    product_name = (By.XPATH, "//div[@class='table-responsive']//table//tbody//tr//td[2]//a")
    numbers_of_rows = (By.XPATH, "//div[@class='table-responsive']//table//tbody//tr")
    warning_message = (By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")

