#!/usr/bin/env python3
"""Write a function named index_range that
takes two integer arguments page and page_size
"""


from typing import Tuple, List
import csv


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


    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return the appropriate page of the dataset"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        # get the data from the csv
        data = self.dataset()

        try:
            start, end = index_range(page, page_size)
            return data[start:end]
        except IndexError:
            return []

