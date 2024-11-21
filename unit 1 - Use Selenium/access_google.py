import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_google():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.google.com")
    searchField = driver.find_element(By.ID, "APjFqb")
    searchField.send_keys("Selenium")
    searchField.send_keys(Keys.RETURN)
    time.sleep(5)
    driver.close()
    driver.quit()
    print("Done!")
