import pytest
from selenium import webdriver

@pytest.fixture
def diver():
    driver = webdriver.Chrome()
    driver.get("https://humo.tj/en")
    yield driver
    driver.quit()