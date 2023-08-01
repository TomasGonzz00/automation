from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoggedInSuccessfullyPage:
    __actual_url = "https://practicetestautomation.com/logged-in-successfully/"
    __header = (By.TAG_NAME, "h1")
    __log_out_button = (By.LINK_TEXT, 'Log out')

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def current_url(self) -> str:
        return self._driver.current_url

    def header(self) -> str:
        return self._driver.find_element(self.__header).text

    def is_logout_button_displayed(self) -> bool:
        return self._driver.find_element(self.__log_out_button).is_displayed()
