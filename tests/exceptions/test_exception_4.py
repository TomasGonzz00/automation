import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


class TestExceptions:
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
