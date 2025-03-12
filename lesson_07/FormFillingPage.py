from selenium.webdriver.common.by import By


class FormFillingPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.maximize_window()

    def first_name(self, name):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='first-name']"
            ).send_keys(name)

    def last_name(self, name):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='last-name']"
            ).send_keys(name)

    def address(self, data):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='address']"
            ).send_keys(data)

    def zip_code(self, data):
        self._driver.find_element(
            By.NAME, 'zip-code').send_keys(data)

    def city(self, data):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='city']"
            ).send_keys(data)

    def country(self, data):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='country']"
            ).send_keys(data)

    def email(self, data):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='e-mail']"
                                  ).send_keys(data)

    def phone_number(self, number):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='phone']").send_keys(number)

    def job_position(self, data):
        self._driver.find_element(By.CSS_SELECTOR, "[name='job-position']"
                                  ).send_keys(data)

    def company(self, data):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='company']"
            ).send_keys(data)
