# import allure
from configuration import User
from page_objects.UserPage import UserPage
from page_objects.elements.InfoMessage import InfoMessage


# @allure.step('Registration form: ')
def test_warning(driver):
    InfoMessage(driver).info_danger()


# @allure.step(f'Registration form: Add user {User.LOGIN}')
def test_add_user(driver, base_url):
    UserPage(driver).registration(User.FIRST_NAME, User.LAST_NAME, User.EMAIL, User.PHONE, User.PASSWORD, base_url)
    UserPage(driver).login(User.EMAIL, User.PASSWORD, base_url)

# @allure.step('Registration form: Login user test@mail.ru')
def test_login(driver, base_url):
    UserPage(driver).login(User.LOGIN, User.PASSWORD, base_url)
