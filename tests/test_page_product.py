from selenium.webdriver.common.by import By


def test_search_elm_product(base_url, browser):
    browser.get(base_url + '/desktops/iphone')
    browser.implicitly_wait(5)
    assert browser.find_element(By.CSS_SELECTOR, '[class="list-unstyled"]')
    assert browser.find_element(By.ID, 'button-cart')
    assert browser.find_element(By.CSS_SELECTOR, '[class="rating"]')
    assert browser.find_element(By.CSS_SELECTOR, '[class="tab-content"]')
    assert browser.find_element(By.CSS_SELECTOR, '[class="row"]')
