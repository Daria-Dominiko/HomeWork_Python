from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self._driver = driver

    def add_to_cart(self):
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

        cart_icon = self._driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()

        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.ID, "checkout"))
        )
