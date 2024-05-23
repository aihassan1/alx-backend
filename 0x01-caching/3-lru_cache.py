#!/usr/bin/env python3
"""task 3. LRU Caching"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class"""

    def __init__(self):
        super().__init__()
        self.cache_order = []

    def get(self, key):
        """Add an item in the cache"""

        if key is None:
            return None
        if self.cache_data.get(key, None) is not None:
            self.cache_order.remove(key)
            self.cache_order.insert(0, key)
            return self.cache_data.get(key, None)
        else:
            return None

    def put(self, key, item):
        """put an item"""
        if key is None or item is None:
            pass
        else:
            if key in self.cache_order:
                self.cache_order.remove(key)

            if len(self.cache_order) >= BaseCaching.MAX_ITEMS:
                print(f"DISCARD: {self.cache_order[-1]}")
                del self.cache_data[self.cache_order[-1]]
                self.cache_order.pop(-1)

            self.cache_order.insert(0, key)
            self.cache_data[key] = item
