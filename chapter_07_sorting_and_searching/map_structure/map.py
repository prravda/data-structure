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

        :return: index of the entry which key is same with the input 'key'
        """
        if high == 0:
            high = len(self.__storage)

        for i in range(low, high + 1):
            if self.__storage[i].key == key:
                return i

        return None

    def search(self, key: str) -> str:
        pass

    def insert(self, entry: Entry) -> None:
        pass

    def delete(self, key: str) -> None:
        pass
