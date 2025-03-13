from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from FormFillingPage import FormFillingPage
from SubmitClickPage import SubmitClickPage


def test_form_filling():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
        )

    form_filling = FormFillingPage(driver)
    form_filling.first_name("Иван")
    form_filling.last_name("Петров")
    form_filling.address("Ленина, 55-3")
    form_filling.zip_code("")
    form_filling.city("Москва")
    form_filling.country("Россия")
    form_filling.email("test@skypro.com")
    form_filling.phone_number("+7985899998787")
    form_filling.job_position("QA")
    form_filling.company("SkyPro")

    submit_click = SubmitClickPage(driver)
    submit_click.button_submit()
    zip_color = submit_click.zip_code_color()
    assert zip_color == "rgba(248, 215, 218, 1)", \
        f"Цвет поля zip-code должен быть rgba(248, 215, 218, 1), \
            а не {zip_color}"
    f_color = submit_click.fields_color()
    assert f_color == "rgba(209, 231, 221, 1)", \
        f"Цвет поля field rgba должен быть (209, 231, 221, 1), а не {f_color}"

    driver.quit
