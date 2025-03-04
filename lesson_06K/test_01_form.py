from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

    first_name = driver.find_element(By.CSS_SELECTOR, "[name='first-name']")
    first_name.send_keys("Иван")

    last_name = driver.find_element(By.CSS_SELECTOR, "[name='last-name']")
    last_name.send_keys("Петров")

    address = driver.find_element(By.CSS_SELECTOR, "[name='address']")
    address.send_keys("Ленина, 55-3")

    zip_code = driver.find_element(By.NAME, 'zip-code')
    zip_code.send_keys("")

    city = driver.find_element(By.CSS_SELECTOR, "[name='city']")
    city.send_keys("Москва")

    country = driver.find_element(By.CSS_SELECTOR, "[name='country']")
    country.send_keys("Россия")

    email = driver.find_element(By.CSS_SELECTOR, "[name='e-mail']")
    email.send_keys("test@skypro.com")

    phone_number = driver.find_element(By.CSS_SELECTOR, "[name='phone']")
    phone_number.send_keys("+7985899998787")

    job_position = driver.find_element(
        By.CSS_SELECTOR, "[name='job-position']")
    job_position.send_keys("QA")

    company = driver.find_element(By.CSS_SELECTOR, "[name='company']")
    company.send_keys("SkyPro")

    element = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3")))
    driver.execute_script("arguments[0].click();", element)

    # Проверка цвета для поля zip-code
    zip_code_color = driver.find_element(
        By.CSS_SELECTOR, "#zip-code").value_of_css_property('background-color')
    assert zip_code_color == "rgba(248, 215, 218, 1)", \
        f"Цвет поля zip-code должен быть rgba(248, 215, 218, 1), \
            а не {zip_code_color}"

    # Проверка цвета для остальных полей
    success_color = "rgba(209, 231, 221, 1)"
    fields = ["#first-name",
              "#last-name",
              "#address",
              "#city",
              "#country",
              "#e-mail",
              "#phone",
              "#job-position",
              "#company"]

    for field in fields:
        field_color = driver.find_element(
            By.CSS_SELECTOR, field).value_of_css_property('background-color')
        assert field_color == success_color, f"Цвет поля {field} должен быть"
        f"{success_color}, а не {field_color}"

    driver.quit()
