"""
Тесты для калькулятора с интеграцией Allure
"""
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from MainPage import MainPage


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка работы калькулятора с задержкой")
@allure.description("""
    Тест проверяет корректность работы калькулятора:
    1. Установка задержки вычислений
    2. Выполнение математической операции
    3. Ожидание результата
    4. Проверка корректности результата
""")
def test_checking_calculator():
    """Тест проверки работы калькулятора с задержкой"""

    # Инициализация драйвера
    with (allure.step("Инициализация Chrome драйвера")):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

    # Создание объекта страницы
    main_page = MainPage(driver)

    # Установка задержки
    with allure.step("Установка задержки вычислений"):
        main_page.delay_input_field("45")

    # Выполнение операции
    with allure.step("Выполнение математической операции: 7 + 8"):
        main_page.mathematical_operation('7', '+', '8')

    # Ожидание результата
    with allure.step("Ожидание результата вычислений"):
        main_page.wait_for_result(46)

    # Проверка результата
    with allure.step("Проверка результата вычислений"):
        result_text = main_page.check_result()

    # Assert с Allure аннотацией
    with allure.step(f'Проверить что результат равен \'15\' (фактический: '
                     f'{result_text})'):
        assert result_text == "15", (f"Ожидалось '15', получено "
                                     f'\'{result_text}\'')

    # Закрытие драйвера
    with allure.step("Закрытие браузера"):
        driver.quit()
