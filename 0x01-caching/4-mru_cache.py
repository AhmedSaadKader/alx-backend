#!/usr/bin/python3
"""MRU Cache
"""
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRU Cache"""
    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache using MRU algorithm"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the existing key and move it to the end (most recently used)
            self.cache_data.move_to_end(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # MRU: remove the most recently used item
                last_key, _ = self.cache_data.popitem(last=True)
                print(f"DISCARD: {last_key}")

        # Add/Update the key-value pair in the cache
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        # Move the key to the end to mark it as recently used
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
