#!/usr/bin/env python3
"""LRU cache"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRU Caching"""
    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache using LRU algorithm"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Move the key to the end to show it was recently used
            self.cache_data.move_to_end(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # LRU: remove the least recently used item
            self.cache_data.popitem(last=False)

        # Add/Update the key-value pair in the cache
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        # Move the key to the end to show it was recently used
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
