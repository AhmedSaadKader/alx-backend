#!/usr/bin/env python3
import csv
import math
from typing import List
"""Simple pagination"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Takes two integer arguments page and page_size.
    Returns a tuple of size two containing a
    start index and an end index corresponding to the range of
    indexes to return in a list for those particular pagination parameters.
    Page numbers are 1-indexed, i.e. the first page is page 1.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


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
        """return the appropriate page of the dataset {Popular_Baby_names.csv}
        """
        assert (type(page) is int and type(page_size) is int)
        assert (page > 0 and page_size > 0)
        indexTuple = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[indexTuple[0]:indexTuple[1]]
