import pytest
from selenium import webdriver

@pytest.fixture
def setUp():
    driver = webdriver.Chrome()
    return driver
