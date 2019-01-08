import logging

from rest_framework import serializers

__author__ = "Alex Laird"
__copyright__ = "Copyright 2019, Helium Edu"
__version__ = "1.0.3"

logger = logging.getLogger(__name__)


class InfoSerializer(serializers.Serializer):
    name = serializers.CharField()

    version = serializers.CharField()

    support_email = serializers.EmailField()
