import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_a_tag():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://duyenqa.github.io/firstweb/index.html")
    driver.maximize_window()
    driver.implicitly_wait(20)

    ulElement = driver.find_element(By.ID, "myDropdown")
    liList = ulElement.find_elements(By.TAG_NAME, "li")

    for li in liList:
        aList = li.find_elements(By.TAG_NAME, "a")
        for a in aList:
            print(a.get_attribute("href"))

    time.sleep(10)
    driver.quit()
    print("Done!")

