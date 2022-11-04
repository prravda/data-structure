import math
from typing import Optional
from chapter_07_sorting_and_searching.map_structure.map_adt import *


class Map(MapADT):
    def __init__(self):
        self.__storage: list[Entry] = []

    def sequential_search(
            self,
            key: str,
            low: Optional[int] = 0,
            high: Optional[int] = 0,
    ) -> Optional[int]:
        """
        find an index of entry in this map
        using 'key' parameter

        :param key: key to find, str type
        :param low: minimum index to find, int type, default value is 0
        :param high: maximum index to find, int type, default value is length of self.__storage (processed internally)

        :return: index of the entry which key is same with the input 'key', but there is no entry, return None alternatively.
        """
        if high == 0:
            high = len(self.__storage)

        for i in range(low, high + 1):
            if self.__storage[i].key == key:
                return i

        return None

    def binary_search(
            self,
            value_to_find: int,
            start_idx: int,
            end_idx: int,
    ) -> Optional[int]:
        """
        find an element
        :return:
        """
        if start_idx >= end_idx:
            return None

        mid_idx = math.floor((start_idx + end_idx) / 2)
        mid_val = self.__storage[mid_idx]

        if mid_val == value_to_find:
            return mid_idx

        if mid_val > value_to_find:
            self.binary_search(value_to_find, start_idx, mid_idx - 1)

        if mid_val < value_to_find:
            self.binary_search(value_to_find, mid_idx + 1, end_idx)

    def search(self, key: str) -> str:
        pass

    def insert(self, entry: Entry) -> None:
        pass

    def delete(self, key: str) -> None:
        pass
