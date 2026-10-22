import pytest
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Фикстура для WebDriver
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Функция для вычисления выражения
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# Тест для редиректа и вычисления выражения
def test_redirect_and_math(browser):
    url = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(url)
    # Кликаем по кнопке, которая открывает новую вкладку
    button = browser.find_element(By.CLASS_NAME, "trollface")
    button.click()

    # Получаем список вкладок и переключаемся на новую
    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)
    # Получаем значение x
    x_value = browser.find_element(By.ID, "input_value").text
    result = calc(x_value)

    # Вводим ответ в поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(result)
    # Нажимаем кнопку "Submit"
    submit_button = browser.find_element(By.CLASS_NAME, "btn-primary")
    submit_button.click()

    # Ожидание alert и проверка текста
    wait = WebDriverWait(browser, 10)
    alert = wait.until(EC.alert_is_present())
    alert_text = Alert(browser).text
    expected_substring = "э"
    assert expected_substring in alert_text, f"Ожидаемая строка '{expected_substring}' отсутствует в alert: '{alert_text}'"

    # Закрываем alert
    alert.accept()




