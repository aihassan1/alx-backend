#!/usr/bin/env python3
""" task 1 Simple pagination
"""

from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Args:
        page (int): The current page number.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a specific page of data from the dataset.

        Args:
            page (int): The page number to retrieve (default is 1).
            page_size (int): The number of items per page (default is 10).

        Returns:
            List[List]: A list of lists representing
            the items on the requested page.

        Raises:
            AssertionError: If either `page` or `page_size`
            is not an integer greater than 0.

        """
        # Use assert to verify that both arguments are integers greater than 0.
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        idx_results = index_range(page, page_size=page_size)
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        idx_results = index_range(page, page_size=page_size)
        if (idx_results[0] > len(self.dataset()) or
                idx_results[1] > len(self.dataset())):
            return []

        dataset_result = self.dataset()

        page_items = dataset_result[idx_results[0]:idx_results[1]]
        return page_items
