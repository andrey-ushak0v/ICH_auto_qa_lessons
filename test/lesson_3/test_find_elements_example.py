from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
from urls import CAT_MEMES
from locators import xpath_id_cat_bullet, xpath_name_cat_vova


#driver = webdriver.Chrome()
#driver.get("https://the-internet.herokuapp.com/forgot_password")
#
#form = driver.find_element(By.CSS_SELECTOR, "#forgot_password")
#print(form.text)
#
#element_by_xpath = driver.find_element(By.XPATH, '//*[@id="form_submit"]')
#print(element_by_xpath.text)

#@pytest.fixture
#def driver():
#    driver = webdriver.Chrome()
#    driver.get(CAT_MEMES)
#    yield driver
#    driver.quit()


#def test_displayed_cat_bullet(driver):
#    cat_bullet = driver.find_element(By.XPATH, xpath_id_cat_bullet)
#    assert cat_bullet.is_displayed() is True
#
#def test_displayed_cat_name_vova(driver):
#    cat_vova = driver.find_element(By.XPATH, xpath_name_cat_vova)
#    assert cat_vova.is_displayed() is True
#
#def test_find_all_cats(driver):
#    cats = driver.find_elements(By.CLASS_NAME, "card")
#    #assert '9 mins' in (cats[1].text)
#    print(cats[0].text)


#def test_find_title(driver):
#    title_text = driver.find_element(By.TAG_NAME, 'h1').text
#    assert title_text == 'Cat memes'


#def test_find_album(driver):
#    assert driver.find_element(By.XPATH, "/html/body/header/div/div/a/strong").text == 'Cats album'






#/html/body/main/div/div/div/div[5]/div/div/div/div/button[1]

def test_login():
    driver = webdriver.Chrome()
    driver.get("http://the-internet.herokuapp.com/login")
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")

    username_field = driver.find_element(By.ID, "password")
    username_field.send_keys("SuperSecretPassword!")

    login_button = driver.find_element(By.CLASS_NAME, 'fa-sign-in')
    login_button.click()
    time.sleep(5)
    #assert driver.find_element(By.LINK_TEXT, 'Welcome to the Secure Area. When you are done click logout below.')
    assert driver.find_element(
        By.XPATH,
        "//h4[text()='Welcome to the Secure Area. When you are done click logout below.']"
    )


#





