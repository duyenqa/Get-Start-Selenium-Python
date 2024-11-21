import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def set_up():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://duyenqa.github.io/firstweb/pages/login.html")
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield driver
    driver.quit()

@pytest.fixture(params=[
    {"username": "tester1", "password": "123456"},
    {"username": "demouser@example.com", "password": "123456"},
    {"username": "demouser@example.com", "password": "Test@user1"}
])
def user_credentials(request):
    return request.param

def test_login(set_up, user_credentials):
    driver = set_up

    emailField = driver.find_element(By.ID, "username")
    emailField.clear()
    emailField.send_keys(user_credentials["username"])

    passwordField = driver.find_element(By.ID, "password")
    passwordField.clear()
    passwordField.send_keys(user_credentials["password"])

    loginButton = driver.find_element(By.CLASS_NAME, "btnLogin")
    loginButton.click()

    time.sleep(5)