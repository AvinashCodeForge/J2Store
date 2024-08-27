import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def setup(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.quit()
