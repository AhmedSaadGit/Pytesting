import time
from selenium import webdriver



driver = webdriver.Chrome(".venv\chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://google.com")



