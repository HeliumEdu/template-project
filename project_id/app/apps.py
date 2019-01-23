import os
import sys

from urllib.parse import urlparse

from django.apps import AppConfig
from django.conf import settings

__author__ = "Alex Laird"
__copyright__ = "Copyright 2018, Helium Edu"
__version__ = "1.1.1"


class CommonConfig(AppConfig):
    name = "{%PROJECT_ID_LOWER%}.app"
    verbose_name = "App"

    def ready(self):
        if os.environ.get('RUN_MAIN', None) and \
                settings.DEV_SERVER and settings.USE_NGROK:
            CommonConfig.init_ngrok()

    @staticmethod
    def init_ngrok():
        from pyngrok import ngrok

        addrport = urlparse('http://{}'.format(sys.argv[-1]))
        port = addrport.port if addrport.netloc and addrport.port else 8000
        public_url = ngrok.connect(port)
        print('ngrok tunneling from {} -> http://127.0.0.1:{}/'.format(public_url, port))

        settings.PROJECT_HOST = public_url.rstrip("/")

        CommonConfig.init_webhooks(public_url)

    @staticmethod
    def init_webhooks(callback_url):
        pass
