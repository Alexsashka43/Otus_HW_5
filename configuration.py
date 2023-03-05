from random import randint


class Admin:
    LOGIN: str = 'user'
    PASSWORD: str = 'bitnami'


class User:
    FIRST_NAME: str = 'FIRST_NAME'
    LAST_NAME: str = 'LAST_NAME'
    EMAIL: str = 'test@mail.com'
    RANDOM_EMAIL = f'test{randint(0, 99999)}test@mail.com'
    PHONE: str = '+91112345678'
    LOGIN: str = 'test'
    PASSWORD: str = 'test'


# user_name = 'test'
# user_password = 'test'
# last_name = 'test'
# email = 'test@mail.ru'
# telephone = 'test'
# product_name = 'macbook'
#
# admin_name = 'user'
# admin_password = 'bitnami'
