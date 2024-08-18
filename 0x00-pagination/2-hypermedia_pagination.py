#!/usr/bin/env python3
import csv
import math
from typing import List
"""Hypermedia pagination"""


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Returns a dictionary with the following key-value pairs
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer

        Args:
            page (int, optional): page number. Defaults to 1.
            page_size (int, optional): page size. Defaults to 10.

        Returns:
            dict: _description_
        """
        current_index = index_range(page, page_size)
        pages = self.get_page(page, page_size)
        hyper_dict = {}
        hyper_dict['page_size'] = len(pages)
        hyper_dict['page'] = page
        hyper_dict['data'] = pages
        try:
            if self.dataset()[current_index[1]]:
                hyper_dict['next_page'] = page + 1
        except IndexError:
            hyper_dict['next_page'] = None
        if (page == 1):
            hyper_dict['prev_page'] = None
        else:
            hyper_dict['prev_page'] = page - 1
        total_pages = len(self.dataset()) / page_size
        hyper_dict['total_pages'] = math.ceil(total_pages)

        return hyper_dict
