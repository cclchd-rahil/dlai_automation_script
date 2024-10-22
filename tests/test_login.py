# tests/test_login.py
from selenium.webdriver.common.by import By
from pages import login_page
from pages.login_page import LoginPage


def test_valid_login(driver):
    login_page = LoginPage(driver)

    driver.get("https://dlai.nfttrace.com/login")
    driver.maximize_window()
    # Enter valid credentials
    login_page.enter_username("dlaiadmin@nfttrace.com")
    login_page.enter_password("DlaiAdmin@2024")
    login_page.click_login()

    expected_title = "DLAI Admin Panel - Login to Manage and Track Your NFTs with Ease"
    assert driver.title == expected_title, f"Expected title '{expected_title}', but got '{driver.title}'"

    # # Admin portal element
    # elements = driver.find_elements(By.XPATH, "/html/body/div[1]/main/div/div/div/nav/div/div[1]/div/h4")
    # assert len(elements) > 0, "element not found"


def test_invalid_login(driver):
    login_page = LoginPage(driver)
    driver.get("https://dlai.nfttrace.com/login")

    login_page.enter_username("dlaiamin@nfttrace.com")
    login_page.enter_password("DlaiAdmin@2024")
    login_page.click_login()

    error_messages = login_page.get_error_messages()

    assert error_messages['require'] == "Email or password is invalid", (f"Expected 'Email or password is invalid', "
                                                                         f"but got '{error_messages['require']}")


def test_empty_username_password(driver):
    login_page = LoginPage(driver)

    driver.get("https://dlai.nfttrace.com/login")

    # Leave both fields empty
    login_page.enter_username("")
    login_page.enter_password("")
    login_page.click_login()

    # Check if the appropriate error message is displayed
    error_messages = login_page.get_error_messages()

    assert error_messages[
               'email'] == "Email is required", f"Expected 'Email is required', but got '{error_messages['email']}'"
    assert error_messages[
               'password'] == "Password is required", f"Expected 'Password is required', but got '{error_messages['password']}'"


def test_empty_username(driver):
    login_page = LoginPage(driver)

    driver.get("https://dlai.nfttrace.com/login")

    # Leave username fields empty
    login_page.enter_username(" ")
    login_page.enter_password("DlaiAdmin@2024")
    login_page.click_login()

    error_message = login_page.get_error_messages()
    assert error_message[
               'email'] == "Email is required", f"Expected 'Email is required',but got '{error_message['email']}'"


def test_empty_password(driver):
    login_page = LoginPage(driver)

    driver.get("https://dlai.nfttrace.com/login")

    login_page.enter_username("dlaiadmin@nfttrace.com")
    login_page.enter_password("")
    login_page.click_login()

    error_message = login_page.get_error_messages()
    assert error_message[
               'password'] == "Password is required", f"Expected 'Password is required', but got '{error_message['password']}'"


