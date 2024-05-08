#!/usr/bin/python3
""" FIFO Caching alghorithme """

from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """
    FIFOCache class represents a First-In-First-Out (FIFO) cache.

    It inherits from the BaseCaching class
    and implements the put and get methods.

    Attributes:
        cache_data (OrderedDict): A dictionary-like object
        that maintains the order of insertion.

    Methods:
        put(key, item): Inserts an item into the cache with the given key.
        get(key): Retrieves the item
        associated with the given key from the cache.

    """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Inserts an item into the cache with the given key.

        If the cache is full,
        the oldest item (according to insertion order) will be discarded.

        Args:
            key: The key to associate with the item.
            item: The item to be inserted into the cache.

        Returns:
            None

        """
        data = self.cache_data
        if key is None or item is None:
            return
        data[key] = item
        if len(data) > BaseCaching.MAX_ITEMS:
            first_key, _ = data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """
        Retrieves the item associated with the given key from the cache.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item associated with the given key,
            or None if the key is not found in the cache.
        """
        return self.cache_data.get(key)
