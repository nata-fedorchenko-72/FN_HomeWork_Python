from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install())
    )

# открыть страницу
driver.get("http://the-internet.herokuapp.com/entry_ad")

# нажать на кнопку
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "div.modal-footer"))
)
button.click()

driver.quit()
