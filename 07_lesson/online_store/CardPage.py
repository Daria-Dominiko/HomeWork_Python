from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CardPage:
    def __init__(self, driver):
        self._driver = driver

    def checkout(self):
        checkout_button = self._driver.find_element(By.ID, "checkout")
        checkout_button.click()
