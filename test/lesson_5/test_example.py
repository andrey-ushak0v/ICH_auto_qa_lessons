import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_fill_form_and_check_alert(browser):
    url = "https://suninjuly.github.io/huge_form.html"
    browser.get(url)
    input_fields = browser.find_elements(By.TAG_NAME, "input")
    for field in input_fields:
        field.clear()
        field.send_keys("Hello")

    submit_button = browser.find_element(By.CLASS_NAME, "btn-default")
    submit_button.click()
    time.sleep(3)
    wait = WebDriverWait(browser, 10)
    alert = wait.until(EC.alert_is_present())
    alert_text = Alert(browser).text
    expected_substring = "Congrats, you've passed the task!"
    assert expected_substring in alert_text, f"Ожидаемая строка '{expected_substring}' отсутствует в alert: '{alert_text}'"

    alert.accept()




def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

def test_math_form(browser):
        url = "https://suninjuly.github.io/math.html"
        browser.get(url)

        x_value = browser.find_element(By.ID, "input_value").text
        result = calc(x_value)

        answer_input = browser.find_element(By.ID, "answer")
        answer_input.send_keys(result)
        robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
        robot_checkbox.click()

        robots_rule_radio = browser.find_element(By.ID, "robotsRule")
        robots_rule_radio.click()

        submit_button = browser.find_element(By.CLASS_NAME, "btn-default")
        submit_button.click()
        wait = WebDriverWait(browser, 10)
        alert = wait.until(EC.alert_is_present())
        alert_text = Alert(browser).text

        expected_substring = "Congrats, you've passed the task!"
        assert expected_substring in alert_text, f"Ожидаемая строка '{expected_substring}' отсутствует в alert: '{alert_text}'"

        alert.accept()


def test_get_attribute(browser):
    # Открываем страницу
    url = "http://suninjuly.github.io/get_attribute.html"
    browser.get(url)

    # Находим элемент с id="treasure"
    treasure = browser.find_element(By.ID, "treasure")

    # Получаем значение атрибута valuex
    x_value = treasure.get_attribute("valuex")

    # Вычисляем математическое выражение
    result = calc(x_value)

    # Находим поле для ответа
    answer_input = browser.find_element(By.ID, "answer")

    # Вводим результат вычисления
    answer_input.send_keys(result)

    # Находим чекбокс "I'm the robot"
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")

    # Устанавливаем чекбокс
    robot_checkbox.click()

    # Находим радиокнопку "Robots rule"
    robots_rule_radio = browser.find_element(By.ID, "robotsRule")

    # Выбираем радиокнопку
    robots_rule_radio.click()

    # Находим кнопку Submit
    submit_button = browser.find_element(
        By.CLASS_NAME,
        "btn-default"
    )

    # Нажимаем Submit
    submit_button.click()

    # Создаём явное ожидание
    wait = WebDriverWait(browser, 10)

    # Ждём появления alert
    alert = wait.until(EC.alert_is_present())

    # Получаем текст alert
    alert_text = alert.text

    # Проверяем, что в alert есть ожидаемая строка
    expected_substring = "Congrats, you've passed the task!"

    assert expected_substring in alert_text, \
        f"Ожидаемая строка '{expected_substring}' отсутствует в alert: '{alert_text}'"

    # Закрываем alert
    alert.accept()





