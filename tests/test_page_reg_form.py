import allure
from selenium.webdriver.common.by import By

from configuration import User
from page_objects.UserPage import UserPage
from page_objects.elements.InfoMessage import InfoMessage


@allure.step(f'Registration form: Add user {User.RANDOM_EMAIL}')
def test_add_user(driver, base_url):
    UserPage(driver).registration(User.FIRST_NAME, User.LAST_NAME, User.RANDOM_EMAIL, User.PHONE, User.PASSWORD, base_url)


@allure.step(f'Registration success: login {User.EMAIL}, password {User.PASSWORD}')
def test_positive_login(driver, base_url):
    try:
        UserPage(driver).login(User.EMAIL, User.PASSWORD, base_url)
        InfoMessage(driver).info_success()
    except:
        UserPage(driver).registration(User.FIRST_NAME, User.LAST_NAME, User.EMAIL, User.PHONE, User.PASSWORD,
                                      base_url)



@allure.step(f'Registration fail: login {User.EMAIL}, password {User.PASSWORD}')
def test_negative_warning(driver, base_url):
    UserPage(driver).login(f'test{User.EMAIL}', f'test{User.PASSWORD}', base_url)
    InfoMessage(driver).info_danger()
