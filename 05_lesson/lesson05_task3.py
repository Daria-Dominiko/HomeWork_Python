from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
input_field.click()

input_field.send_keys("Sky")
input_field.clear()

input_field.send_keys("Pro")

driver.quit()
