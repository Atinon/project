from os import getenv


def is_production():
    return getenv('APP_ENVIRONMENT') == 'Production'


def is_development():
    return getenv('APP_ENVIRONMENT') == 'Development'

