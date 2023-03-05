import logging
import os

from datetime import datetime
from selenium.webdriver.remote.errorhandler import WebDriverException


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        if WebDriverException:
            try:
                os.mkdir("screenshots")
            except:
                self.driver.get_screenshot_as_file(
                    f"screenshots/{datetime.now().strftime('%m-%d-%Y_%H-%M')}_{self.driver.test_name}.png")

        self.logger = logging.getLogger(type(self).__name__)
        os.makedirs('logs', exist_ok=True)
        file_handler = logging.FileHandler(f"logs/{self.driver.test_name}.log")
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(file_handler)
        self.logger.setLevel(level=self.driver.log_level)
