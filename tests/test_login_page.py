import time

from PageObjects.login_page import LoginPage
from PageObjects.login_success_page import LoggedInSuccessfullyPage
import pytest


class TestPositiveScenarios:
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("student", "Password123")
        logged_in_page = LoggedInSuccessfullyPage(driver)
        time.sleep(3)
        assert logged_in_page.expected_url == logged_in_page.current_url
        assert logged_in_page.header == "Logged In Successfully"
        assert logged_in_page.is_logout_button_displayed()
