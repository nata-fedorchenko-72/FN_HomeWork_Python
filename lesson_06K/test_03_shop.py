from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_shop():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
        )
    driver.maximize_window()

    driver.get("https://www.saucedemo.com/")

    userName = driver.find_element(By.CSS_SELECTOR, "#user-name")
    userName.send_keys("standard_user")

    password = driver.find_element(By.CSS_SELECTOR, "#password")
    password.send_keys("secret_sauce")

    button_login = driver.find_element(By.CSS_SELECTOR, "#login-button")
    button_login.click()

    add_backpack = driver.find_element(
        By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-backpack")
    add_backpack.click()

    add_shirt = driver.find_element(
        By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-bolt-t-shirt"
        )
    add_shirt.click()

    add_pajamas = driver.find_element(
        By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-onesie")
    add_pajamas.click()

    basket = driver.find_element(
        By.CSS_SELECTOR, "a.shopping_cart_link"
        )
    basket.click()

    checkout = driver.find_element(By.CSS_SELECTOR, "#checkout")
    checkout.click()

    first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
    first_name.send_keys("Наталья")

    last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
    last_name.send_keys("Федорченко")

    postal_code = driver.find_element(By.CSS_SELECTOR, "#postal-code")
    postal_code.send_keys("347340")

    button_continue = driver.find_element(By.CSS_SELECTOR, "#continue")
    button_continue.click()

    total = driver.find_element(
        By.CSS_SELECTOR, ".summary_total_label"). text
    print(total)
    assert (total) == "Total: $58.29"

    driver.quit()
