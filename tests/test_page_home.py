import time
import pytest
from selenium.webdriver.common.by import By


def test_search_elm_home(base_url, browser):
    browser.get(base_url + '/index.php?route=common/home')
    time.sleep(1)
    assert browser.find_element(By.CSS_SELECTOR, '[class="col-sm-4"]')
    assert browser.find_element(By.CSS_SELECTOR, '[name="search"]')
    assert browser.find_element(By.CSS_SELECTOR, '[alt="MacBookAir"]')
    assert len(browser.find_elements(By.CSS_SELECTOR, '[class="product-thumb transition"]')) == 4


@pytest.mark.parametrize("param",
                         ['Information', 'About Us', 'Delivery Information', 'Privacy Policy',
                          'Terms & Conditions'])
def test_text(base_url, browser, param):
    browser.get(base_url + '/index.php?route=common/home')
    assert browser.find_element(By.PARTIAL_LINK_TEXT, f'{param}')
