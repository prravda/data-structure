from typing import Any


class CustomList:
    def __init__(self, *args) -> None:
        self.custom_list = list(args)

    def insert(self, index: int, element: Any):
        self.custom_list.insert(index, element)

    def display(self):
        print(self.custom_list)


custom_list = CustomList(1, 2, 3)
custom_list.display()