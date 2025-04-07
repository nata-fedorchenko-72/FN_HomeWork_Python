from selenium.webdriver.common.by import By


class ShoppingCartPage:
    """
       Класс для выбора товара
    """
    def __init__(self, driver):
        self._driver = driver

    def add_backpack(self, locator):
        """
           Добавить товар в корзину
        """
        self._driver.find_element(
            By.CSS_SELECTOR, (locator)).click()

    def add_shirt(self, locator):
        """
           Добавить товар в корзину
        """
        self._driver.find_element(
            By.CSS_SELECTOR, (locator)).click()

    def add_pajamas(self, locator):
        """
           Добавить товар в корзину
        """
        self._driver.find_element(
            By.CSS_SELECTOR, (locator)).click()

    def basket(self):
        """
           Нажать на элемент корзины
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "a.shopping_cart_link"
            ).click()

    def checkout(self):
        """
           Нажать кнопку "Cheskout"
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "#checkout").click()
