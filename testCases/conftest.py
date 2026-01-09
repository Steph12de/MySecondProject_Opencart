import pytest
from pytest_metadata.plugin import metadata_key
from selenium import webdriver


@pytest.fixture
def setUp(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()

    elif browser == "firefox":
        driver = webdriver.Firefox()

    elif browser == "edge":
        driver = webdriver.Edge()

    driver.get("https://awesomeqa.com/ui")
    # driver.get("https://demo.opencart.com/")
    driver.maximize_window()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_html_report_title(report):
    report.title = "OpenCart Reports"


def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'OpenCart Project'
    config.stash[metadata_key]['Tester'] = 'Stephanie'
