from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install())
    )

# открыть страницу
driver.get("http://the-internet.herokuapp.com/inputs")

# текст 1000
search_input = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
search_input.send_keys("1000")

sleep(5)

# очистить поле
search_input.clear()

sleep(5)

# текст 999
search_input.send_keys("999")

sleep(5)

driver.quit()
