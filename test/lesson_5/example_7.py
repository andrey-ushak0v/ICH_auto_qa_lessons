from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Открываем браузер и переходим на страницу
url = "https://www.globalsqa.com/demo-site/draganddrop/"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()


iframe = driver.find_element(By.CSS_SELECTOR, "iframe[src*='photo-manager']")
driver.switch_to.frame(iframe)

photo = driver.find_element(By.XPATH, '//ul[@id="gallery"]/li[1]')
trash = driver.find_element(By.ID, 'trash')

actions = ActionChains(driver)
actions.drag_and_drop(photo, trash).perform()

time.sleep(2)

# Проверяем количество фотографий в корзине
photos_in_trash = len(
    driver.find_elements(
        By.XPATH,
        "//div[@id='trash']//ul/li"
    )
)

# Проверяем количество фотографий в галерее
photos_in_gallery = len(
    driver.find_elements(
        By.XPATH,
        "//ul[@id='gallery']/li"
    )
)
assert photos_in_trash == 1
assert photos_in_gallery == 3

driver.quit()



