#from selenium.webdriver.common.by import By
#from pages.login_page import LoginPage
#
#
#def test_success_login_valid_data(driver):
#    """Проверяет успешный вход с корректными учетными данными."""
#    user_name_input_field = driver.find_element(By.ID, "user-name")
#    user_name_input_field.send_keys("standard_user")
#    password_input_field = driver.find_element(By.ID, "password")
#    password_input_field.send_keys("secret_sauce")
#    login_button = driver.find_element(By.ID, "login-button")
#    login_button.click()
#    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Не удалось войти в систему."
#    inventory_list = driver.find_element(By.CLASS_NAME, "inventory_list")
#    assert inventory_list, "Список товаров не найден на странице."
#
#
#def test_invalid_password(driver):
#    """Проверяет отображение ошибки при вводе неверного пароля."""
#    user_name_input_field = driver.find_element(By.ID, "user-name")
#    user_name_input_field.send_keys("standard_user")
#    password_input_field = driver.find_element(By.ID, "password")
#    password_input_field.send_keys("wrong_password")
#    login_button = driver.find_element(By.ID, "login-button")
#    login_button.click()
#    error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
#    assert error_message, "Сообщение об ошибке не отображается."
#    assert "Username and password do not match" in error_message.text, "Неверное сообщение об ошибке."
#
#
#def test_locked_out_user(driver):
#    """Проверяет невозможность входа заблокированного пользователя."""
#    user_name_input_field = driver.find_element(By.ID, "user-name")
#    user_name_input_field.send_keys("locked_out_user")
#    password_input_field = driver.find_element(By.ID, "password")
#    password_input_field.send_keys("secret_sauce")
#    login_button = driver.find_element(By.ID, "login-button")
#    login_button.click()
#    error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
#    assert error_message, "Сообщение об ошибке не отображается."
#    assert "Sorry, this user has been locked out." in error_message.text, "Неверное сообщение об ошибке."
#
#
#def test_empty_username(driver):
#    """Проверяет отображение ошибки при пустом поле имени пользователя."""
#    password_input_field = driver.find_element(By.ID, "password")
#    password_input_field.send_keys("secret_sauce")
#    login_button = driver.find_element(By.ID, "login-button")
#    login_button.click()
#    error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
#    assert error_message, "Сообщение об ошибке не отображается."
#    assert "Username is required" in error_message.text, "Неверное сообщение об ошибке."
#
#
#def test_empty_password(driver):
#    """Проверяет отображение ошибки при пустом поле пароля."""
#    user_name_input_field = driver.find_element(By.ID, "user-name")
#    user_name_input_field.send_keys("standard_user")
#    login_button = driver.find_element(By.ID, "login-button")
#    login_button.click()
#    error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
#    assert error_message, "Сообщение об ошибке не отображается."
#    assert "Password is required" in error_message.text, "Неверное сообщение об ошибке."
#
#
#
#
#
#
#def test_successful_login(driver):
#    login_page = LoginPage(driver)
#    login_page.enter_username("standard_user")
#    login_page.enter_password("secret_sauce")
#    login_page.click_on_login_button()
#    assert "inventory.html" in driver.current_url, "Не удалось войти в систему."
#
#def test_invalid_password(driver):
#    login_page = LoginPage(driver)
#    login_page.enter_username("standard_user")
#    login_page.enter_password("wrong_password")
#    login_page.click_on_login_button()
#    assert "Username and password do not match" in login_page.error_message(), "Неверное сообщение об ошибке."
#
#
#def test_locked_out_user(driver):
#    login_page = LoginPage(driver)
#    login_page.enter_username("locked_out_user")
#    login_page.enter_password("secret_sauce")
#    login_page.click_on_login_button()
#    assert "Sorry, this user has been locked out." in login_page.error_message(), "Неверное сообщение об ошибке."
#
#
#def test_empty_username(driver):
#    login_page = LoginPage(driver)
#    login_page.enter_password("secret_sauce")
#    login_page.click_on_login_button()
#    assert "Username is required" in login_page.error_message(), "Неверное сообщение об ошибке."
#
#
#def test_empty_password(driver):
#    login_page = LoginPage(driver)
#    login_page.enter_username("standard_user")
#    login_page.click_on_login_button()
#    assert "Password is required" in login_page.error_message(), "Неверное сообщение об ошибке."


# новые тесты



# ------------------- ДОПОЛНИТЕЛЬНЫЕ ТЕСТЫ -------------------


def test_filter_booking_by_name(api, sample_booking):
    """Тест 1: фильтрация бронирований по имени и фамилии"""

    # sample_booking — фикстура, которая возвращает словарь с тестовыми данными.
    # Создаём бронирование с уникальными именем и фамилией,
    # чтобы отличить его от других записей на сервере.
    #
    # Важно: здесь используется копия словаря, чтобы не изменять
    # исходные тестовые данные фикстуры.
    booking_data = sample_booking.copy()
    booking_data["firstname"] = "FilterTestAlex"
    booking_data["lastname"] = "FilterTestSmith"

    # Отправляем POST-запрос на создание бронирования.
    # В метод передаём словарь booking_data, который будет отправлен
    # в теле HTTP-запроса в формате JSON.
    #
    # Метод create_booking возвращает JSON-ответ в виде Python-словаря.
    created = api.create_booking(booking_data)

    # Из ответа сервера извлекаем ID созданного бронирования.
    # Этот ID понадобится, чтобы проверить, нашла ли фильтрация
    # именно созданную нами запись.
    booking_id = created["bookingid"]

    # Формируем параметры фильтрации.
    # Ключи firstname и lastname — названия параметров API,
    # значения — имя и фамилия, по которым ищем бронирование.
    params = {
        "firstname": "FilterTestAlex",
        "lastname": "FilterTestSmith"
    }

    # Вызываем GET /booking с параметрами фильтрации.
    # requests передаст params в URL как query-параметры:
    # /booking?firstname=FilterTestAlex&lastname=FilterTestSmith
    #
    # Метод get_booking_ids возвращает список словарей с bookingid.
    booking_ids = api.get_booking_ids(params)

    # Создаём список только из ID найденных бронирований.
    # В каждом элементе booking_ids находится словарь,
    # например {"bookingid": 123}.
    found_ids = [item["bookingid"] for item in booking_ids]

    # Проверяем, что ID нашего бронирования присутствует в результатах.
    # Если ID отсутствует, pytest завершит тест с ошибкой.
    assert booking_id in found_ids, (
        "Бронирование не найдено при фильтрации по имени и фамилии"
    )


def test_get_nonexistent_booking(api):
    """Тест 2: получение несуществующего бронирования"""

    # Отправляем GET-запрос на получение списка бронирований.
    # Без параметров фильтрации API возвращает список доступных ID.
    booking_ids = api.get_booking_ids()

    # Из списка словарей извлекаем все ID в отдельный список.
    # Пример результата: [1, 2, 3, 4].
    existing_ids = [item["bookingid"] for item in booking_ids]

    # Выбираем ID, который значительно превышает максимальный
    # ID из полученного списка.
    #
    # max(existing_ids) возвращает наибольший ID.
    # Если список пустой, default=0 позволит использовать 0.
    # Прибавляем 100000, чтобы выбрать ID за пределами текущего диапазона.
    nonexistent_id = max(existing_ids, default=0) + 100000

    # Отправляем GET-запрос на получение бронирования по выбранному ID.
    # Ответ сохраняем в resp, чтобы проверить HTTP-статус.
    resp = api.get_booking(nonexistent_id)

    # Ожидаем HTTP 404 Not Found — бронирование не найдено.
    # Если сервер вернёт другой статус, тест завершится ошибкой.
    assert resp.status_code == 404, (
        f"Ожидался статус 404, получен {resp.status_code}"
    )


def test_update_booking_without_token(api, sample_booking):
    """Тест 3: попытка обновления без авторизации"""

    # Создаём бронирование, которое будем использовать в тесте.
    # Для PUT необходимо иметь существующую запись.
    created = api.create_booking(sample_booking)

    # Получаем ID созданного бронирования из ответа сервера.
    booking_id = created["bookingid"]

    # Создаём полный набор данных для PUT.
    # Оператор ** распаковывает словарь sample_booking:
    # все его ключи и значения копируются в новый словарь.
    #
    # Затем lastname переопределяется значением UnauthorizedUpdate.
    # При этом исходный sample_booking не изменяется.
    updated_payload = {
        **sample_booking,
        "lastname": "UnauthorizedUpdate"
    }

    # Вызываем метод полного обновления PUT.
    # Передаём пустую строку вместо токена.
    #
    # Внутри update_booking заголовок Cookie будет сформирован
    # как "token=", поэтому запрос не содержит действительного токена.
    resp = api.update_booking(
        booking_id,
        updated_payload,
        token=""
    )

    # Проверяем, что сервер отклонил запрос без авторизации.
    # Для Restful-Booker ожидается статус 403 Forbidden.
    assert resp.status_code == 403, (
        f"Ожидался статус 403, получен {resp.status_code}"
    )

    # После неудачного PUT дополнительно проверяем состояние записи.
    # Выполняем GET-запрос по тому же ID.
    get_resp = api.get_booking(booking_id)

    # Убеждаемся, что бронирование по-прежнему существует.
    assert get_resp.status_code == 200

    # Извлекаем JSON-тело ответа в виде словаря.
    # Проверяем, что фамилия осталась исходной.
    # Это подтверждает, что попытка обновления не изменила данные.
    assert get_resp.json()["lastname"] == sample_booking["lastname"]


def test_update_booking_with_invalid_token(api, sample_booking):
    """Тест 4: попытка обновления с неверным токеном"""

    # Создаём бронирование, которое будем пытаться изменить.
    created = api.create_booking(sample_booking)

    # Извлекаем ID созданной записи.
    booking_id = created["bookingid"]

    # Создаём строку, которая не является действительным токеном.
    # Она нужна для проверки обработки неверных учётных данных.
    invalid_token = "invalid_token_12345"

    # Формируем полный набор данных для PUT.
    # Все исходные поля сохраняются, но фамилия заменяется
    # на новое значение, чтобы можно было обнаружить изменение.
    updated_payload = {
        **sample_booking,
        "lastname": "InvalidTokenUpdate"
    }

    # Отправляем PUT-запрос с неверным токеном.
    # Метод update_booking поместит его в HTTP-заголовок Cookie.
    resp = api.update_booking(
        booking_id,
        updated_payload,
        invalid_token
    )

    # Проверяем, что сервер запрещает обновление с неверным токеном.
    # Ожидаемый статус — 403 Forbidden.
    assert resp.status_code == 403, (
        f"Ожидался статус 403, получен {resp.status_code}"
    )

    # Повторно запрашиваем бронирование, чтобы убедиться,
    # что после отклонённого PUT запись осталась доступной.
    get_resp = api.get_booking(booking_id)

    # Проверяем успешное получение исходной записи.
    assert get_resp.status_code == 200

    # Убеждаемся, что фамилия не поменялась на InvalidTokenUpdate.
    # Сравниваем её с исходным значением из фикстуры.
    assert get_resp.json()["lastname"] == sample_booking["lastname"]


def test_partial_update_preserves_unchanged_fields(
    api, auth_token, sample_booking
):
    """Тест 5: PATCH изменяет только указанные поля"""

    # Создаём бронирование с исходными тестовыми данными.
    # Сохраняем ответ сервера, чтобы получить ID записи.
    created = api.create_booking(sample_booking)

    # Извлекаем ID бронирования, которое будем обновлять.
    booking_id = created["bookingid"]

    # Формируем тело PATCH-запроса.
    # В отличие от PUT, здесь указываем только поля,
    # которые хотим изменить: firstname и totalprice.
    patch_payload = {
        "firstname": "PatchTestAlex",
        "totalprice": 777
    }

    # Отправляем PATCH-запрос.
    # api — объект BookerApi.
    # partial_update_booking принимает ID записи, данные изменений
    # и токен авторизации, полученный из фикстуры auth_token.
    resp = api.partial_update_booking(
        booking_id,
        patch_payload,
        auth_token
    )

    # Проверяем, что сервер успешно выполнил частичное обновление.
    # Для успешного PATCH ожидается статус 200 OK.
    assert resp.status_code == 200

    # Преобразуем JSON-ответ сервера в Python-словарь.
    # В updated_data должны находиться актуальные данные бронирования.
    updated_data = resp.json()

    # Проверяем первое изменённое поле.
    # Имя должно соответствовать значению из patch_payload.
    assert updated_data["firstname"] == "PatchTestAlex"

    # Проверяем второе изменённое поле.
    # Цена должна быть равна 777, а не исходной цене.
    assert updated_data["totalprice"] == 777

    # Проверяем, что фамилия не изменилась.
    # PATCH не передавал поле lastname, поэтому ожидаем исходное значение.
    assert updated_data["lastname"] == sample_booking["lastname"]

    # Проверяем, что флаг оплаты сохранился.
    # В PATCH-запросе поле depositpaid отсутствовало.
    assert updated_data["depositpaid"] == sample_booking["depositpaid"]

    # Проверяем, что даты заезда и выезда остались прежними.
    # Сравниваем вложенный словарь целиком.
    assert updated_data["bookingdates"] == sample_booking["bookingdates"]

    # Проверяем, что дополнительные пожелания не изменились.
    # Поле additionalneeds также отсутствовало в PATCH-запросе.
    assert updated_data["additionalneeds"] == sample_booking["additionalneeds"]


def test_get_booking_response_structure(api, sample_booking):
    """Тест 7: проверка структуры ответа при получении бронирования."""

    # Создаём новое бронирование, чтобы получить существующий ID.
    created_booking = api.create_booking(sample_booking)
    booking_id = created_booking["bookingid"]

    # Запрашиваем созданное бронирование по его ID.
    resp = api.get_booking(booking_id)

    # Проверяем, что запрос завершился успешно.
    assert resp.status_code == 200, (
        f"Ожидался статус 200, получен {resp.status_code}"
    )

    # Преобразуем JSON-ответ сервера в Python-словарь.
    booking_data = resp.json()

    # Проверяем наличие всех обязательных полей бронирования.
    expected_fields = {
        "firstname",
        "lastname",
        "totalprice",
        "depositpaid",
        "bookingdates",
        "additionalneeds"
    }

    assert expected_fields.issubset(booking_data.keys()), (
        f"В ответе отсутствуют обязательные поля: "
        f"{expected_fields - booking_data.keys()}"
    )

    # Проверяем, что даты заезда и выезда представлены отдельными полями.
    assert "checkin" in booking_data["bookingdates"], (
        "В ответе отсутствует дата заезда checkin"
    )
    assert "checkout" in booking_data["bookingdates"], (
        "В ответе отсутствует дата выезда checkout"
    )






