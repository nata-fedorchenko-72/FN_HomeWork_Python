import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_calc():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
        )
    driver.maximize_window()

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    wait = driver.find_element(By.CSS_SELECTOR, "#delay")
    wait.clear()
    wait.send_keys("45")

    driver.find_element(
        By.XPATH, "//span[contains(@class, 'btn btn-outline-primary') and text()='7']"
        ).click()
    driver.find_element(
        By.XPATH, "//span[contains(@class, 'btn btn-outline-success') and text()='+']"
        ).click()
    driver.find_element(
        By.XPATH, "//span[contains(@class, 'btn btn-outline-primary') and text()='8']"
        ).click()
    driver.find_element(
        By.XPATH, "//span[contains(@class, 'btn btn-outline-warning') and text()='=']"
        ).click()

    WebDriverWait(driver, 45).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
    )

    result = driver.find_element(By.CSS_SELECTOR, "div.screen"). text
    assert int(result) == 15
    driver.quit
