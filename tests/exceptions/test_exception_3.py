import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


class TestExceptions:
    @pytest.mark.exceptions
    def test_invalid_element_state_exception(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        input_locator = driver.find_element(By.XPATH, "//input[contains(@value,'Pizza')]")
        input_locator.clear()
        input_locator.send_keys("Tacos")

        assert input_locator.text == "Tacos"
