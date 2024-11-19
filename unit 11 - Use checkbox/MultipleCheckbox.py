import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_multiple_checkbox():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://duyenqa.github.io/firstweb/pages/contact.html")
    driver.maximize_window()
    driver.implicitly_wait(20)

    colors = driver.find_elements(By.NAME, "color")
    for item in colors:
        if not item.is_selected():
            item.click()

    time.sleep(10)
    driver.quit()
    print("Done!")