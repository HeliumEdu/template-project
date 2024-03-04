"""
Base URL configuration.
"""

__copyright__ = "Copyright (c) 2024 Helium Edu"
__license__ = "MIT"

import sys

from django.conf import settings as config
from django.urls import include, re_path
from django.views import static

import {%PROJECT_ID_LOWER%}.app.urls

urlpatterns = [
    # Include app-specific URL files
    re_path(r"^", include({%PROJECT_ID_LOWER%}.app.urls)),
]

if config.DEBUG or "test" in sys.argv:
    # Ensure media files are shown properly when using a dev server
    urlpatterns += [
        re_path(r"^" + config.MEDIA_URL.lstrip("/") + "(?P<path>.*)$", static.serve, {
            "document_root": config.MEDIA_ROOT})
    ]
