import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.keys import Keys


class TestNegativePathUsername:
    @pytest.mark.loginN
    def test_negative_username(self, driver):

        driver.get("https://practicetestautomation.com/practice-test-login/")

        user = driver.find_element(By.NAME, 'username')
        user.send_keys('incognito')

        password = driver.find_element(By.ID, 'password')
        password.send_keys('Password123')
        time.sleep(5)

        submit = driver.find_element(By.ID, "submit")
        submit.click()

        error = driver.find_element(By.ID, 'error')
        actual_text = error.text
        assert actual_text == 'Your username is invalid!'

        time.sleep(5)
        driver.close()

    class TestNegativePathPassword:
        @pytest.mark.loginN
        def test_negative_password(self):
            chrome_driver_path = 'C:\\Users\\admin\\Desktop\\drivers\\chromedriver.exe'  # En Windows | tu ruta aqui
            service = ChromeService(executable_path=chrome_driver_path)
            driver = webdriver.Chrome(service=service)
            time.sleep(5)
            driver.get("https://practicetestautomation.com/practice-test-login/")

            user = driver.find_element(By.NAME, 'username')
            user.send_keys('student')

            password = driver.find_element(By.ID, 'password')
            password.send_keys('Password1234')

            time.sleep(5)

            submit = driver.find_element(By.ID, "submit")
            submit.click()

            error = driver.find_element(By.ID, 'error')
            actual_text = error.text
            assert actual_text == "Your password is invalid!"

            time.sleep(5)