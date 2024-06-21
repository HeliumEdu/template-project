__copyright__ = "Copyright (c) 2024 Helium Edu"
__license__ = "MIT"

from django.urls import re_path

from {%PROJECT_ID_LOWER%}.app.admin import admin_site
from {%PROJECT_ID_LOWER%}.app.views.apis.infoviews import InfoResourceView
from {%PROJECT_ID_LOWER%}.app.views.apis.statusviews import StatusResourceView

urlpatterns = [
    # URLs for auto-generated resources
    re_path("admin/", admin_site.urls, name="admin"),

    ##############################
    # Unauthenticated URLs
    ##############################
    re_path("status/", StatusResourceView.as_view({"get": "status"}), name="resource_status"),
    re_path("info/", InfoResourceView.as_view({"get": "info"}), name="resource_info"),
]
