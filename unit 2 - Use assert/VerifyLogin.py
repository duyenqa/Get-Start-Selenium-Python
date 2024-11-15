import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_login():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.vinabook.com/account/login")
    driver.maximize_window()
    driver.implicitly_wait(20)

    
    emailField = driver.find_element(By.ID, "customer_email")
    assert emailField.is_displayed(), "The email textbox is not displayed"

    passwordField = driver.find_element(By.ID, "customer_password")
    assert passwordField.is_displayed(), "The password textbox is not displayed"