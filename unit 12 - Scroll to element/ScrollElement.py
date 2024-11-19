import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_scroll():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://duyenqa.github.io/firstweb/pages/login.html")
    driver.maximize_window()
    driver.implicitly_wait(20)

    emailField = driver.find_element(By.ID, "username")
    emailField.clear()
    emailField.send_keys("demouser@example.com")

    passwordField = driver.find_element(By.ID, "password")
    passwordField.send_keys("Test@user1")

    loginButton = driver.find_element(By.CLASS_NAME, "btnLogin")
    loginButton.click()

    time.sleep(3)

    elementTable = driver.find_element(By.ID, "customers") 
    driver.execute_script("arguments[0].scrollIntoView(true);", elementTable)

    time.sleep(10)
    driver.quit()
    print("Done!")