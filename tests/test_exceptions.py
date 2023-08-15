import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestExceptions:
    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        chrome_driver_path = 'C:\\Users\\admin\\Desktop\\drivers\\chromedriver.exe'
        service = ChromeService(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(service=service)
        time.sleep(5)
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()
        row_2_input_element = driver.find_element(By.ID, "row2")
        assert row_2_input_element.is_displayed(), "Row 2 input should be displayed, but it's not"

    @pytest.mark.exceptions
    def test_element_not_interactable_exception(self, driver):
        chrome_driver_path = 'C:\\Users\\admin\\Desktop\\drivers\\chromedriver.exe'
        service = ChromeService(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(service=service)
        time.sleep(5)
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        add_button_locator = driver.find_element(By.XPATH, "//button[@id='add_btn']")
        add_button_locator.click()
        wait = WebDriverWait(driver, 10)
        row_2_input_element = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))
        assert row_2_input_element.is_displayed()

        field_input = driver.find_element(By.XPATH, "(//input[contains(@type,'text')])[2]")
        field_input.send_keys("Tacos")

        save_btn = driver.find_element(By.NAME, "Save")
        save_btn.click()

        confirm = driver.find_element(By.ID, "confirmation")
        assert confirm.is_displayed(), "probando que esto funciona"

    @pytest.mark.exceptions
    def test_invalid_element_state_exception(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        input_locator = driver.find_element(By.XPATH, "//input[contains(@value,'Pizza')]")
        input_locator.clear()
        input_locator.send_keys("Tacos")
        assert input_locator.text == "Tacos"

    @pytest.mark.exceptions
    def test_element_reference_exception(self, driver):
        chrome_driver_path = 'C:\\Users\\admin\\Desktop\\drivers\\chromedriver.exe'
        service = ChromeService(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(service=service)
        time.sleep(5)
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        add_instructions_locator = driver.find_element(By.ID, "instructions")
        add_button_locator = driver.find_element(By.XPATH, "//button[@id='add_btn']")
        add_button_locator.click()
        assert add_instructions_locator.is_displayed()

    @pytest.mark.exceptions
    def test_element_reference_exception(self, driver):
        chrome_driver_path = 'C:\\Users\\admin\\Desktop\\drivers\\chromedriver.exe'
        service = ChromeService(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(service=service)
        time.sleep(5)
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        add_button_locator = driver.find_element(By.XPATH, "//button[@id='add_btn']")
        add_button_locator.click()
        WebDriverWait(driver, 3).until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))
        second_row = driver.find_element(By.XPATH, "//div[@id='row2']/input")
        assert second_row.is_displayed()