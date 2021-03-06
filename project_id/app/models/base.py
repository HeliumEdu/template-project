import logging

from django.db import models

__author__ = "Alex Laird"
__copyright__ = "Copyright 2018, Helium Edu"
__version__ = "1.0.2"

logger = logging.getLogger(__name__)


class BaseModel(models.Model):
    """
    The abstract base model from which most other models should inherit to ensure common base attributes.
    """

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
