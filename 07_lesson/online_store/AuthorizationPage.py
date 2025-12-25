from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthorizationPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(5)
        self._driver.maximize_window()

    def authorization(self):
        username_input = self._driver.find_element(By.ID, "user-name")
        password_input = self._driver.find_element(By.ID, "password")
        login_button = self._driver.find_element(By.ID, "login-button")

        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")
        login_button.click()

        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
        )
