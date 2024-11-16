import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_rightclick():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://demo.guru99.com/test/simple_context_menu.html")
    driver.maximize_window()
    driver.implicitly_wait(20)

    button = driver.find_element(By.XPATH, "//span[text()='right click me']")
    ActionChains(driver).context_click(button).perform()

    time.sleep(10)
    driver.quit()
    print("Done!")