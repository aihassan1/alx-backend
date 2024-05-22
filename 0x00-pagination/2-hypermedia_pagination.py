#!/usr/bin/env python3
""" task 1 Simple pagination
"""

from typing import Tuple, List, Dict
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

        start_idx, end_idx = index_range(page, page_size=page_size)
        if start_idx > len(self.dataset()) or end_idx > len(self.dataset()):
            return []

        dataset_result = self.dataset()

        page_items = dataset_result[start_idx:end_idx]
        return page_items

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """returns a dictionary containing the following key-value pairs:

        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        """
        info = {}
        page_data = self.get_page(page, page_size)
        page_len = len(page_data)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        start, end = index_range(page, page_size)

        info["page_size"] = page_len
        info["page"] = page
        info["data"] = page_data
        info["next_page"] = page + 1 if end < len(self.__dataset) else None
        info["prev_page"] = page - 1 if start - 1 > 0 else None
        info["total_pages"] = total_pages

        return info
