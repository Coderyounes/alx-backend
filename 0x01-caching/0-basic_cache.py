#!/usr/bin/python3
""" Base Caching """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
        A class BasicCache inherent from BaseCaching
    """
    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key of the item.
            item: The item to be added to the cache.
        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item associated with the given key,
            or None if the key is not found in the cache.
        """
        return self.cache_data.get(key)
