from selenium.webdriver.common.by import By


class LoginPageLocators:

    eMail = (By.ID, "input-email")
    password = (By.ID, "input-password")
    loginButton = (By.XPATH, "//input[@type='submit']")
    login_error_message = (By.XPATH, "//div[contains(@class, 'alert-danger') and contains(text(), 'Warning') and contains(text(), 'No match')]")
    # login_error_account_exceded = (By.XPATH, "//div[contains(@class, 'alert-danger') and contains(text(), 'Warning') and contains(text(), 'Your account has')]")
    forgotten_password_text = (By.LINK_TEXT, "Forgotten Password")
    loginButtonRightHandMenu = (By.XPATH, "//div[@class='list-group']//a[1]")
    continue_button = (By.LINK_TEXT, "Continue")
    right_hand_menu_elements = (By.XPATH, "//div[@class='list-group']//a")


