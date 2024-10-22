# pages/base_page.py
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def find_element(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            print(f"Element with locator {locator} not found.")
            return None

    def click(self, locator):
        element = self.find_element(locator)
        if element:
            element.click()

    def send_keys(self, locator, keys):
        element = self.find_element(locator)
        if element:
            element.clear()
            element.send_keys(keys)

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text if element else ""
