from selenium.webdriver.common.by import By

from page_objects.elements.Buttons import Buttons


class AdminPage:

    def __init__(self, driver):
        self.driver = driver

    def login(self, admin_name, admin_password, base_url):
        self.driver.get(base_url + '/admin/index.php?route=common/login')
        self.driver.find_element(By.CSS_SELECTOR, '[name="username"]').send_keys(admin_name)
        self.driver.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys(admin_password)
        self.driver.find_element(By.CSS_SELECTOR, '[class="fa fa-key"]').click()

    def navigation_products(self):
        self.driver.find_element(By.CSS_SELECTOR, '[id="menu-catalog"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[id="menu-extension"]').click()
        self.driver.find_element(By.LINK_TEXT, 'Products').click()

    def add_product(self):
        AdminPage(self.driver).navigation_products()
        Buttons(self.driver).click_plus()
        self.driver.find_element(By.CSS_SELECTOR, '[id="input-name1"]').send_keys('test')
        self.driver.find_element(By.CSS_SELECTOR, '[id="input-meta-title1"]').send_keys('test')
        self.driver.find_element(By.LINK_TEXT, 'Data').click()
        self.driver.find_element(By.CSS_SELECTOR, '[name="model"]').send_keys('test')
        Buttons(self.driver).click_save()

    def del_product(self):
        AdminPage(self.driver).navigation_products()
        self.driver.find_element(By.CSS_SELECTOR, '[id="input-model"]').send_keys('test')
        self.driver.find_element(By.CSS_SELECTOR, '[id="button-filter"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[type="checkbox"]').click()
        Buttons(self.driver).click_trash()
        # time.sleep(1)
        self.driver.switch_to.alert.accept()
