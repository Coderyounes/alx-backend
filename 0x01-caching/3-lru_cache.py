#!/usr/bin/env python3
""" DOcumentation """

from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Least Recently Used (LRU) Cache implementation.

    Inherits from BaseCaching class.

    Attributes:
        cache_data (OrderedDict): A dictionary-like object
        that maintains the order of insertion.
    """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache.

        If the cache is full, the least recently used item is discarded.

        Args:
            key: The key of the item.
            item: The item to be added to the cache.

        Returns:
            None
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        If the item exists in the cache, it is moved to
        the front to indicate it was recently used.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item associated with the key,
            or None if the key is not found in the cache.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
