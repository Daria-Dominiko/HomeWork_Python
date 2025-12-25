from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))
    driver.get("https://www.saucedemo.com/")

    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
    )

    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-onesie").click()

    cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_icon.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "checkout"))
    )

    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()

    first_name_input = driver.find_element(By.ID, "first-name")
    last_name_input = driver.find_element(By.ID, "last-name")
    postal_code_input = driver.find_element(By.ID, "postal-code")

    first_name_input.send_keys("Иван")
    last_name_input.send_keys("Петров")
    postal_code_input.send_keys("123456")

    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )

    total_element = driver.find_element(
        By.CSS_SELECTOR, ".summary_total_label")
    total_text = total_element.text
    assert total_text == "Total: $58.29"

    driver.quit()

