"""
Settings common to all deployment methods.
"""

__copyright__ = "Copyright (c) 2024 Helium Edu"
__license__ = "MIT"
__version__ = "1.3.3"

import os
import socket

from conf.settings import PROJECT_ID

# Define the base working directory of the application
BASE_DIR = os.path.normpath(os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", ".."))

# ############################
# Project configuration
# ############################

# Project information

PROJECT_NAME = os.environ.get("{%PROJECT_ID_UPPER%}_NAME")

PROJECT_HOST = os.environ.get("{%PROJECT_ID_UPPER%}_HOST")

# Version information

PROJECT_VERSION = __version__

# AWS S3

AWS_S3_ACCESS_KEY_ID = os.environ.get("{%PROJECT_ID_UPPER%}_AWS_S3_ACCESS_KEY_ID")
AWS_S3_SECRET_ACCESS_KEY = os.environ.get("{%PROJECT_ID_UPPER%}_AWS_S3_SECRET_ACCESS_KEY")

#############################
# Default lists for host-specific configurations
#############################

INSTALLED_APPS = (
    # Django modules
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    # Health modules
    "health_check",
    "health_check.cache",
    "health_check.db",
    # Third-party modules
    "pipeline",
    "rest_framework",
    # Project modules
    "{%PROJECT_ID_LOWER%}.app",
)

MIDDLEWARE = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "APP_DIRS": True,
    "OPTIONS": {
        "context_processors": [
            "django.contrib.auth.context_processors.auth",
            "django.template.context_processors.media",
            "django.template.context_processors.static",
            "django.template.context_processors.tz",
            "django.contrib.messages.context_processors.messages",
            "django.template.context_processors.request",
        ],
    },
}]

#############################
# Django configuration
#############################

# Application definition

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
ROOT_URLCONF = "conf.urls"
WSGI_APPLICATION = "conf.wsgi.application"

HOSTNAME = socket.gethostname()

# API configuration

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

# Internationalization

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_THOUSAND_SEPARATOR = True
USE_TZ = True

# DateTime sanity

NORMALIZED_DATE_FORMAT = "%a, %b %d"
NORMALIZED_DATE_TIME_FORMAT = f"{NORMALIZED_DATE_FORMAT} at %I:%M %p"

# Email settings

ADMIN_EMAIL_ADDRESS = os.environ.get("{%PROJECT_ID_UPPER%}_ADMIN_EMAIL")
SERVER_EMAIL = ADMIN_EMAIL_ADDRESS
EMAIL_USE_TLS = os.environ.get("{%PROJECT_ID_UPPER%}_EMAIL_USE_TLS", "True") == "True"
EMAIL_PORT = os.environ.get("{%PROJECT_ID_UPPER%}_EMAIL_PORT")
EMAIL_ADDRESS = os.environ.get("{%PROJECT_ID_UPPER%}_CONTACT_EMAIL")
DEFAULT_FROM_EMAIL = f"{PROJECT_NAME} <{EMAIL_ADDRESS}>"
EMAIL_HOST = os.environ.get("{%PROJECT_ID_UPPER%}_EMAIL_HOST")

EMAIL_HOST_USER = os.environ.get("{%PROJECT_ID_UPPER%}_EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("{%PROJECT_ID_UPPER%}_EMAIL_HOST_PASSWORD")

# Security

SECRET_KEY = os.environ.get("{%PROJECT_ID_UPPER%}_SECRET_KEY")
CSRF_COOKIE_SECURE = os.environ.get("{%PROJECT_ID_UPPER%}_CSRF_COOKIE_SECURE", "True") == "True"
SESSION_COOKIE_SECURE = os.environ.get("{%PROJECT_ID_UPPER%}_SESSION_COOKIE_SECURE", "True") == "True"
ALLOWED_HOSTS = os.environ.get("{%PROJECT_ID_UPPER%}_ALLOWED_HOSTS", "").split(" ")
CSRF_TRUSTED_ORIGINS = [PROJECT_HOST]

# Logging

DEBUG = os.environ.get("{%PROJECT_ID_UPPER%}_DEBUG", "False") == "True"

# Static files (CSS, JavaScript, Images)

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_STORAGE = "pipeline.storage.PipelineStorage"

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "pipeline.finders.PipelineFinder",
)

# Media files

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Pipelines

PIPELINE = {
    "DISABLE_WRAPPER": True,
    "STYLESHEETS": {
        "error": {
            "source_filenames": (
                "css/error.css",
            ),
            "output_filename": f"css/{PROJECT_ID}_error_{PROJECT_VERSION}.min.css",
        },
    },
}

# Server

USE_NGROK = os.environ.get("USE_NGROK", "False") == "True" and os.environ.get("RUN_MAIN", None) != "true"
