from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(10)
start_time = time.time()
driver.get('http://www.seleniumframework.com/Practiceform/')
# time.sleep(5)
element = driver.find_element_by_id('periodicElement')

print(element.text)
print(time.time() - start_time)
driver.close()