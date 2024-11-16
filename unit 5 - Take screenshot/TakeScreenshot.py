import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def test_screenshot():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.vinabook.com")
    driver.maximize_window()
    driver.implicitly_wait(20)

    driver.save_screenshot('screenshot.png')
    
    time.sleep(10)
    driver.quit()
    print("Done!")