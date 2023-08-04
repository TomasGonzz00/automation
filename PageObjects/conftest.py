import pytest
from selenium import webdriver


@pytest.fixture(params=("chrome", "edge"))
def driver(request):
    browser = request.param
    if browser == "chrome":
        print("Creating chrome driver")
        my_driver = webdriver.Chrome()
        yield my_driver
        print("Closing chrome driver")
        my_driver.quit()
    else:
        print("Creating edge driver")
        my_driver = webdriver.Edge()
        yield my_driver
        print("Closing edge driver")
        my_driver.quit()
