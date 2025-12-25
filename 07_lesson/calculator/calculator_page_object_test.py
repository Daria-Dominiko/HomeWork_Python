from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calcuiator.MainPage import MainPage


def test_checking_calculator():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    main_page = MainPage(driver)
    main_page.delay_input_field("45")

    main_page.mathematical_operation('7', '+', '8')

    main_page.wait_for_result(46)

    result_text = main_page.check_result()
    assert result_text == "15"

    driver.quit()
