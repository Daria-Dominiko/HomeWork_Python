from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

input_username = driver.find_element(By.CSS_SELECTOR, "[name=username]")
input_username.click()
input_username.send_keys("tomsmith")

input_password = driver.find_element(By.CSS_SELECTOR, "[name=password]")
input_password.click()
input_password.send_keys("SuperSecretPassword!")

driver.find_element(By.CSS_SELECTOR, ".fa.fa-2x.fa-sign-in").click()

title = driver.find_element(By.CSS_SELECTOR, ".flash.success")
print(f" {title.text}")

driver.quit()
