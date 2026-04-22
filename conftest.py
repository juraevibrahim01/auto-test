import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    service = Service(executable_path="chromedriver/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://humo.tj/en")
    yield driver
    driver.quit()