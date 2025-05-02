from selenium.webdriver.common.by import By


class HomePageLocators:
    my_account_button = (By.XPATH, "//a[@title='My Account']")
    my_account_login = (By.LINK_TEXT, "Login")
    desktop_button = (By.XPATH, "//a[@class='dropdown-toggle' and text()='Desktops']")
    #desktop_button = (By.LINK_TEXT, "Desktops")
    show_all_desktops_button = (By.LINK_TEXT, "Show All Desktops")



