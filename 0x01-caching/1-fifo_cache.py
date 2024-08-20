#!/usr/bin/env python3
"""FIFO cache"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """First in First out Caching system"""
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item in the cache using FIFO algorithm"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the existing key and maintain the order
            self.cache_data[key] = item
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # FIFO: remove the first item added to the cache
                first_key = self.order.pop(0)
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

            # Add the new key
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
