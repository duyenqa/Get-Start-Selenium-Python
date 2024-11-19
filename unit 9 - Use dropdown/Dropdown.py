import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

def test_dropdown():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://duyenqa.github.io/firstweb/pages/contact.html")
    driver.maximize_window()
    driver.implicitly_wait(20)

    author = driver.find_element(By.NAME, "author")
    selectAuthor = Select(author)
    selectAuthor.select_by_value("Leopoldo_Corkery")
    time.sleep(3)



