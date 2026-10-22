import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Фикстура для WebDriver
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


# Тест на hover и проверку заголовка
def test_hover_menu(browser):
    url = "https://crossbrowsertesting.github.io/hover-menu.html"
    browser.get(url)

    # Создаем объект ActionChains для работы с движением мыши
    actions = ActionChains(browser)

    # Находим пункт "Dropdown"
    dropdown = browser.find_element(By.LINK_TEXT, "Dropdown")

    # Наводим курсор на "Dropdown"
    actions.move_to_element(dropdown).perform()

    # Находим пункт "Secondary Menu"
    secondary_menu = browser.find_element(
        By.LINK_TEXT,
        "Secondary Menu"
    )

    # Наводим курсор на "Secondary Menu"
    actions.move_to_element(secondary_menu).perform()

    # Находим пункт "Secondary Action"
    secondary_action = browser.find_element(
        By.LINK_TEXT,
        "Secondary Action"
    )

    # Кликаем на "Secondary Action"
    secondary_action.click()

    # Сдвигаем мышку немного вниз,
    # чтобы курсор ушел с меню

    # Создаем явное ожидание
    wait = WebDriverWait(browser, 10)

    # Ждем, пока станет видимым h1 именно внутри
    # блока с классом secondary-clicked
    header = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".secondary-clicked h1")
        )
    )

    # Проверяем, что заголовок действительно "Secondary Page"
    assert header.text == "Secondary Page", \
        f"Заголовок не совпадает, найдено: {header.text}"


# Тест для drag and drop
def test_drag_and_drop(browser):
    url = "https://crossbrowsertesting.github.io/drag-and-drop.html"
    browser.get(url)

    # Находим элементы
    draggable = browser.find_element(By.ID, "draggable")  # Что перетаскиваем
    droppable = browser.find_element(By.ID, "droppable")  # Куда перетаскиваем
    # Создаем объект ActionChains
    actions = ActionChains(browser)

    # Выполняем drag and drop
    actions.drag_and_drop(draggable, droppable).perform()
    # Ожидаем, что текст в droppable изменится на "Dropped!"
    wait = WebDriverWait(browser, 5)
    dropped_text = wait.until(EC.text_to_be_present_in_element((By.ID, "droppable"), "Dropped!"))

    # Проверяем результат
    assert dropped_text, "Текст в droppable не изменился на 'Dropped!'"


