# practice 6.3
# implement queue using the linked structure
# enqueue should use rear
# dequeue should use front

from typing import Optional
from chapter_06_linked_structures.node import Node


class LinkedQueue:
    def __init__(self):
        self.__front: Optional[Node] = None
        self.__rear: Optional[Node] = None

    def __str__(self) -> str:
        return f'{self.display()}'

    def display(self) -> list[int]:
        current_node = self.__front
        element_to_display = []

        while current_node is not None:
            element_to_display.append(current_node.data)
            current_node = current_node.link

        return element_to_display

    def enqueue(self, element: int) -> None:
        if self.__rear is None:
            self.__rear = Node(element)
            self.__front = self.__rear
            return

        self.__rear.link = Node(element)
        self.__rear = self.__rear.link

    def dequeue(self) -> Optional[int]:
        if self.__front is None:
            return None

        node_to_return = self.__front
        self.__front = self.__front.link

        return node_to_return.data

    def peek(self) -> Optional[int]:
        if self.__front is None:
            return None

        return self.__front.data


def test_linked_queue_set_one():
    queue = LinkedQueue()

    for i in range(10):
        queue.enqueue(i)

    assert queue.dequeue() == 0
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2


def test_linked_queue_set_two():
    queue = LinkedQueue()

    hero_list = ('superman', 'batman', 'wonder_woman' 'aquaman')

    for hero in hero_list:
        queue.enqueue(hero)

    assert queue.dequeue() == hero_list[0]
    assert queue.peek() == hero_list[1]



