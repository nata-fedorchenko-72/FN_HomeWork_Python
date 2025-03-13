from selenium.webdriver.common.by import By


class CalculatorPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java"
            "/slow-calculator.html")
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    def wait(self, time):
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(time)

    def button_1(self, button_text):
        self._driver.find_element(
            By.XPATH,
            f"//span[contains(@class, 'btn btn-outline-primary')"
            f"and text()='{button_text}']"
            ).click()

    def button_2(self, button_text):
        self._driver.find_element(
            By.XPATH,
            f"//span[contains(@class, 'btn btn-outline-success')"
            f"and text()='{button_text}']"
            ).click()

    def button_3(self, button_text):
        self._driver.find_element(
            By.XPATH,
            f"//span[contains(@class, 'btn btn-outline-primary')"
            f"and text()='{button_text}']"
            ).click()

    def button_4(self, button_text):
        self._driver.find_element(
            By.XPATH,
            f"//span[contains(@class, 'btn btn-outline-warning')"
            f"and text()='{button_text}']"
            ).click()
