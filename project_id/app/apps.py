from django.apps import AppConfig

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2018, Alex Laird'
__version__ = '0.1.0'


class CommonConfig(AppConfig):
    name = '{%PROJECT_ID%}.app'
    verbose_name = 'App'
