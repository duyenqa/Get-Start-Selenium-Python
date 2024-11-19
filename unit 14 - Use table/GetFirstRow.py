import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_table():
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

    #scroll to element
    elementTable = driver.find_element(By.ID, "customers")
    driver.execute_script("arguments[0].scrollIntoView(true);", elementTable)

    time.sleep(7)
    tableData = driver.find_element(By.XPATH, "//table[@id='customers']/tbody/tr[1]")

    cells = tableData.find_elements(By.TAG_NAME, "td")
    for cell in cells:
        print(cell.text) #first row