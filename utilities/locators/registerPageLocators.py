from selenium.webdriver.common.by import By


class RegisterPageLocators:
    first_name_input = (By.XPATH, "//input[@id='input-firstname']")
    last_name_input = (By.XPATH, "//input[@id='input-lastname']")
    eMail_input = (By.XPATH, "//input[@id='input-email']")
    telephone_input = (By.ID, "input-telephone")
    password_input = (By.NAME, "password")
    password_confirm_input = (By.ID, "input-confirm")
    newsletter_subscribe = (By.XPATH, "//label[@class='radio-inline']//input[@value='0']")
    newsletter_unsubschribe = (By.XPATH, "//label[@class='radio-inline']//input[@value='1']")
    privacy_policy_check = (By.XPATH, "//input[@name='agree']")
    continue_button = (By.XPATH, "//input[@value='Continue']")
