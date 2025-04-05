import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from CalculatorPage import CalculatorPage
from CalculatorResultPage import CalculatorResultPage


@allure.title("Калькулятор")
@allure.description("Работа калькулятора с задержкой по времени")
@allure.feature("Сложение")
@allure.severity("minor")
def test_calculator():
    with allure.step("Зайти на сайт"):
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
            )

    caiculator = CalculatorPage(driver)
    with allure.step("Выставить время задержки"):
        caiculator.wait("45")
    with allure.step("Нажать на цифру 7"):
        caiculator.button_1("7")
    with allure.step("Нажать на знак +"):
        caiculator.button_2("+")
    with allure.step("Нажать на цифру 8"):
        caiculator.button_3("8")
    with allure.step("Нажать на знак ="):
        caiculator.button_4("=")

    calc_result = CalculatorResultPage(driver)
    calc_result.checking_result("15")
    check = calc_result.result("15")
    with allure.step("Проверить: результат = 15"):
        assert check == 15

    with allure.step("Закрыть драйвер"):
        driver.quit
