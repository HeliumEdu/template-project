import logging

from django.conf import settings
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from {%PROJECT_ID_LOWER%}.app.serializers.infoserializer import InfoSerializer

__author__ = "Alex Laird"
__copyright__ = "Copyright 2019, Helium Edu"
__version__ = "1.0.3"

logger = logging.getLogger(__name__)


class InfoResourceView(ViewSet):
    """
    info:
    Return version and configuration information about the app.
    """

    def info(self, request, *args, **kwargs):
        serializer = InfoSerializer({
            'name': settings.PROJECT_NAME,
            'version': settings.PROJECT_VERSION,
            'support_email': settings.EMAIL_ADDRESS
        })

        return Response(serializer.data)
