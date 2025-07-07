from selenium.webdriver.common.by import By


class ComparisonPageLocators:
    #add_to_cart_ipod_classic = (By.XPATH, "//table[@class='table table-bordered']//tbody[4]//tr//td")
    number_of_rows = (By.XPATH, "//table[@class='table table-bordered']//tbody[1]//tr")
    product_names = (By.XPATH, "//table[@class='table table-bordered']//tbody[1]//tr[1]//td//a")
    add_to_cart_buttons = (By.XPATH, "//table[@class='table table-bordered']//tbody[5]//tr//td//input")
    success_message_text = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    shopping_cart_link = (By.LINK_TEXT, "shopping cart")
    product_table = (By.XPATH, "//div[@id='content']//table[@class='table table-bordered']")
    product_unavailability_text = (By.XPATH, "//div[@id='content']//p")
    add_to_cart_apple_cinema = (By.XPATH, "//div[@id='content']//div[1]//div[1]//div[2]//div[2]//button[3]")
