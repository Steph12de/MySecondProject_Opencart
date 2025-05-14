from selenium.webdriver.common.by import By


class WishListPageLocators:
    add_to_cart_icon = (By.XPATH, "//div[@class='table-responsive']//table//tbody//tr//td[6]//button[@class='btn btn-primary']")
    shopping_cart_header_icon = (By.XPATH, "//a[@title='Shopping Cart']")
    numbers_of_rows = (By.XPATH, "//div[@class='table-responsive']//table//tbody//tr")
    logout_right_hand_menu = (By.XPATH, "//div[@class='list-group']//a[13]")
    password_right_hand_menu = (By.XPATH, "//div[@class='list-group']//a[3]")