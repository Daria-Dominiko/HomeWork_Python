from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from AuthorizationPage import AuthorizationPage
from MainPage import MainPage
from CardPage import CardPage
from MakingToOrderPage import OrderPage

def test_efficiency_online_store():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    authorization_page = AuthorizationPage(driver)
    authorization_page.authorization()

    main_page = MainPage(driver)
    main_page.add_to_cart()

    card_page = CardPage(driver)
    card_page.checkout()

    order_page = OrderPage(driver)
    order_page.make_order()

    total_text = order_page.check_total()

    driver.quit()

    assert total_text == "Total: $58.29"

