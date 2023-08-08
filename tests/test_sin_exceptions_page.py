from PageObjects.exceptions_page import ExceptionPage
import pytest

class TestSinExceptionPage:

    def test_no_such_element_exception_wait(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open()
        exception_page.add_second_row()
        assert exception_page.is_row_2_input_displayed()


    def test_element_not_interactable_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open()
        exception_page.add_second_row()
        exception_page.send_keys_row_2()
        assert exception_page.confirmation_row_2()

    @pytest.mark.sin_exception_page
    def test_invalid_element_state_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open()
        exception_page.clear_input()
        exception_page.send_keys_row_1()
        assert exception_page.text_changed()
