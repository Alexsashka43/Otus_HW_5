from configuration import user_name, last_name, email, telephone, user_password
from page_objects.UserPage import UserPage
from page_objects.elements.InfoMessage import InfoMessage


def test_warning(browser, base_url):
    InfoMessage(browser).info_danger()


def test_add_user(browser, base_url):
    UserPage(browser).registration(user_name, last_name, email, telephone, user_password, base_url)


def test_login(browser, base_url):
    UserPage(browser).login(email, user_password, base_url)
