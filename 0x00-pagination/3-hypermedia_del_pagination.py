#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> dict:
        """Retrieves info about a page from a
        given index and with a specified size."""
        assert isinstance(index, int) and index >= 0 and index is not None

        data = self.indexed_dataset()
        assert index <= max(data.keys())

        start_index = index
        end_index = start_index + page_size

        page_data = list(data.items())[start_index:end_index]

        page_info = {
            'index': start_index,
            'data': [item for _, item in page_data],
            'page_size': len(page_data),
            'next_index': end_index if end_index < len(data) else None,
        }

        return page_info
