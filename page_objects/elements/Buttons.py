from selenium.webdriver.common.by import By


class Buttons:

    def __init__(self, driver):
        self.driver = driver

    def click_plus(self):
        self.driver.find_element(By.CSS_SELECTOR, '[class="fa fa-plus"]').click()

    def click_save(self):
        self.driver.find_element(By.CSS_SELECTOR, '[class ="fa fa-save"]').click()

    def click_trash(self):
        self.driver.find_element(By.CSS_SELECTOR, '[class="fa fa-trash-o"]').click()

    def click_continue(self):
        self.driver.find_element(By.CSS_SELECTOR, '[value="Continue"]').click()

    def click_agree(self):
        self.driver.find_element(By.CSS_SELECTOR, "[name='agree']").click()

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, '[value="Login"]').click()

    def click_add_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, '[class="button-group"]').find_element(
                By.CSS_SELECTOR, '[class="fa fa-shopping-cart"]').click()

    def click_add_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, '[id="button-cart"]').click()

    def click_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, '[title="Shopping Cart"]').click()

    def click_add_to_wish_list(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-original-title="Add to Wish List"]').click()

    def click_wish_list(self):
        self.driver.find_element(By.CSS_SELECTOR, '[id="wishlist-total"]').click()

    def click_add_compare(self):
        self.driver.find_element(By.CSS_SELECTOR, '[class="fa fa-exchange"]').click()

    def click_del(self):
        self.driver.find_element(By.CSS_SELECTOR, '[class="fa fa-times"]').click()

    def click_del_circle(self):
        self.driver.find_element(By.CSS_SELECTOR, '[class="fa fa-times-circle"]').click()
