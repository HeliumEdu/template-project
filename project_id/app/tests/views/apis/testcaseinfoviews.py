__copyright__ = "Copyright (c) 2024 Helium Edu"
__license__ = "MIT"

from django.conf import settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestCaseInfoViews(APITestCase):
    def test_info(self):
        # WHEN
        response = self.client.get(reverse("resource_info"))

        # THEN
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(settings.PROJECT_NAME, response.data["name"])
        self.assertEqual(settings.PROJECT_VERSION, response.data["version"])
        self.assertEqual(settings.EMAIL_ADDRESS, response.data["support_email"])
