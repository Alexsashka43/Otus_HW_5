import allure
from selenium.webdriver.common.by import By


import pytest

from configuration import User
from page_objects.ProductPage import ProductPage
from page_objects.UserPage import UserPage
from page_objects.elements.Currency import Currency


@allure.step('User page: Add goods to wishlist')
def test_add_to_wish_list(driver, base_url):
    UserPage(driver).login(User.LOGIN, User.PASSWORD, base_url)
    ProductPage(driver, base_url).add_to_wish_list()


@allure.step('User page: Delete goods from wishlist')
def test_del_from_with_list(driver, base_url):
    UserPage(driver).login(User.LOGIN, User.PASSWORD, base_url)
    ProductPage(driver, base_url).del_from_wish_list()


@allure.step('User page: Add goods to cart')
def test_add_to_cart(driver, base_url):
    UserPage(driver).login(User.LOGIN, User.PASSWORD, base_url)
    ProductPage(driver, base_url).add_to_cart()


@allure.step('User page: Delete goods from cart')
def test_del_from_cart(driver, base_url):
    UserPage(driver).login(User.LOGIN, User.PASSWORD, base_url)
    ProductPage(driver, base_url).del_from_cart()


@allure.step('User page: Add goods to compare')
def test_add_to_compare(driver, base_url):
    ProductPage(driver, base_url).add_to_compare()


@allure.step('User page: Add goods to cart')
def test_search_elm_product(base_url, driver):
    driver.get(base_url + '/desktops/iphone')
    driver.implicitly_wait(5)
    assert driver.find_element(By.CSS_SELECTOR, '[class="list-unstyled"]')
    assert driver.find_element(By.ID, 'button-cart')
    assert driver.find_element(By.CSS_SELECTOR, '[class="rating"]')
    assert driver.find_element(By.CSS_SELECTOR, '[class="tab-content"]')
    assert driver.find_element(By.CSS_SELECTOR, '[class="row"]')


@allure.step('User page: Check currency(login)')
@pytest.mark.parametrize("currency,sign", [("EUR", "€"), ("GBP", "£"), ("USD", "$")])
def test_check_currency(driver, currency, sign, base_url):
    UserPage(driver).login(User.LOGIN, User.PASSWORD, base_url)
    Currency(driver).check_currency(currency, sign, base_url)
