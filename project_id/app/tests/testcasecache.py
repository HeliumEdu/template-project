from django.core.cache import cache
from django.test import TestCase

__author__ = "Alex Laird"
__copyright__ = "Copyright 2019, Helium Edu"
__version__ = "1.1.0"


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
