from selenium.webdriver.common.by import By


class FormFillingPage:
    """
       Класс для заполнения формы
    """
    def __init__(self, driver):
        """
           Зайти на сайт
        """
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.maximize_window()

    def first_name(self, name: str):
        """
           Заполнить поле "имя"
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='first-name']"
            ).send_keys(name)

    def last_name(self, name: str):
        """
          Заполнить поле "фамилия"
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='last-name']"
            ).send_keys(name)

    def address(self, data: str):
        """
           Заполнить поле "адресс"
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='address']"
            ).send_keys(data)

    def zip_code(self, data: str):
        """
           Заполнить поле "почтовый индекс"
        """
        self._driver.find_element(
            By.NAME, 'zip-code').send_keys(data)

    def city(self, data: str):
        """
           Заполнить поле "город"
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='city']"
            ).send_keys(data)

    def country(self, data: str):
        """
           Заполнить поле "страна"
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='country']"
            ).send_keys(data)

    def email(self, data: str):
        """
           Заполнить поле "e-mail"
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='e-mail']"
                                  ).send_keys(data)

    def phone_number(self, number: str):
        """
           Заполнить поле "телефон"
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='phone']").send_keys(number)

    def job_position(self, data: str):
        """
           Заполнить поле "должность"
        """
        self._driver.find_element(By.CSS_SELECTOR, "[name='job-position']"
                                  ).send_keys(data)

    def company(self, data: str):
        """
           Заполнить поле "компания"
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='company']"
            ).send_keys(data)
