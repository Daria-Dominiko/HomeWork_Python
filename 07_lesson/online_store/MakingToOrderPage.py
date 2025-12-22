from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage:
    def __init__(self, driver):
        self._driver = driver

    def make_order(self):
        first_name_input = self._driver.find_element(By.ID, "first-name")
        last_name_input = self._driver.find_element(By.ID, "last-name")
        postal_code_input = self._driver.find_element(By.ID, "postal-code")

        first_name_input.send_keys("Иван")
        last_name_input.send_keys("Петров")
        postal_code_input.send_keys("123456")

        continue_button = self._driver.find_element(By.ID, "continue")
        continue_button.click()

        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
    def check_total(self):
        total_element = self._driver.find_element(By.CSS_SELECTOR, ".summary_total_label")
        total_text = total_element.text
        return total_text
