from django.urls import re_path
from rest_framework.documentation import include_docs_urls

from {%PROJECT_ID_LOWER%}.app.admin import admin_site
from {%PROJECT_ID_LOWER%}.app.views.apis.infoviews import InfoResourceView
from {%PROJECT_ID_LOWER%}.app.views.apis.statusviews import StatusResourceView

__author__ = "Alex Laird"
__copyright__ = "Copyright 2019, Helium Edu"
__version__ = "1.3.0"

urlpatterns = [
    # URLs for auto-generated resources
    re_path("admin/", admin_site.urls, name="admin"),
    re_path("docs/", include_docs_urls(title="{%PROJECT_NAME%} API Documentation"), name="docs"),

    ##############################
    # Unauthenticated URLs
    ##############################
    re_path("status/", StatusResourceView.as_view({"get": "status"}), name="resource_status"),
    re_path("info/", InfoResourceView.as_view({"get": "info"}), name="resource_info"),
]
