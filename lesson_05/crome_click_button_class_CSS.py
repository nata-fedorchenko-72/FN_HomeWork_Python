from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
    )

# открыть страницу
driver.get("http://uitestingplayground.com/classattr")

sleep(5)

# кликнуть на синюю кнопку
button_blue = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
button_blue.click()

sleep(5)