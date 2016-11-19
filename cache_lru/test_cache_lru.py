import unittest

from cache_lru.cache_lru import CacheLRU


class TestCacheLRU(unittest.TestCase):

    def setUp(self):
        self.cache_lru = CacheLRU(5)

    def test_small_cache_size(self):
        self.assertRaises(Exception, CacheLRU, 1)

    def test_get_on_empty_cache(self):
        cache_lru = CacheLRU(5)

        result = cache_lru.get()

        self.assertEqual(result, [])

    def test_addition_to_cache(self):
        cache_lru = CacheLRU(5)

        cache_lru.add(1)
        result = cache_lru.get()

        self.assertEqual(result, [1])

    def test_addition_same_number_of_elements_and_size(self):
        cache_lru = CacheLRU(3)

        cache_lru.add(1)
        cache_lru.add(2)
        cache_lru.add(3)
        result = cache_lru.get()

        self.assertEqual(result, [1, 2, 3])

    def test_addition_to_cache_over_size(self):
        cache_lru = CacheLRU(2)

        cache_lru.add(1)
        cache_lru.add(2)
        cache_lru.add(3)
        result = cache_lru.get()

        self.assertEqual(result, [2, 3])

    def test_get_element(self):
        cache_lru = CacheLRU(2)

        cache_lru.add(1)
        result = cache_lru.get(1)

        self.assertEqual(result, 1)

    def test_get_element_update_cache(self):
        cache_lru = CacheLRU(2)

        cache_lru.add(1)
        cache_lru.add(2)
        cache_lru.get(1)
        cache_lru.add(3)
        result = cache_lru.get()

        self.assertEqual(result, [1, 3])
