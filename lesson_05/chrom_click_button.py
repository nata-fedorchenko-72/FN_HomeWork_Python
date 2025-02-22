from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
    )

# открыть страницу
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

sleep(5)

# пять раз кликнуть на кнопку
button = driver.find_element(By.CSS_SELECTOR, "button")
for bu in range(5):
    button.click()

sleep(5)

# собрать список кнопок Delite
delete_button = driver.find_elements(By.CSS_SELECTOR, "button.added-manually")

# вывести размер списка
print("Кнопок Delete:", len(delete_button))
