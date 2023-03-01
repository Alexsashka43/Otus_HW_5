import allure
from selenium.webdriver.common.by import By


@allure.step('Catalog: Search elements')
def test_search_elm_product(base_url, driver):
    driver.get(base_url + '/desktops')
    assert driver.find_element(By.CSS_SELECTOR, '[class="col-sm-3 hidden-xs"]')
    assert driver.find_element(By.ID, 'input-sort')
    assert driver.find_element(By.CSS_SELECTOR, '[class="btn btn-inverse btn-block btn-lg dropdown-toggle"]')
    assert len(driver.find_elements(By.CSS_SELECTOR,
                                     '[class="product-layout product-grid col-lg-4 col-md-4 col-sm-6 col-xs-12"]')) == 12
    assert driver.find_element(By.CSS_SELECTOR, '[class="col-sm-6 text-right"]')

