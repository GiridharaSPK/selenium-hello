from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./chromedriver')

driver.get('https://www.seleniumeasy.com/test/dynamic-data-loading-demo.html')

# button = driver.find_element_by_id('save')
button = driver.find_element(By.ID, 'save')

button.click()
time.sleep(5)

details = driver.find_element_by_id("loading")

print(details.text)

driver.close()