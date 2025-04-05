import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from AuthorizationShopPage import AuthorizationShopPage
from ShoppingCartPage import ShoppingCartPage
from InformationPage import InformationPage


@allure.title("Покупка на сайте")
@allure.description("Проверить итоговую сумму покупок")
@allure.feature("итоговая сумма в корзине")
@allure.severity("blocker")
def test_authorization_shop():
    with allure.step("Зайти на сайт"):
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))

    authorization_shop = AuthorizationShopPage(driver)
    with allure.step("Ввести имя"):
        authorization_shop.userName("standard_user")
    with allure.step("Ввести пароль"):
        authorization_shop.password("secret_sauce")
    with allure.step("Нажать кнопку login"):
        authorization_shop.button_login()

    shoppig_cart = ShoppingCartPage(driver)
    with allure.step("Добавить товар в корзину"):
        shoppig_cart.add_backpack("button#add-to-cart-sauce-labs-backpack")
    with allure.step("Добавить товар в корзину"):
        shoppig_cart.add_shirt("button#add-to-cart-sauce-labs-bolt-t-shirt")
    with allure.step("Добавить товар в корзину"):
        shoppig_cart.add_pajamas("button#add-to-cart-sauce-labs-onesie")
    with allure.step("Нажать на элемент корзины"):
        shoppig_cart.basket()
    with allure.step("Нажать кнопку Cheskout"):
        shoppig_cart.checkout()

    info = InformationPage(driver)
    with allure.step("Заполнить поле имя"):
        info.first_name("Наталья")
    with allure.step("Заполнить поле фамилия"):
        info.last_name("Федорченко")
    with allure.step("Заполнить поле почтовый индекс"):
        info.postal_code("347340")
    with allure.step("Нажать кнопку Continue"):
        info.button_continue()
    with allure.step("Получить итоговую стоимость"):
        total = info.total_set()

    with allure.step("Проверить итоговую стоимость"):
        assert (total) == "Total: $58.29"

    with allure.step("Закрыть драйвер"):
        driver.quit
