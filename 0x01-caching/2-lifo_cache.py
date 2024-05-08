#!/usr/bin/python3
""" FIFO Caching alghorithme """

from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """
    LIFOCache class represents a Last-In-First-Out (LIFO) caching mechanism.

    Attributes:
        cache_data (OrderedDict): A dictionary-like object
        that maintains the order of insertion.

    Methods:
        put(key, item): Adds an item to
        the cache with the specified key.
        get(key): Retrieves the item associated with
        the specified key from the cache.
    """

    def __init__(self):
        """ Init Method """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds an item to the cache with the specified key.

        Args:
            key: The key to associate with the item.
            item: The item to be added to the cache.

        Returns:
            None
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

    def get(self, key):
        """
        Retrieves the item associated with the specified key from the cache.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item associated with the specified key,
            or None if the key is not found in the cache.
        """
        return self.cache_data.get(key)
