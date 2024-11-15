import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_table():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://duyenqa.github.io/firstweb/")
    driver.maximize_window()
    driver.implicitly_wait(20)

    list = driver.find_elements(By.XPATH, "//table[@id='customers']/thead/tr/th")
    for title in list:
        print(title.text)
    
    time.sleep(5)
    driver.close()
    driver.quit()
    print("Done!")
