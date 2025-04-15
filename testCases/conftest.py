import pytest
from selenium import webdriver


@pytest.fixture
def setUp(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()

    elif browser == "firefox":
        driver = webdriver.Firefox()

    elif browser == "edge":
        driver = webdriver.Edge()

    else:
        driver = webdriver.Ie()

    driver.get("https://awesomeqa.com/ui")
    driver.maximize_window()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    print(request)
    return request.config.getoption("--browser")
