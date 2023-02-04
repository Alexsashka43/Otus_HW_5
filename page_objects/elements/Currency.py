from selenium.webdriver.common.by import By


class Currency:

    def __init__(self, driver):
        self.driver = driver

    def check_currency(self, currency, sign, base_url):
        self.driver.get(base_url)
        menu = self.driver.find_element(By.CSS_SELECTOR, "[class='btn btn-link dropdown-toggle']").click()
        choose_currency = self.driver.find_element(By.CSS_SELECTOR, f"[name='{currency}']").click()
        assert self.driver.find_element(By.CSS_SELECTOR, f"[class='price']").text.__contains__(sign)
