import allure
from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage
from page_objects.elements.Buttons import Buttons


class UserPage(BasePage):

    @allure.step
    def registration(self, user_name, last_name, email, phone, user_password, base_url):
        self.logger.info("Registration: {}".format(email))
        self.driver.get(base_url + '/index.php?route=account/register')
        self.driver.find_element(By.CSS_SELECTOR, '[id="input-firstname"]').send_keys(user_name)
        self.driver.find_element(By.CSS_SELECTOR, '[id="input-lastname"]').send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, '[id="input-email"]').send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, '[id="input-telephone"]').send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, '[id="input-password"]').send_keys(user_password)
        self.driver.find_element(By.CSS_SELECTOR, '[id="input-confirm"]').send_keys(user_password)
        Buttons(self.driver).click_agree()
        Buttons(self.driver).click_continue()
        assert self.driver.find_element(By.LINK_TEXT, 'Success')

    @allure.step
    def login(self, email, user_password, base_url):
        self.logger.info("Login: {}".format(email))
        self.driver.get(base_url + '/index.php?route=account/login')
        self.driver.find_element(By.CSS_SELECTOR, '[id="input-email"]').send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, '[id="input-password"]').send_keys(user_password)
        Buttons(self.driver).click_login()
