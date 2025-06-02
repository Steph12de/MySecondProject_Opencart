from selenium.webdriver.common.by import By


class ComparisonPageLocators:
    add_to_cart_ipod_classic = (By.XPATH, "//table[@class='table table-bordered']//tbody[4]//tr//td")
    number_of_rows = (By.XPATH, "//table[@class='table table-bordered']//tbody[1]//tr")
    number_of_columns= (By.XPATH, "")
    product_name = (By.XPATH, "//table[@class='table table-bordered']//tbody[1]//tr//td//a")
