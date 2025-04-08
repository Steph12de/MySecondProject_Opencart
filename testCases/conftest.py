import pytest
from selenium import webdriver

@pytest.fixture
def setUp():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui")
    driver.maximize_window()
    return driver

# parametrizing fixture
# @pytest.fixture(scope="class")
# def setUp(request):
#     driver = webdriver.Chrome()
#     driver.get("https://awesomeqa.com/ui")
#     driver.maximize_window()
#     request.cls.driver = driver


