#!/usr/bin/env python3
"""Pagination helper function.
"""
from typing import Tuple


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Takes two integer arguments `page` and `page_size`.
    The function should return a tuple of size two containing a
    start index and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters.

    Args:
        page (int): The current page number.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
