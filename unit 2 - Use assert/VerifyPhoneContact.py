import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_mainMenu():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.vinabook.com/account/login")
    driver.maximize_window()
    driver.implicitly_wait(20)

    
    phoneElement = driver.find_element(By.XPATH, "//div[@class='header-support__detail']/span")
    phoneText = phoneElement.text
    assert phoneText == "19006401", f"The {phoneElement} is not match"

    time.sleep(5)
    driver.close()
    driver.quit()
    print("Done!")
