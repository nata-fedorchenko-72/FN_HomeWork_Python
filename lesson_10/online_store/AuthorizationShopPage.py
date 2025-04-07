from selenium.webdriver.common.by import By


class AuthorizationShopPage:
    """
       Класс авторизации
    """
    def __init__(self, driver):
        """
           Зайти на сайт
        """
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def userName(self, name: str):
        """
           Ввести имя пользователя
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "#user-name"
            ).send_keys(name)

    def password(self, code: str):
        """
           Ввести пароль
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "#password"
            ).send_keys(code)

    def button_login(self):
        """
           Нажать кнопку login
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "#login-button"
            ).click()
