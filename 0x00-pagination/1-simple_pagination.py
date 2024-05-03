#!/usr/bin/env python3
""" Documentation """

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> tuple:
        """
        Calculate the start and end indices for a given page and page size.

        Args:
            page (int): The page number.
            page_size (int): The number of items per page.

        Returns:
            tuple: A tuple containing the start and end indices.

        """
        start = (page - 1) * page_size
        end = start + page_size
        return (start, end)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a specific page of data from the dataset.

        Args:
            page (int): The page number to retrieve (default is 1).
            page_size (int): The number of items per page (default is 10).

        Returns:
            List[List]: The data for the specified page.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        start, end = self.index_range(page, page_size)
        assert page >= 0 and page_size > 0
        return self.dataset()[start:end]
