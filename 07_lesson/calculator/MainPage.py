from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

basic_url = "https://bonigarcia.dev"


class MainPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            basic_url + "/selenium-webdriver-java/slow-calculator.html"
        )
        self._driver.implicitly_wait(5)
        self._driver.maximize_window()

    def delay_input_field(self, delay):
        delay_input = self._driver.find_element(
            By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    def mathematical_operation(self, number1, mat_operation, number2):
        self._driver.find_element(
            By.XPATH, f"//span[text()='{number1}']").click()
        self._driver.find_element(
            By.XPATH, f"//span[text()='{mat_operation}']").click()
        self._driver.find_element(
            By.XPATH, f"//span[text()='{number2}']").click()
        self._driver.find_element(
            By.XPATH, "//span[text()='=']").click()

    def wait_for_result(self, timeout=46):
        WebDriverWait(self._driver, timeout).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "")
        )

    def check_result(self):
        result_element = self._driver.find_element(
            By.CSS_SELECTOR, "[class='screen']")
        result_text = result_element.text
        return result_text
