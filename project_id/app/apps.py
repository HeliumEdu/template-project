__copyright__ = "Copyright (c) 2024 Helium Edu"
__license__ = "MIT"

import os
import sys
from django.apps import AppConfig
from django.conf import settings
from urllib.parse import urlparse


class CommonConfig(AppConfig):
    name = "{%PROJECT_ID_LOWER%}.app"
    verbose_name = "App"
    default_auto_field = "django.db.models.BigAutoField"

    def ready(self):
        if settings.USE_NGROK and os.environ.get("NGROK_AUTHTOKEN"):
            # pyngrok will only be installed, and should only ever be initialized, in a dev environment
            from pyngrok import ngrok

            # Get the dev server port (defaults to 8000 for Django, can be overridden with the
            # last arg when calling `runserver`)
            addrport = urlparse(f"http://{sys.argv[-1]}")
            port = addrport.port if addrport.netloc and addrport.port else 8000

            # Open a ngrok tunnel to the dev server
            public_url = ngrok.connect(port).public_url
            print(f"ngrok tunnel \"{public_url}\" -> \"http://127.0.0.1:{port}\"")

            # Update any base URLs or webhooks to use the public ngrok URL
            settings.PROJECT_HOST = public_url
            CommonConfig.init_webhooks(public_url)

    @staticmethod
    def init_webhooks(callback_url):
        pass
