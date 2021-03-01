from selenium import webdriver

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')

driver.get('https://www.google.com')

input = driver.find_element_by_name('q')
input.send_keys("hello world"+Keys.RETURN)

logo = driver.find_element_by_id('logo')
logo.click()

driver.quit()
