from selenium.webdriver.common.by import By


class SearchPageLocators:
    # imac_image = (By.XPATH, "//img[@title='iMac']")
    imac_image = (By.XPATH, "//img[@title='iMac' and @class='img-responsive']")
    add_to_cart_button = (By.XPATH, "//div[@class='button-group']//button//span")
    success_message = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    black_card_button = (By.XPATH, "//button[@class='btn btn-inverse btn-block btn-lg dropdown-toggle']")
    p_elements = (By.XPATH, "//p[@class='text-right']//a//p[@class='text-right']//a")
    view_cart_button = (By.XPATH, "//strong[contains(text(), 'View Cart')]") # "//strong[text()='View Cart']"
    item_card_total = (By.XPATH, "//span[@id='cart-total']")