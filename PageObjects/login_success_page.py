from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from PageObjects.base_page import BasePage


class LoggedInSuccessfullyPage(BasePage):
    __actual_url = "https://practicetestautomation.com/logged-in-successfully/"
    __header = (By.TAG_NAME, "h1")
    __log_out_button = (By.LINK_TEXT, 'Log out')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self.__actual_url

    @property
    def header(self) -> str:
        return super()._get_text(self.__header)

    def is_logout_button_displayed(self) -> bool:
        return super()._is_displayed(self.__log_out_button)

