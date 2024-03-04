__copyright__ = "Copyright (c) 2024 Helium Edu"
__license__ = "MIT"

import logging

from rest_framework import serializers

logger = logging.getLogger(__name__)


class InfoSerializer(serializers.Serializer):
    name = serializers.CharField()

    version = serializers.CharField()

    support_email = serializers.EmailField()
