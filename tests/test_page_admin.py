import time
from selenium.webdriver.common.by import By


def test_search_elm_admin(base_url, browser):
    browser.get(base_url + '/admin')
    time.sleep(1)
    assert browser.find_element(By.CSS_SELECTOR, '[class="panel-title"]').text == 'Please enter your login details.'
    assert browser.find_element(By.CSS_SELECTOR, '[name="username"]')
    assert browser.find_element(By.CSS_SELECTOR, '[name="password"]')
    assert browser.find_element(By.CSS_SELECTOR, '[class="help-block"]')
    assert browser.find_element(By.CSS_SELECTOR, '[class="fa fa-key"]')
