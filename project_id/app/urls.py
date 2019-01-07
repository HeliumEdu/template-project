from django.conf.urls import url

from {%PROJECT_ID_LOWER%}.app.admin import admin_site

__author__ = "Alex Laird"
__copyright__ = "Copyright 2018, Helium Edu"
__version__ = "1.0.2"

urlpatterns = [
    # Top-level URLs
    url(r"^admin/", admin_site.urls),
]
