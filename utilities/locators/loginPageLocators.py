from selenium.webdriver.common.by import By


class LoginPageLocators:

    eMail = (By.ID, "input-email")
    password = (By.ID, "input-password")
    loginButton = (By.XPATH, "//input[@type='submit']")
    login_error_message = (By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")
    forgotten_password_text = (By.LINK_TEXT, "Forgotten Password")
    loginButtonRightHandMenu = (By.XPATH, "//div[@class='list-group']//a[1]")

