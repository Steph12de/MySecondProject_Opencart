from selenium.webdriver.common.by import By


class ChangePasswordLocators:

    password_field = (By.XPATH, "//input[@id='input-password']")
    password_confirm_field = (By.XPATH, "//input[@id='input-confirm']")
    continue_button = (By.XPATH, "//input[@value='Continue']")
    expected_error_message = (By.XPATH, "//div[@class='text-danger']")