from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.google.com")

time.sleep(2)

driver.get("https://www.addverb.com")
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.close()
