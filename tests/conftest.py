import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import os

@pytest.fixture(scope="session")
def driver():
    driver=webdriver.Chrome()

    yield driver
    driver.quit()
