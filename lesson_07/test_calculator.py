from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from CalculatorPage import CalculatorPage
from CalculatorResultPage import CalculatorResultPage


def test_calculator():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
        )

    caiculator = CalculatorPage(driver)
    caiculator.wait("45")
    caiculator.button_1("7")
    caiculator.button_2("+")
    caiculator.button_3("8")
    caiculator.button_4("=")

    calc_result = CalculatorResultPage(driver)
    calc_result.checking_result("15")
    check = calc_result.result("15")
    assert check == 15

    driver.quit
