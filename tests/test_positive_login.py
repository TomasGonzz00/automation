import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import pytest


class TestPositivePathUsername:
    @pytest.mark.loginP
    def test_positive_username(self):
        chrome_driver_path = 'C:\\Users\\admin\\Desktop\\drivers\\chromedriver.exe'  # En Windows | tu ruta aqui
        service = ChromeService(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(service=service)
        time.sleep(5)
        # Acceder a la página web
        driver.get("https://practicetestautomation.com/practice-test-login/")

        user = driver.find_element(By.NAME, "username")
        user.send_keys('student')

        password = driver.find_element(By.ID, 'password')
        password.send_keys('Password123')

        # btnSubmit = driver.find_element(By.ID,'submit')
        btnSubmit = driver.find_element(By.XPATH, "//button[@class='btn']")
        btnSubmit.click()

        # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        actual_url = driver.current_url
        assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"
        # Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        text_locator = driver.find_element(By.TAG_NAME, "h1")
        actual_text = text_locator.text
        assert actual_text == "Logged In Successfully"
        # Verify button Log out is displayed on the new page
        log_out_button_locator = driver.find_element(By.LINK_TEXT, 'Log out')
        assert log_out_button_locator.is_displayed()

        time.sleep(5)
