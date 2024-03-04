__copyright__ = "Copyright (c) 2024 Helium Edu"
__license__ = "MIT"

from django.core.cache import cache
from django.test import TestCase


class TestCaseCache(TestCase):
    def tearDown(self):
        cache.clear()

    def test_cache_keys(self):
        # WHEN
        cache.set("key", "value")

        # THEN
        self.assertEqual(len(cache.keys("*")), 1)

        # WHEN
        cache.delete("key")

        # THEN
        self.assertEqual(len(cache.keys("*")), 0)
