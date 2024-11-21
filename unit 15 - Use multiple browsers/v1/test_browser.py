import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

def test_on_chrome():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    time.sleep(3)
    driver.quit()

def test_on_firefox():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    time.sleep(3)
    driver.quit()

test_on_chrome()
test_on_firefox()