from django.apps import AppConfig

__author__ = "Alex Laird"
__copyright__ = "Copyright 2018, Helium Edu"
__version__ = "1.0.2"


class CommonConfig(AppConfig):
    name = "{%PROJECT_ID_LOWER%}.app"
    verbose_name = "App"
