from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/droppable/")
actions = ActionChains(driver)
iframe = driver.find_element(By.CLASS_NAME, 'demo-frame')
driver.switch_to.frame(iframe)

source = driver.find_element(By.ID, 'draggable')
target = driver.find_element(By.ID, 'droppable')

time.sleep(2)

actions.drag_and_drop(source, target).perform()
time.sleep(2)
