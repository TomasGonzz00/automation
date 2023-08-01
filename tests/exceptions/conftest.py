import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    print("Creating chrome driver")
    my_driver = webdriver.Chrome()
    yield my_driver
    print("Closing chrome driver")
    my_driver.quit()
