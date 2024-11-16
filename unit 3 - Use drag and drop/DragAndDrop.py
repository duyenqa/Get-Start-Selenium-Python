import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_dragdrop():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://demo.guru99.com/test/drag_drop.html")
    driver.maximize_window()
    driver.implicitly_wait(20)

    dragElement = driver.find_element(By.XPATH, "//li[@id='fourth'][1]")
    dropElement = driver.find_element(By.XPATH, "//ol[@id='amt7']/li")

    ActionChains(driver).drag_and_drop(dragElement, dropElement).perform()

    time.sleep(10)
    driver.close()
    driver.quit()
    print("Done!")
