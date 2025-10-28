import os


class Helpers:
    def __init__(self, driver, logger, home_page, login_page, my_account):
        self.driver = driver
        self.logger = logger
        self.home_page = home_page
        self.login_page = login_page
        self.my_account = my_account

    def log_failure(self, screenshot_name, message, exception):
        screenshot_path = os.path.join("screenshots", screenshot_name)
        self.driver.save_screenshot(screenshot_path)
        self.logger.error(
            f"{message}\n"
            f"Screenshot saved at: {screenshot_path}\n"
            f"Details: {exception}"
        )
        raise exception

    def navigate_and_optional_login(self, email, password, expected_title="My Account", want_to_login=False,
                                    via_menu=False, using_keyboard=False):
        self.logger.info("Starting Re/login process")

        # Step 1: Navigate to login page
        self.home_page.open_login_page()
        self.logger.info("Navigated to login page")

        if not want_to_login:
            self.logger.info("Login skipped — only navigation performed")
        else:
            # Step 2: Choose login method
            if via_menu:
                self.login_page.click_login_button_right_hand_menu()
                self.logger.info("Triggered login via right-hand menu")

            if using_keyboard:
                self.login_page.log_me_in_using_keyboard(email, password)
                self.logger.info("Submitted credentials using keyboard navigation")
            else:
                self.login_page.log_me_in(email, password)
                self.logger.info("Submitted credentials using standard form submission")

            # Step 3: Wait for expected title to appear
            try:
                self.my_account.check_presence_of_title(expected_title)
                self.logger.info(f"Expected title '{expected_title}' was found")
            except Exception as e:
                self.logger.error(f"Expected title '{expected_title}' not found — possible login failure")
                self.logger.exception(e)

        # Step 4: Return current page title
        actual_title = self.driver.title
        self.logger.info(f"Actual page title after login: '{actual_title}'")

        return actual_title
