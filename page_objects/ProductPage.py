import allure

from page_objects.HomePage import HomePage
from page_objects.elements.Buttons import Buttons
from page_objects.elements.InfoMessage import InfoMessage


class ProductPage(HomePage):

    @allure.step
    def add_to_cart(self):
        self.logger.info('Add to cart')
        Buttons(self.driver).click_add_to_cart()
        InfoMessage(self.driver).info_success()
