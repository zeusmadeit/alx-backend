#!/usr/bin/env python3
"""Write a function named index_range that
takes two integer arguments page and page_size
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    pagination function

    Args:
        page(int) - page number
        page_size(int) - number of documents in page

    Returns - a tuple containing a start index and an end index.
    """
    # if page is 1, start at 0 and end at page_size
    # if page is 2, start at ((page-1) * page_size) and
    # end at (page_size * page)
    # if page is 3, start at ((page-1) * page_size) and
    # end at (page_size * page)
    return ((page-1) * page_size, page_size * page)
