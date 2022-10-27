from typing import Any
from abc import ABC, abstractmethod


class Entry:
    def __init__(
            self,
            key: str,
            val: Any,
    ):
        self.key = key
        self.val = val


class MapADT(ABC):
    @abstractmethod
    def search(self, key: str) -> str:
        pass

    @abstractmethod
    def insert(self, entry: Entry) -> None:
        pass

    @abstractmethod
    def delete(self, key: str) -> None:
        pass
