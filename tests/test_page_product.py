import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest

from configuration import email, user_password
from conftest import base_url
from page_objects.HomePage import HomePage
from page_objects.ProductPage import ProductPage
from page_objects.UserPage import UserPage
from page_objects.elements.Currency import Currency


def test_add_to_wish_list(browser, base_url):
    UserPage(browser).login(email, user_password, base_url)
    ProductPage(browser, base_url).add_to_wish_list()


def test_del_from_with_list(browser, base_url):
    UserPage(browser).login(email, user_password, base_url)
    ProductPage(browser, base_url).del_from_wish_list()


def test_add_to_cart(browser, base_url):
    UserPage(browser).login(email, user_password, base_url)
    ProductPage(browser, base_url).add_to_cart()


def test_del_from_cart(browser, base_url):
    UserPage(browser).login(email, user_password, base_url)
    ProductPage(browser, base_url).del_from_cart()


def test_add_to_compare(browser, base_url):
    ProductPage(browser, base_url).add_to_compare()


def test_search_elm_product(base_url, browser):
    browser.get(base_url + '/desktops/iphone')
    browser.implicitly_wait(5)
    assert browser.find_element(By.CSS_SELECTOR, '[class="list-unstyled"]')
    assert browser.find_element(By.ID, 'button-cart')
    assert browser.find_element(By.CSS_SELECTOR, '[class="rating"]')
    assert browser.find_element(By.CSS_SELECTOR, '[class="tab-content"]')
    assert browser.find_element(By.CSS_SELECTOR, '[class="row"]')


@pytest.mark.parametrize("currency,sign", [("EUR", "€"), ("GBP", "£"), ("USD", "$")])
def test_check_currency(browser, currency, sign, base_url):
    Currency(browser).check_currency(currency, sign, base_url)