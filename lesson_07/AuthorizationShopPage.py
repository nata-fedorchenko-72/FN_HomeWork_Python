from selenium.webdriver.common.by import By


class AuthorizationShopPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def userName(self, name):
        self._driver.find_element(
            By.CSS_SELECTOR, "#user-name"
            ).send_keys(name)

    def password(self, code):
        self._driver.find_element(
            By.CSS_SELECTOR, "#password"
            ).send_keys(code)

    def button_login(self):
        self._driver.find_element(
            By.CSS_SELECTOR, "#login-button"
            ).click()
