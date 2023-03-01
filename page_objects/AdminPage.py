import allure
from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage
from page_objects.elements.Buttons import Buttons


class AdminPage(BasePage):

    @allure.step
    def login(self, admin_name, admin_password, base_url):
        self.logger.info('Login Admin')
        self.driver.get(base_url + '/admin/index.php?route=common/login')
        self.driver.find_element(By.CSS_SELECTOR, '[name="username"]').send_keys(admin_name)
        self.driver.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys(admin_password)
        self.driver.find_element(By.CSS_SELECTOR, '[class="fa fa-key"]').click()

    @allure.step
    def navigation_products(self):
        self.logger.info('Catalog: Products')
        self.driver.find_element(By.CSS_SELECTOR, '[id="menu-catalog"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[id="menu-extension"]').click()
        self.driver.find_element(By.LINK_TEXT, 'Products').click()

    @allure.step
    def add_product(self):
        self.logger.info('Admin: Add goods')
        self.driver.find_element(By.CSS_SELECTOR, '[id="input-name1"]').send_keys('test')
        self.driver.find_element(By.CSS_SELECTOR, '[id="input-meta-title1"]').send_keys('test')
        self.driver.find_element(By.LINK_TEXT, 'Data').click()
        self.driver.find_element(By.CSS_SELECTOR, '[name="model"]').send_keys('test')

    @allure.step
    def del_product(self):
        self.logger.info('Admin: Delete goods')
        self.driver.find_element(By.CSS_SELECTOR, '[id="input-model"]').send_keys('test')
        self.driver.find_element(By.CSS_SELECTOR, '[id="button-filter"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[type="checkbox"]').click()


