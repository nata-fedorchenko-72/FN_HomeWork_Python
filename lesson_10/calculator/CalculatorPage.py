from selenium.webdriver.common.by import By


class CalculatorPage:
    """
       Класс для взаимодействия с кнопками
    """

    def __init__(self, driver):
        """
           Зайти на сайт
        """
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java"
            "/slow-calculator.html")
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    def wait(self, time: str):
        """
           Функция, которая задает время задержки выполнения действий
        """
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(time)

    def button_1(self, button_text: str):
        """
           Нажать на кнопку с цифрой
        """
        self._driver.find_element(
            By.XPATH,
            f"//span[contains(@class, 'btn btn-outline-primary')"
            f"and text()='{button_text}']"
            ).click()

    def button_2(self, button_text: str):
        """
           Нажать на кнопку математической операции
        """
        self._driver.find_element(
            By.XPATH,
            f"//span[contains(@class, 'btn btn-outline-success')"
            f"and text()='{button_text}']"
            ).click()

    def button_3(self, button_text: str):
        """
           Нажать на кнопку с цифрой
        """
        self._driver.find_element(
            By.XPATH,
            f"//span[contains(@class, 'btn btn-outline-primary')"
            f"and text()='{button_text}']"
            ).click()

    def button_4(self, button_text: str):
        """
           Нажать на кнопку со знаком "="
        """
        self._driver.find_element(
            By.XPATH,
            f"//span[contains(@class, 'btn btn-outline-warning')"
            f"and text()='{button_text}']"
            ).click()
