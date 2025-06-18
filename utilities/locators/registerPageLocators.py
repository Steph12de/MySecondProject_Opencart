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
    warning_message = (By.XPATH, "//div[contains(text(),' Warning: You must agree to the Privacy Policy!')]")
    first_name_warning_message = (By.XPATH, "//div[contains(text(),'First Name must be between 1 and 32 characters!')]")
    last_name_warning_message = (By.XPATH, "//div[contains(text(),'Last Name must be between 1 and 32 characters!')]")
    eMail_warning_message = (By.XPATH, "//div[contains(text(),'E-Mail Address does not appear to be valid!')]")
    telephone_warning_message = (By.XPATH, "//div[contains(text(),'Telephone must be between 3 and 32 characters!')]")
    password_warning_message = (By.XPATH, "//div[contains(text(),'Password must be between 4 and 20 characters!')]")
    confirm_password_warning_message = (By.XPATH, "//div[contains(text(),'Password confirmation does not match "
                                                  "password!')]")
    eMail_registered_warning_message = (By.XPATH, "//div[contains(text(),' Warning: E-Mail Address is already "
                                                  "registered!')]")