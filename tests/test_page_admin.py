import allure
from configuration import Admin
from page_objects.AdminPage import AdminPage
from page_objects.elements.Buttons import Buttons
from page_objects.elements.InfoMessage import InfoMessage


@allure.step('Admin page: Login')
def test_login(driver, base_url):
    AdminPage(driver).login(Admin.LOGIN, Admin.PASSWORD, base_url)


@allure.step('Admin page: Add goods')
def test_add_goods(driver, base_url):
    AdminPage(driver).login(Admin.LOGIN, Admin.PASSWORD, base_url)
    AdminPage(driver).navigation_products()
    Buttons(driver).click_plus()
    AdminPage(driver).add_product()
    Buttons(driver).click_save()


@allure.step('Admin page: Delete goods')
def test_del_goods(driver, base_url):
    AdminPage(driver).login(Admin.LOGIN, Admin.PASSWORD, base_url)
    AdminPage(driver).navigation_products()
    AdminPage(driver).del_product()
    Buttons(driver).click_trash()
    InfoMessage(driver).switch_alert()
