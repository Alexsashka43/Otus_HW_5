from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InfoMessage:

    def __init__(self, driver):
        self.driver = driver

    def info_danger(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="alert alert-danger alert-dismissible"]')))

    def info_success(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[class ="alert alert-success alert-dismissible"]')))


    def switch_alert(self):
        self.driver.switch_to.alert.accept()
