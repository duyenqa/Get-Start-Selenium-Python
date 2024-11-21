import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
import time

@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_browser(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    driver.get("https://www.google.com")
    time.sleep(3)
    assert "Google" in driver.title
    time.sleep(2) 
    driver.quit()
