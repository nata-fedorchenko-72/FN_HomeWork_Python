from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SubmitClickPage:
    """
       Класс для получения ответа сайта на незаполненное поле
    """
    def __init__(self, driver):
        self._driver = driver

    def button_submit(self):
        """
           Нажать на кнопку "submit"
        """
        element = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3")))
        self._driver.execute_script("arguments[0].click();", element)

    def zip_code_color(self) -> str:
        """
           Цвет незаполненного поля
        """
        return self._driver.find_element(
            By.CSS_SELECTOR, "#zip-code"
            ).value_of_css_property('background-color')

    def fields_color(self) -> str:
        """
           Цвет заполненных полей
        """
        fields = ["#first-name",
                  "#last-name",
                  "#address",
                  "#city",
                  "#country",
                  "#e-mail",
                  "#phone",
                  "#job-position",
                  "#company"]
        for field in fields:
            return self._driver.find_element(
                By.CSS_SELECTOR, field).value_of_css_property(
                    'background-color')
