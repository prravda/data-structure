# Refactor the linked stack
# requirements
# - make the time complexity of size() method
#   from O(n) to O(1)

from chapter_06_linked_structures.node import Node
from typing import Any, Optional


class LinkedStackRefactored:
    def __init__(self):
        self.__top: Optional[Node] = None
        self.__size: int = 0

    def push(self, element: Any) -> None:
        self.__size += 1

        self.__top = Node(element, self.__top)

    def pop(self) -> Any:
        self.__size -= 1

        last_node = self.__top
        self.__top = self.__top.link

        return last_node.data

    def peek(self) -> Any:
        return self.__top.data

    def size_refactored(self) -> int:
        return self.__size


# test
def test_size_refactored():
    stack = LinkedStackRefactored()

    elements = [0, 1, 2, 3]
    for e in elements:
        stack.push(e)

    assert stack.size_refactored() == len(elements)

    number_of_pop = 2
    for _ in range(0, number_of_pop):
        stack.pop()

    assert stack.size_refactored() == len(elements) - number_of_pop



