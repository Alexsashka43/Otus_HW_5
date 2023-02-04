from configuration import admin_name, admin_password
from page_objects.AdminPage import AdminPage


def test_login(browser, base_url):
    AdminPage(browser).login(admin_name, admin_password, base_url)


def test_add_goods(browser, base_url):
    AdminPage(browser).login(admin_name, admin_password, base_url)
    AdminPage(browser).add_product()


def test_del_goods(browser, base_url):
    AdminPage(browser).login(admin_name, admin_password, base_url)
    AdminPage(browser).del_product()
