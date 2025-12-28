"""
Page Object для страницы калькулятора
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

basic_url = "https://bonigarcia.dev"


class MainPage:
    """Класс для работы с главной страницей калькулятора"""

    def __init__(self, driver):
        """
        Инициализация страницы

        :param driver: WebDriver экземпляр
        :type driver: webdriver.Chrome
        """
        self._driver = driver
        self._driver.get(
            basic_url + "/selenium-webdriver-java/slow-calculator.html"
        )
        self._driver.implicitly_wait(5)
        self._driver.maximize_window()

    @allure.step("Установить задержку калькулятора: {delay}")
    def delay_input_field(self, delay: str) -> None:
        """
        Устанавливает значение задержки в поле ввода

        :param delay: Значение задержки в секундах
        :type delay: str
        :return: None
        """
        delay_input = self._driver.find_element(
            By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    @allure.step("Выполнить математическую операцию: "
                 "{number1} {mat_operation} {number2}")
    def mathematical_operation(
            self,
            number1: str,
            mat_operation: str,
            number2: str) -> None:
        """
        Выполняет математическую операцию на калькуляторе

        :param number1: Первое число
        :type number1: str
        :param mat_operation: Математическая операция (+, -, *, /)
        :type mat_operation: str
        :param number2: Второе число
        :type number2: str
        :return: None
        """
        self._driver.find_element(
            By.XPATH, f"//span[text()='{number1}']").click()
        self._driver.find_element(
            By.XPATH, f"//span[text()='{mat_operation}']").click()
        self._driver.find_element(
            By.XPATH, f"//span[text()='{number2}']").click()
        self._driver.find_element(
            By.XPATH, "//span[text()='=']").click()

    @allure.step("Ожидать результат вычислений (таймаут: {timeout} сек)")
    def wait_for_result(self, timeout: int = 46) -> None:
        """
        Ожидает появления результата на экране калькулятора

        :param timeout: Максимальное время ожидания в секундах
        :type timeout: int
        :return: None
        """

        WebDriverWait(self._driver, timeout).until(
            EC.invisibility_of_element_located(
                (By.CSS_SELECTOR, "[role='status']")))

    @allure.step("Получить результат вычислений")
    def check_result(self) -> str:
        """
        Получает текст результата с экрана калькулятора

        :return: Текст результата
        :rtype: str
        """
        result_element = self._driver.find_element(
            By.CSS_SELECTOR, "[class='screen']")
        result_text = result_element.text
        return result_text
