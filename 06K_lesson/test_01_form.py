# from selenium import webdriver
# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# def test_form():
#     service = EdgeService()
#     driver = webdriver.Edge(service=service)
#     driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
#
#     waiter = WebDriverWait(driver, 15)
#
#     driver.find_element(By.CSS_SELECTOR, "[name='first-name']").send_keys("Иван")
#     driver.find_element(By.CSS_SELECTOR, "[name='last-name']").send_keys("Петров")
#     driver.find_element(By.CSS_SELECTOR, "[name='address']").send_keys("Ленина, 55-3")
#     driver.find_element(By.CSS_SELECTOR, "[name='e-mail']").send_keys("test@skypro.com")
#     driver.find_element(By.CSS_SELECTOR, "[name='phone']").send_keys("+7985899998787")
#     driver.find_element(By.CSS_SELECTOR, "[name='city']").send_keys("Москва")
#     driver.find_element(By.CSS_SELECTOR, "[name='country']").send_keys("Россия")
#     driver.find_element(By.CSS_SELECTOR, "[name='job-position']").send_keys("QA")
#     driver.find_element(By.CSS_SELECTOR, "[name='company']").send_keys("SkyPro")
#
#     driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
#
#     assert "alert-danger" in driver.find_element(By.CSS_SELECTOR, "#zip-code").get_attribute("class")
#
#     assert "alert-success" in driver.find_element(By.CSS_SELECTOR, "#first-name").get_attribute("class")
#     assert "alert-success" in driver.find_element(By.CSS_SELECTOR, "#last-name").get_attribute("class")
#     assert "alert-success" in driver.find_element(By.CSS_SELECTOR, "#address").get_attribute("class")
#     assert "alert-success" in driver.find_element(By.CSS_SELECTOR, "#e-mail").get_attribute("class")
#     assert "alert-success" in driver.find_element(By.CSS_SELECTOR, "#phone").get_attribute("class")
#     assert "alert-success" in driver.find_element(By.CSS_SELECTOR, "#city").get_attribute("class")
#     assert "alert-success" in driver.find_element(By.CSS_SELECTOR, "#country").get_attribute("class")
#     assert "alert-success" in driver.find_element(By.CSS_SELECTOR, "#job-position").get_attribute("class")
#     assert "alert-success" in driver.find_element(By.CSS_SELECTOR, "#company").get_attribute("class")
#
#     driver.quit()
#