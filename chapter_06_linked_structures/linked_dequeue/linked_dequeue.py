from typing import Optional
from chapter_06_linked_structures.linked_dequeue.doubly_node import DoublyNode


class LinkedDequeue:
    def __init__(self):
        self.__front: Optional[DoublyNode] = None
        self.__rear: Optional[DoublyNode] = None

    def is_empty(self) -> bool:
        return self.__front is None

    def clear(self) -> None:
        self.__front = self.__rear = None

    def size(self) -> int:
        current_node = self.__front
        size_of_dequeue = 0

        while current_node is not None:
            size_of_dequeue += 1
            current_node = current_node.next

        return size_of_dequeue

    def display(self) -> list[int]:
        current_node = self.__front
        elements_in_dequeue = []

        while current_node is not None:
            elements_in_dequeue.append(current_node.data)
            current_node = current_node.next

        return elements_in_dequeue

    def add_front(self, element: int) -> None:
        node_to_add = DoublyNode(element, None, self.__front)

        if self.is_empty():
            self.__front = self.__rear = node_to_add
            return

        self.__front.prev = node_to_add
        self.__front = node_to_add

    def delete_front(self) -> int:
        if self.is_empty():
            raise Exception("This dequeue is empty")

        node_to_return = self.__front
        self.__front = self.__front.next

        if self.__front is None:
            self.__rear = None

        self.__front.prev = None

        return node_to_return.data

    def add_rear(self, element: int) -> None:
        node_to_add = DoublyNode(element, self.__rear, None)

        if self.is_empty():
            self.__front = self.__rear = node_to_add
            return

        self.__rear.next = node_to_add
        self.__rear = node_to_add

    def delete_rear(self) -> int:
        if self.is_empty():
            raise Exception("This dequeue is empty")

        node_to_return = self.__rear
        self.__rear = self.__rear.prev

        if self.__rear is None:
            self.__front = None

        self.__rear.next = None

        return node_to_return.data
