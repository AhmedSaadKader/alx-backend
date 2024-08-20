#!/usr/bin/env python3
"""LIFO cache"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Last in First out Caching system"""
    def __init__(self):
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """Add an item in the cache using LIFO algorithm"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the existing key and maintain the order
            self.cache_data[key] = item
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if self.last_key:
                    # LIFO: remove the last item added to the cache
                    del self.cache_data[self.last_key]

            # Add the new key
            self.cache_data[key] = item

        self.last_key = key

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
