import allure
import time

import pytest
from selenium.webdriver.common.by import By
from configuration import User
from page_objects.BasePage import BasePage
from page_objects.HomePage import HomePage
from page_objects.UserPage import UserPage
from page_objects.elements.Currency import Currency


@allure.step('Home page: Search elements')
def test_search_elm_home(base_url, driver):
    driver.get(base_url + '/index.php?route=common/home')
    time.sleep(1)
    assert driver.find_element(By.CSS_SELECTOR, '[class="col-sm-4"]')
    assert driver.find_element(By.CSS_SELECTOR, '[name="search"]')
    assert driver.find_element(By.CSS_SELECTOR, '[alt="MacBookAir"]')
    assert len(driver.find_elements(By.CSS_SELECTOR, '[class="product-thumb transition"]')) == 4


@allure.step('Home page: Add goods to wishlist')
def test_add_to_wish_list(driver, base_url):
    UserPage(driver).login(User.EMAIL, User.PASSWORD, base_url)
    HomePage(driver, base_url).add_to_wish_list()


@allure.step('Home page: Delete goods from wishlist')
def test_del_from_with_list(driver, base_url):
    UserPage(driver).login(User.LOGIN, User.PASSWORD, base_url)
    HomePage(driver, base_url).del_from_wish_list()


@allure.step('Home page: Add goods to cart')
def test_add_to_cart(driver, base_url):
    UserPage(driver).login(User.LOGIN, User.PASSWORD, base_url)
    HomePage(driver, base_url).add_to_cart()


@allure.step('Home page: Delete goods from cart')
def test_del_from_cart(driver, base_url):
    UserPage(driver).login(User.LOGIN, User.PASSWORD, base_url)
    HomePage(driver, base_url).del_from_cart()


@allure.step('Home page: Delete goods to compare')
def test_add_to_compare(driver, base_url):
    HomePage(driver, base_url).add_to_compare()


@allure.step('Home page: Check_currency(without login)')
@pytest.mark.parametrize("currency,sign", [("EUR", "€"), ("GBP", "£"), ("USD", "$")])
def test_check_currency(driver, currency, sign, base_url):
    Currency(driver).check_currency(currency, sign, base_url)
