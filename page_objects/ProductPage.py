import allure

from page_objects.HomePage import HomePage
from page_objects.elements.Buttons import Buttons
from page_objects.elements.InfoMessage import InfoMessage


class ProductPage(HomePage):
    # def __init__(self, driver, base_url):
    #     super().__init__(driver)
    #     self.url = self.driver.get(base_url + f'/{product_name}')

    @allure.step
    def add_to_cart(self):
        self.logger.info('Add to cart')
        Buttons(self.driver).click_add_to_cart()
        InfoMessage(self.driver).info_success()
