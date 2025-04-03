from selenium.webdriver.common.by import By


class LoginPageLocators:

    eMail = (By.ID, "input-email")
    password = (By.ID, "input-password")
    loginButton = (By.XPATH, "//button[@type='submit']")

