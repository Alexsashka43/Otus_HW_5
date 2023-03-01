import json

import allure
import pytest
import os
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service



@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="http:192.168.1.7:8081")
    parser.addoption("--drivers", default=os.path.expanduser("~/Downloads/drivers"))
    # parser.addoption("--log_level", action="store", default="DEBUG")
    parser.addoption("--executor", default="192.168.1.7")
    parser.addoption("--bversion")
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--logs", action="store_true", default=False)
    parser.addoption("--video", action="store_true", default=True)


@pytest.fixture
def driver(request):

    driver = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    # log_level = request.config.getoption("--log_level")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    video = request.config.getoption("--video")
    version = request.config.getoption("--bversion")
    drivers = request.config.getoption("--drivers")

    options = webdriver.ChromeOptions()
    options.add_experimental_option('w3c', True)
    executor_url = f"http://{executor}:4444/wd/hub"

    if executor == 'local':
        if driver == "chrome":
            service = Service(executable_path=os.path.join(drivers, "chromedriver.exe"))
            browser = webdriver.Chrome(service=service, options=options)
        elif driver == "yandex":
            browser = webdriver.Chrome(executable_path=os.path.join(drivers, "yandexdriver.exe"), options=options)
        elif driver == "firefox":
            browser = webdriver.Firefox(executable_path=os.path.join(drivers, "geckodriver.exe"), options=options)
        elif driver == "edge":
            browser = webdriver.Edge(executable_path=os.path.join(drivers, "msedgedriver.exe"), options=options)
        elif driver == "safari":
            browser = webdriver.Safari(executable_path=os.path.join(drivers, "safaridriver.exe"), options=options)
        else:
            raise Exception("Driver not supported")

    else:

        capabilities = {
            'browserName': driver,
            'browserVersion': version,
            'selenoid:options': {
                'enableVNC': vnc,
                'enableVideo': video,
                'enableLog': logs,
            },
            'name': 'test',
        }

        browser = webdriver.Remote(
            desired_capabilities=capabilities,
            command_executor=executor_url,
            options=options
        )


    allure.attach(
        name=browser.session_id,
        body=json.dumps(browser.capabilities),
        attachment_type=allure.attachment_type.JSON,
    )

    def finalizer():
        browser.quit()

        with open("allure-results/environment.xml", "w+") as file:
            file.write(f"""<environment>
                <parameter>
                    <key>Browser</key>
                    <value>{browser}</value>
                </parameter>
                <parameter>
                    <key>Browser.Version</key>
                    <value>{version}</value>
                </parameter>
                <parameter>
                    <key>Executor</key>
                    <value>{executor_url}</value>
                </parameter>
            </environment>
            """)

    browser.test_name = request.node.name
    browser.log_level = logging.DEBUG

    request.addfinalizer(finalizer)
    return browser