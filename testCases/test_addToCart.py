from pageObjects.homePage import HomePage
from pageObjects.loginPage import LoginPage
from pageObjects.myAccountPage import MyAccountPage
from pageObjects.searchPage import SearchPage
from utilities.custom_logger import LogGen


class Test_002_addToCart:
    logger = LogGen.loggen()

    def test_add_to_cart(self, setUp):
        self.driver = setUp
        home_page = HomePage(self.driver)
        home_page.bring_me_to_login_page()
        login_page = LoginPage(self.driver)
        login_page.log_me_in("username@gmail.de", "admin")
        myAccount_page = MyAccountPage(self.driver)
        myAccount_page.input_search_element("imac")
        myAccount_page.click_on_search_button()
        search_page = SearchPage(self.driver)
        search_page.click_on_imac_image()
