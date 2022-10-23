from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_search_elm_reg(browser, base_url):
    browser.get(base_url + '/index.php?route=account/register')
    button_continue = browser.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]')
    wait = WebDriverWait(browser, 10)
    wait.until(EC.title_is('Register Account'))
    assert browser.find_element(By.ID, 'account-register')
    assert browser.find_element(By.ID, 'column-right')
    assert len(browser.find_elements(By.CSS_SELECTOR, '[class="form-control"]')) == 6
    assert button_continue
    button_continue.click()
    assert browser.find_element(By.CSS_SELECTOR, '[class="alert alert-danger alert-dismissible"]')
