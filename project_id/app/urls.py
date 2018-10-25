from django.conf.urls import url

from {%PROJECT_ID%}.app.admin import admin_site

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2018, Alex Laird'
__version__ = '0.1.0'

urlpatterns = [
    # Top-level URLs
    url(r'^admin/', admin_site.urls),
]
