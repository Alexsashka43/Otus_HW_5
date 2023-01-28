from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from configuration import email, user_password, product_name
from conftest import base_url
from page_objects.UserPage import UserPage
from page_objects.elements.Buttons import Buttons
from selenium.webdriver.support import expected_conditions as EC

from page_objects.elements.InfoMessage import InfoMessage


class HomePage:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.url = self.driver.get(base_url + '/index.php?route=common/home')


    def add_to_wish_list(self):
        Buttons(self.driver).click_add_to_wish_list()
        InfoMessage(self.driver).info_success()

    def del_from_wish_list(self):
        Buttons(self.driver).click_wish_list()
        Buttons(self.driver).click_del()
        InfoMessage(self.driver).info_success()

    def add_to_cart(self):
        Buttons(self.driver).click_add_cart()
        InfoMessage(self.driver).info_success()

    def del_from_cart(self):
        Buttons(self.driver).click_cart()
        Buttons(self.driver).click_del_circle()
        InfoMessage(self.driver).info_success()

    def add_to_compare(self):
        Buttons(self.driver).click_add_compare()
        InfoMessage(self.driver).info_success()
