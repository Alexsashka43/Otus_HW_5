import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from configuration import email, user_password
from page_objects.HomePage import HomePage
from page_objects.UserPage import UserPage
from page_objects.elements.Buttons import Buttons
from page_objects.elements.Currency import Currency


def test_search_elm_home(base_url, browser):
    browser.get(base_url + '/index.php?route=common/home')
    time.sleep(1)
    assert browser.find_element(By.CSS_SELECTOR, '[class="col-sm-4"]')
    assert browser.find_element(By.CSS_SELECTOR, '[name="search"]')
    assert browser.find_element(By.CSS_SELECTOR, '[alt="MacBookAir"]')
    assert len(browser.find_elements(By.CSS_SELECTOR, '[class="product-thumb transition"]')) == 4


def test_add_to_wish_list(browser, base_url):
    UserPage(browser).login(email, user_password, base_url)
    HomePage(browser, base_url).add_to_wish_list()


def test_del_from_with_list(browser, base_url):
    UserPage(browser).login(email, user_password, base_url)
    HomePage(browser, base_url).del_from_wish_list()


def test_add_to_cart(browser, base_url):
    UserPage(browser).login(email, user_password, base_url)
    HomePage(browser, base_url).add_to_cart()


def test_del_from_cart(browser, base_url):
    UserPage(browser).login(email, user_password, base_url)
    HomePage(browser, base_url).del_from_cart()


def test_add_to_compare(browser, base_url):
    HomePage(browser, base_url).add_to_compare()


@pytest.mark.parametrize("currency,sign", [("EUR", "€"), ("GBP", "£"), ("USD", "$")])
def test_check_currency(browser, currency, sign, base_url):
    Currency(browser).check_currency(currency, sign, base_url)
