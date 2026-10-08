from selenium import webdriver

# Открываем браузер
driver = webdriver.Chrome()
driver.get("https://example.com")

# Открываем новую вкладку
driver.execute_script("window.open('https://google.com', '_blank');")

tabs = driver.window_handles
print("Идентификаторы вкладок:", tabs)

# Переключаемся на вторую вкладку (Google)
driver.switch_to.window(tabs[1])
print("Текущая вкладка:", driver.current_window_handle)
# Закрываем вторую вкладку
driver.close()

# Переключаемся обратно на первую вкладку
driver.switch_to.window(tabs[0])
print("Вернулись на вкладку:", driver.current_window_handle)


