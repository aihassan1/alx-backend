#!/usr/bin/python3
"""task 0 """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache"""

    def get(self, key):
        """get the value of the a key in the cache"""
        if key is None:
            return None
        return self.cache_data.get(key, None)

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
