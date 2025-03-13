from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from AuthorizationShopPage import AuthorizationShopPage
from ShoppingCartPage import ShoppingCartPage
from InformationPage import InformationPage


def test_authorization_shop():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    authorization_shop = AuthorizationShopPage(driver)
    authorization_shop.userName("standard_user")
    authorization_shop.password("secret_sauce")
    authorization_shop.button_login()

    shoppig_cart = ShoppingCartPage(driver)
    shoppig_cart.add_backpack("button#add-to-cart-sauce-labs-backpack")
    shoppig_cart.add_shirt("button#add-to-cart-sauce-labs-bolt-t-shirt")
    shoppig_cart.add_pajamas("button#add-to-cart-sauce-labs-onesie")
    shoppig_cart.basket()
    shoppig_cart.checkout()

    info = InformationPage(driver)
    info.first_name("Наталья")
    info.last_name("Федорченко")
    info.postal_code("347340")
    info.button_continue()
    total = info.total_set()

    assert (total) == "Total: $58.29"

    driver.quit
