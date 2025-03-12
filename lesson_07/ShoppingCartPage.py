from selenium.webdriver.common.by import By


class ShoppingCartPage:

    def __init__(self, driver):
        self._driver = driver

    def add_backpack(self, locator):
        self._driver.find_element(
            By.CSS_SELECTOR, (locator)).click()

    def add_shirt(self, locator):
        self._driver.find_element(
            By.CSS_SELECTOR, (locator)).click()

    def add_pajamas(self, locator):
        self._driver.find_element(
            By.CSS_SELECTOR, (locator)).click()

    def basket(self):
        self._driver.find_element(
            By.CSS_SELECTOR, "a.shopping_cart_link"
            ).click()

    def checkout(self):
        self._driver.find_element(
            By.CSS_SELECTOR, "#checkout").click()
