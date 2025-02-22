from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install())
    )

# открыть страницу
driver.get(" http://the-internet.herokuapp.com/login")

# ввести значение в поле username
search_input = driver.find_element(By.CSS_SELECTOR, "#username")
search_input.send_keys("tomsmith")

# ввести значение в поле password
search_input = driver.find_element(By.CSS_SELECTOR, "#password")
search_input.send_keys("SuperSecretPassword!")

# нажать кнопку
button = driver.find_element(By.CSS_SELECTOR, "button.radius")
button.click()

sleep(5)

driver.quit()
