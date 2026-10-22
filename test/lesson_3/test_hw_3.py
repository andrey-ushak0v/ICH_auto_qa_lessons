from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_implicitly_wating(driver):
    driver.implicitly_wait(10)
    driver.get("https://www.selenium.dev/selenium/web/dynamic.html")
    driver.find_element(By.ID, "adder").click()
    element = driver.find_element(By.ID, "box0")
    assert element.get_attribute("class") == "redbox"
    driver.quit()



def test_explicit_wating(driver):
    driver.get("https://www.selenium.dev/selenium/web/dynamic.html")
    wait = WebDriverWait(driver, 10)
    reveal_button = driver.find_element(By.ID, "reveal")
    reveal_button.click()
    element = wait.until(
        EC.visibility_of_element_located((By.ID, "revealed"))
    )
    element.send_keys("Hello Selenium")
    assert element.get_attribute("value") == "Hello Selenium"
    driver.quit()

def test_ajax_request(driver):
    driver.get("http://www.uitestingplayground.com/ajax")
    wait = WebDriverWait(driver, 20)  # Ожидание до 15 секунд

    # Нажимаем на кнопку, которая запускает AJAX-запрос
    ajax_button = driver.find_element(By.ID, "ajaxButton")
    ajax_button.click()
    # Ожидаем, пока появится элемент с классом "bg-success" и нужным текстом
    ajax_text = wait.until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "bg-success"), "Data loaded with AJAX get request."
        )
    )
    # Проверяем, что текст появился
    assert ajax_text, "Текст 'Data loaded with AJAX get request.' не появился!"


def test_ajax_request_implicit(driver):
    driver.implicitly_wait(20)  # Глобальное неявное ожидание до 15 секунд
    driver.get("http://www.uitestingplayground.com/ajax")

    # Нажимаем на кнопку AJAX-запроса
    ajax_button = driver.find_element(By.ID, "ajaxButton")
    ajax_button.click()
    # Ищем появившийся элемент (Selenium будет ждать до 15 секунд)
    ajax_text_element = driver.find_element(By.CLASS_NAME, "bg-success")

    # Проверяем, что текст внутри элемента соответствует ожидаемому
    assert "Data loaded with AJAX get request." in ajax_text_element.text, "Текст не загрузился!"


def test_wait_for_button(driver):
    wait = WebDriverWait(driver, 15)  # Ожидание до 15 секунд
    driver.get("http://www.uitestingplayground.com/loaddelay")

    # Ждём, пока кнопка появится на странице
    button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Button Appearing After Delay']")))

    # Проверяем, что кнопка действительно появилась
    assert button.is_displayed(), "Кнопка не появилась!"


def test_login_to_orangehrm(driver):
    wait = WebDriverWait(driver, 10)  # Явное ожидание до 10 секунд

    driver.get(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    )

    # Ждём, пока поле Username появится и станет видимым
    username_field = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "username")
        )
    )

    # Вводим имя пользователя
    username_field.send_keys("Admin")

    # Ждём появления поля Password
    password_field = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "password")
        )
    )

    # Вводим пароль
    password_field.send_keys("admin123")

    # Ждём, пока кнопка Login станет доступна для клика
    login_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit']")
        )
    )

    # Нажимаем кнопку Login
    login_button.click()

    # Ожидаем появления заголовка "Dashboard"
    dashboard_header = wait.until(
        EC.text_to_be_present_in_element(
            (By.TAG_NAME, "h6"),
            "Dashboard"
        )
    )

    # Проверяем, что заголовок содержит "Dashboard"
    assert dashboard_header, \
        "Текст заголовка не содержит 'Dashboard'"


def test_login_and_check_url(driver):
    wait = WebDriverWait(driver, 10)  # Явное ожидание до 10 секунд

    driver.get(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    )

    # Ждём, пока поле Username появится и станет видимым
    username_field = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "username")
        )
    )

    # Вводим имя пользователя
    username_field.send_keys("Admin")

    # Ждём появления поля Password
    password_field = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "password")
        )
    )

    # Вводим пароль
    password_field.send_keys("admin123")

    # Ждём, пока кнопка Login станет доступна для клика
    login_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit']")
        )
    )

    # Нажимаем кнопку Login
    login_button.click()

    # Ожидаем, пока URL изменится и будет содержать "dashboard"
    wait.until(
        EC.url_contains("dashboard")
    )

    # Проверяем, что в URL содержится "dashboard"
    assert "dashboard" in driver.current_url, \
        f"Ожидаемый URL не содержит 'dashboard': {driver.current_url}"


def test_slow_calculator(driver):
    wait = WebDriverWait(driver, 50)  # Ожидание результата
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Вводим задержку 45 секунд в поле #delay
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")
    # Нажимаем кнопки: 7, +, 8, =
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()
    # Ждём появления результата "15" через 45 секунд
    result_element = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    # Проверяем, что результат действительно 15
    assert result_element, "Ожидаемый результат '15' не отобразился!"


def test_data_types_form(driver):
    # Создаём явное ожидание.
    # Максимальное время ожидания каждого условия — 10 секунд.
    wait = WebDriverWait(driver, 10)

    # Открываем страницу с формой.
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    # ---------------------------------------------------------
    # FIRST NAME
    # ---------------------------------------------------------

    # Ищем поле по атрибуту name="first-name".
    #
    # visibility_of_element_located() ждёт, пока элемент:
    # 1. появится в DOM
    # 2. станет видимым для пользователя
    #
    # Это надёжнее, чем сразу делать find_element(),
    # потому что страница может ещё загружаться.
    first_name = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "first-name")
        )
    )

    # Вводим имя.
    first_name.send_keys("Hans")

    # ---------------------------------------------------------
    # LAST NAME
    # ---------------------------------------------------------

    last_name = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "last-name")
        )
    )

    # Вводим фамилию.
    last_name.send_keys("Schmidt")

    # ---------------------------------------------------------
    # ADDRESS
    # ---------------------------------------------------------

    address = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "address")
        )
    )

    # Вводим адрес.
    address.send_keys("Berliner Straße, 55-3")

    # ---------------------------------------------------------
    # E-MAIL
    # ---------------------------------------------------------

    # Обрати внимание:
    # здесь name именно "e-mail", а не "email".
    #
    # Это важно, потому что локатор должен точно
    # соответствовать HTML страницы.
    email = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "e-mail")
        )
    )

    # Вводим e-mail.
    email.send_keys("test@itch.de")

    # ---------------------------------------------------------
    # PHONE
    # ---------------------------------------------------------

    phone = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "phone")
        )
    )

    # Вводим номер телефона.
    phone.send_keys("+4917623456789")

    # ---------------------------------------------------------
    # ZIP CODE
    # ---------------------------------------------------------

    # ZIP code специально НЕ заполняем.
    #
    # По условию задания это поле должно остаться пустым.
    #
    # Поэтому здесь вообще не нужен send_keys().
    #
    # После нажатия Submit сайт должен показать это поле
    # красным цветом.
    #
    # Сам элемент мы найдём уже после отправки формы.

    # ---------------------------------------------------------
    # CITY
    # ---------------------------------------------------------

    city = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "city")
        )
    )

    # Вводим город.
    city.send_keys("Berlin")

    # ---------------------------------------------------------
    # COUNTRY
    # ---------------------------------------------------------

    country = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "country")
        )
    )

    # Вводим страну.
    country.send_keys("Deutschland")

    # ---------------------------------------------------------
    # JOB POSITION
    # ---------------------------------------------------------

    job_position = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "job-position")
        )
    )

    # Вводим должность.
    job_position.send_keys("QA")

    # ---------------------------------------------------------
    # COMPANY
    # ---------------------------------------------------------

    company = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "company")
        )
    )

    # Вводим название компании.
    company.send_keys("ITCH")

    # ---------------------------------------------------------
    # SUBMIT
    # ---------------------------------------------------------

    # Ищем кнопку Submit.
    #
    # Здесь используем presence_of_element_located(),
    # потому что нам достаточно, чтобы кнопка существовала
    # в DOM.
    #
    # Обычный .click() на этой странице может вызвать
    # ElementClickInterceptedException, поэтому используем
    # JavaScript click.
    submit_button = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "button[type='submit']")
        )
    )

    # Нажимаем кнопку через JavaScript.
    #
    # arguments[0] — это найденная Selenium кнопка.
    driver.execute_script(
        "arguments[0].click();",
        submit_button
    )

    # ---------------------------------------------------------
    # WAIT FOR RESULT PAGE
    # ---------------------------------------------------------

    # После Submit форма отправляет GET-запрос и браузер
    # переходит на:
    #
    # data-types-submitted.html
    #
    # Поэтому сначала ждём именно перехода на эту страницу.
    wait.until(
        EC.url_contains("data-types-submitted.html")
    )

    # ---------------------------------------------------------
    # CHECK ZIP CODE
    # ---------------------------------------------------------

    # На странице результата HTML уже отличается.
    #
    # На исходной странице поле было:
    #
    # <input name="zip-code">
    #
    # А на странице результата:
    #
    # <div id="zip-code" class="alert py-2 alert-danger">
    #
    # Поэтому здесь используем By.ID, а не By.NAME.
    zip_code = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "zip-code")
        )
    )

    # Так как ZIP code мы оставили пустым,
    # JavaScript сайта добавляет класс:
    #
    # alert-danger
    #
    # Проверяем, что этот класс действительно присутствует.
    assert "alert-danger" in zip_code.get_attribute("class"), \
        "Zip code не подсвечен красным!"

    # ---------------------------------------------------------
    # CHECK ALL VALID FIELDS
    # ---------------------------------------------------------

    # Список всех полей, которые мы заполнили.
    #
    # Zip code сюда НЕ включаем,
    # потому что он должен быть красным.
    valid_fields = [
        "first-name",
        "last-name",
        "address",
        "city",
        "country",
        "e-mail",
        "phone",
        "job-position",
        "company",
    ]

    # Проходим по каждому полю из списка.
    for field_id in valid_fields:

        # На странице результата каждое поле представлено
        # отдельным <div> с соответствующим id.
        #
        # Например:
        #
        # <div id="first-name"
        #      class="alert py-2 alert-success">
        #
        # Поэтому используем By.ID.
        field = wait.until(
            EC.visibility_of_element_located(
                (By.ID, field_id)
            )
        )

        # Проверяем, что сайт добавил класс alert-success.
        #
        # alert-success означает, что значение поля
        # было передано и отображается как корректное.
        assert "alert-success" in field.get_attribute("class"), \
            f"Поле {field_id} не подсвечено зелёным!"