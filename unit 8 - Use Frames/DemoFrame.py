import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_iframe():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://duyenqa.github.io/firstweb/pages/exampleweb.html")
    driver.maximize_window()
    driver.implicitly_wait(20)

    driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demoFrame']"))
    resultText = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))
    print(resultText.text)

    time.sleep(10)
    driver.quit()
    print("Done!")