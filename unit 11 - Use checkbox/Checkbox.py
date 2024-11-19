import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_checkbox():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://duyenqa.github.io/firstweb/pages/login.html")
    driver.maximize_window()
    driver.implicitly_wait(20)

    rememberMe = driver.find_element(By.ID, "remember")
    if not rememberMe.is_selected():
        rememberMe.click()

    time.sleep(10)
    driver.quit()
    print("Done!")