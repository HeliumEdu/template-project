import json

from django.db import IntegrityError
from django.urls import reverse
from mock import mock
from rest_framework import status
from rest_framework.test import APITestCase

__author__ = "Alex Laird"
__copyright__ = "Copyright 2019, Helium Edu"
__version__ = "1.0.3"


class TestCaseStatusViews(APITestCase):
    @mock.patch('health_check.db.backends.DatabaseBackend.check_status')
    @mock.patch('health_check.cache.backends.CacheBackend.check_status')
    def test_status(self, mock_cache, mock_db):
        # WHEN
        response = self.client.get(reverse('resource_status'))

        # THEN
        content = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(content['components']), 2)
        self.assertEqual(content['status'], 'operational')

        for component in content['components']:
            self.assertEqual(content['components'][component]['status'], 'operational')

    @mock.patch('health_check.db.models.TestModel.objects.create')
    @mock.patch('health_check.cache.backends.CacheBackend.check_status')
    def test_status_critical_fails(self, mock_cache, mock_db):
        # GIVEN
        mock_db.side_effect = IntegrityError("Database integrity error")

        # WHEN
        response = self.client.get(reverse('resource_status'))

        # THEN
        content = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(len(content['components']), 2)
        self.assertEqual(content['status'], 'minor_outage')

        for component in content['components']:
            if component == 'Database':
                self.assertEqual(content['components'][component]['status'], 'minor_outage')
