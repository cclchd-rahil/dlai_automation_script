# pages/login_page.py
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Login')]")

    def enter_username(self, username):
        self.send_keys(self.USERNAME, username)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def get_error_messages(self):
        messages = {}
        #Email validation
        try:
            email_error_element = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div["
                                                                     "2]/div/div/div/div/form/div[1]/div")
            messages['email'] = email_error_element.text
        except NoSuchElementException:
            messages['email'] = None  # or just don't add it if you prefer

        #Password validation
        try:
            password_error_element = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div["
                                                                        "2]/div/div/div/div/form/div[2]/div/div")
            messages['password'] = password_error_element.text
        except NoSuchElementException:
            messages['password'] = None  # or just don't add it if you prefer

        #Toaster
        try:
            require_error_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div/div[1]/div[2]"))
            )
            messages['require'] = require_error_element.text
        except (NoSuchElementException, TimeoutException):
            messages['require'] = None  # or skip this entry

        return messages






