#!/usr/bin/env python3
"""task 3 lifo_cache """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache  class"""

    def __init__(self):
        super().__init__()
        self.cache_order = []

    def get(self, key):
        """Add an item in the cache"""

        if key is None:
            return None
        return self.cache_data.get(key, None)

    def put(self, key, item):
        """put an item"""
        if key is None or item is None:
            pass
        else:
            if len(self.cache_order) >= BaseCaching.MAX_ITEMS:

                print(f"DISCARD: {self.cache_order[-1]}")
                del self.cache_data[self.cache_order[-1]]
                self.cache_order.pop(-1)
                self.cache_order.append(key)
                self.cache_data[key] = item

            else:
                self.cache_order.append(key)
                self.cache_data[key] = item
