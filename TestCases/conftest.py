import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver
