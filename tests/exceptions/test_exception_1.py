import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



class TestExceptions:
    @pytest.mark.exceptions
    def test_no_such_element_exception(self):
        chrome_driver_path = 'C:\\Users\\admin\\Desktop\\drivers\\chromedriver.exe'
        service = ChromeService(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(service=service)
        time.sleep(5)
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")


        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()
        row_2_input_element = driver.find_element(By.ID, "row2")
        assert row_2_input_element.is_displayed(), "Row 2 input should be displayed, but it's not"

