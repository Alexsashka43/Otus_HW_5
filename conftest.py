import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="http:192.168.1.26:8081")
    parser.addoption("--drivers", default=os.path.expanduser("~/Downloads/drivers"))


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    drivers = request.config.getoption("--drivers")

    if browser == "chrome":
        service = Service(executable_path=os.path.join(drivers, "chromedriver"))
        driver = webdriver.Chrome(service=service)
    elif browser == "yandex":
        driver = webdriver.Chrome(executable_path=os.path.join(drivers, "yandexdriver"))
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=os.path.join(drivers, "geckodriver"))
    elif browser == "edge":
        driver = webdriver.Edge(executable_path=os.path.join(drivers, "msedgedriver"))
    elif browser == "safari":
        driver = webdriver.Safari(executable_path=os.path.join(drivers, "safaridriver"))
    else:
        raise Exception("Driver not supported")

    request.addfinalizer(driver.quit)

    return driver


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")