"""
Settings specific to prod-like deployable code, reading values from system environment variables.
"""

__copyright__ = "Copyright (c) 2024 Helium Edu"
__license__ = "MIT"

import os

from conf.configs import common
from conf.settings import PROJECT_ID

# Define the base working directory of the application
BASE_DIR = os.path.normpath(os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", ".."))

# Application definition

INSTALLED_APPS = common.INSTALLED_APPS

MIDDLEWARE = common.MIDDLEWARE + (
    "rollbar.contrib.django.middleware.RollbarNotifierMiddleware",
)

TEMPLATES = common.TEMPLATES

if common.DEBUG:
    TEMPLATES[0]["OPTIONS"]["context_processors"] += (
        "django.template.context_processors.debug",
    )

#############################
# Django configuration
#############################

# Security

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

# Logging

ROLLBAR = {
    "access_token": os.environ.get("PLATFORM_ROLLBAR_POST_SERVER_ITEM_ACCESS_TOKEN"),
    "environment": os.environ.get("ENVIRONMENT"),
    "branch": "main",
    "root": BASE_DIR,
}

if not common.DEBUG:
    ADMINS = (
        (common.PROJECT_NAME, common.ADMIN_EMAIL_ADDRESS),
    )
    MANAGERS = ADMINS

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        },
    },
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        }
    },
    "handlers": {
        "rollbar": {
            "level": "WARN",
            "class": "rollbar.logger.RollbarHandler",
            "filters": ["require_debug_false"],
        },
        "django": {
            "level": "ERROR",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": f"/var/log/{PROJECT_ID}/django.log",
            "maxBytes": 50000000,
            "backupCount": 3,
            "formatter": "standard",
        },
        f"{PROJECT_ID}_app": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": f"/var/log/{PROJECT_ID}/app.log",
            "maxBytes": 50000000,
            "backupCount": 3,
            "formatter": "standard",
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["django", "rollbar"],
            "level": "ERROR",
            "propagate": False,
        },
        "{%PROJECT_ID_LOWER%}.app": {
            "handlers": [f"{PROJECT_ID}_app", "rollbar"],
            "level": "INFO",
        },
    }
}

# Cache

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.environ.get("{%PROJECT_ID_UPPER%}_REDIS_HOST"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
}

# Database

DATABASES = {
    "default": {
        "NAME": os.environ.get("{%PROJECT_ID_UPPER%}_DB_NAME"),
        "ENGINE": "django.db.backends.mysql",
        "HOST": os.environ.get("{%PROJECT_ID_UPPER%}_DB_HOST"),
        "USER": os.environ.get("{%PROJECT_ID_UPPER%}_DB_USER"),
        "PASSWORD": os.environ.get("{%PROJECT_ID_UPPER%}_DB_PASSWORD"),
    }
}
