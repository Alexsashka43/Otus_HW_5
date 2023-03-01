import logging

import allure

from page_objects.BasePage import BasePage
from page_objects.elements.Buttons import Buttons
from page_objects.elements.InfoMessage import InfoMessage


class HomePage(BasePage):
    def __init__(self, driver, base_url):
        super().__init__(driver)
        driver.get(base_url + '/index.php?route=common/home')

    @allure.step
    def add_to_wish_list(self):
        self.logger.info('Add to wishlist')
        Buttons(self.driver).click_add_to_wish_list()
        InfoMessage(self.driver).info_success()

    @allure.step
    def del_from_wish_list(self):
        self.logger.info('Delete from wishlist')
        Buttons(self.driver).click_wish_list()
        Buttons(self.driver).click_del()
        InfoMessage(self.driver).info_success()

    @allure.step
    def add_to_cart(self):
        self.logger.info('Add to cart')
        Buttons(self.driver).click_add_cart()
        InfoMessage(self.driver).info_success()

    @allure.step
    def del_from_cart(self):
        self.logger.info('Delete from cart')
        Buttons(self.driver).click_cart()
        Buttons(self.driver).click_del_circle()
        InfoMessage(self.driver).info_success()

    @allure.step
    def add_to_compare(self):
        self.logger.info('Add to compare')
        Buttons(self.driver).click_add_compare()
        InfoMessage(self.driver).info_success()
