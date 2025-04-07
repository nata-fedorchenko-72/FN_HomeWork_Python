from selenium.webdriver.common.by import By


class InformationPage:
    """
       Класс оформления заказа
    """
    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(10)

    def first_name(self, name: str):
        """
           Заполнить поле "имя"
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "#first-name"
            ).send_keys(name)

    def last_name(self, name: str):
        """
           Заполнить поле "фамилия"
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "#last-name"
            ).send_keys(name)

    def postal_code(self, code: str):
        """
           Заполнить поле "почтовый индекс"
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "#postal-code"
            ).send_keys(code)

    def button_continue(self):
        """
           Нажать кнопку "Continue"
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "#continue"
            ).click()

    def total_set(self) -> str:
        """
           Получить итоговую стоимость
        """
        total = self._driver.find_element(
            By.CSS_SELECTOR, ".summary_total_label"
            ). text

        return (total)
