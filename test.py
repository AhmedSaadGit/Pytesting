import os
import time
from selenium import webdriver

    #setting up the chrome driver 
os.environ['PATH'] += r"./"
driver = webdriver.Chrome()

driver.get("https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal")

#time.sleep(3)
driver.implicitly_wait(30) #apply across all /waiting for the element to charge for 30 s , once charged click immediatly
HomeElement = driver.find_element_by_id("n-thema")
HomeElement.click()

TextSourceElement = driver.find_element_by_class_name("mw-list-item")
print(f"{TextSourceElement} Hello world ")

driver.close


