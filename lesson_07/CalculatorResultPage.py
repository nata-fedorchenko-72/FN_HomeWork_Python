from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorResultPage:
    def __init__(self, driver):
        self._driver = driver

    def checking_result(self, answer):
        return WebDriverWait(self._driver, 45).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "div.screen"), answer)
                )

    def result(self, answer):
        res = self._driver.find_element(By.CSS_SELECTOR, "div.screen"). text
        return int(res)
