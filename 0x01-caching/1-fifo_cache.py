#!/usr/bin/python3
""" FIFO Caching alghorithme """

from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()


    def put(self, key, item):
        if key is not None and item is not None:
            data = self.cache_data
            if len(data) >= BaseCaching.MAX_ITEMS:
                first = next(iter(data))
                data.pop(first)
                print("DISCARD: {}".format(first))
            data.update({key: item})


    def get(self, key):
        return self.cache_data.get(key)