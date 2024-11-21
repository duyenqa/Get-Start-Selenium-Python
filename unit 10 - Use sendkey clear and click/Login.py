import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_login():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://duyenqa.github.io/firstweb/pages/login.html")
    driver.maximize_window()
    driver.implicitly_wait(20)

    emailField = driver.find_element(By.ID, "username")
    emailField.clear()
    emailField.send_keys("demouser@example.com")

    passwordField = driver.find_element(By.ID, "password")
    passwordField.clear()
    passwordField.send_keys("Test@user1")

    loginButton = driver.find_element(By.CLASS_NAME, "btnLogin")
    loginButton.click()

    time.sleep(5)
    driver.close()
    driver.quit()
    print("Done!")