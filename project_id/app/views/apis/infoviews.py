__copyright__ = "Copyright (c) 2024 Helium Edu"
__license__ = "MIT"

import logging

from django.conf import settings
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from {%PROJECT_ID_LOWER%}.app.serializers.infoserializer import InfoSerializer

logger = logging.getLogger(__name__)


class InfoResourceView(ViewSet):
    """
    info:
    Return version and configuration information about the app.
    """

    def info(self, request, *args, **kwargs):
        serializer = InfoSerializer({
            "name": settings.PROJECT_NAME,
            "version": settings.PROJECT_VERSION,
            "support_email": settings.EMAIL_ADDRESS
        })

        return Response(serializer.data)
