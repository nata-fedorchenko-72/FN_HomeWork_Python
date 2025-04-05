import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from FormFillingPage import FormFillingPage
from SubmitClickPage import SubmitClickPage


@allure.title("Заполнение формы")
@allure.description("Проверить ответ сайта на пустое поле")
@allure.feature("Ввод данных")
@allure.severity("critical")
def test_form_filling():
    with allure.step("Зайти на сайт"):
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
            )

    form_filling = FormFillingPage(driver)
    with allure.step("Ввести имя"):
        form_filling.first_name("Иван")
    with allure.step("Ввести фамилию"):
        form_filling.last_name("Петров")
    with allure.step("Ввести адресс"):
        form_filling.address("Ленина, 55-3")
    with allure.step("Оставить поле пустым"):
        form_filling.zip_code("")
    with allure.step("Ввести город"):
        form_filling.city("Москва")
    with allure.step("Ввести страну"):
        form_filling.country("Россия")
    with allure.step("Ввести e-mail"):
        form_filling.email("test@skypro.com")
    with allure.step("Ввести номер телефона"):
        form_filling.phone_number("+7985899998787")
    with allure.step("Ввести должность"):
        form_filling.job_position("QA")
    with allure.step("Ввести название компании"):
        form_filling.company("SkyPro")

    submit_click = SubmitClickPage(driver)
    with allure.step("Нажать на кнопку submit"):
        submit_click.button_submit()
        zip_color = submit_click.zip_code_color()
    with allure.step("Проверить, что цвет поля соответствует ожидаемому"):
        assert zip_color == "rgba(248, 215, 218, 1)", \
            f"Цвет поля zip-code должен быть rgba(248, 215, 218, 1), \
                а не {zip_color}"
        f_color = submit_click.fields_color()
    with allure.step("Проверить, что цвет поля соответствует ожидаемому"):
        assert f_color == "rgba(209, 231, 221, 1)", \
            f"Цвет поля field rgba должен быть (209, 231, 221, 1), \
                а не {f_color}"
    with allure.step("Закрыть драйвер"):
        driver.quit
