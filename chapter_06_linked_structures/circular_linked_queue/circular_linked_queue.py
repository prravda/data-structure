from chapter_06_linked_structures.node import Node
from typing import Optional


class CircularLinkedQueue:
    def __init__(self):
        self.__tail: Optional[Node] = None

    def is_empty(self) -> bool:
        return self.__tail is None

    def clear(self) -> None:
        self.__tail = None

    def peek(self) -> Optional[int]:
        if not self.is_empty():
            return self.__tail.data
        return None

    def enqueue(self, element: int) -> None:
        new_node = Node(element)

        if self.is_empty():
            new_node.link = new_node
            self.__tail = new_node
            return

        # goal: make back-most will-be node's next node
        #       to point current front-most node's memory address
        # set
        # - where: back-most will-be node's next node
        #   - via: new_node.link
        # - what: current front-most node's memory address
        #   - via: self.__tail.link
        new_node.link = self.__tail.link

        # goal: make current back-most node's next node
        #       to point back-most will-be node's memory address
        # set
        # - where: current back-most node's next node
        #   - via: self.__tail.link
        # - what: back-most will-be node's memory address
        #   - via: new_node
        self.__tail.link = new_node

        # goal: update the tail property to new back-most node
        # set
        # - where: self.__tail
        # - what: new_node
        self.__tail = new_node

    def dequeue(self) -> Optional[int]:
        # if the queue is empty, return None
        if self.is_empty():
            return None

        # make a variable 'node_to_return'
        # to hold the current front-most node
        #  - via self.__tail.link
        node_to_return = self.__tail.link

        # if there is only one element in queue,
        # set tail as None and return the variable, node_to_return
        if self.__tail is self.__tail.link:
            self.__tail = None
            return node_to_return.data

        # if there are elements more than 2 in queue,
        # set tail.link(== head) as tail.link.link(head.link)
        self.__tail.link = self.__tail.link.link
        # and return it
        return node_to_return.data

    def size(self) -> int:
        if self.is_empty():
            return 0

        count = 1
        current_node = self.__tail.link

        while current_node is not self.__tail:
            current_node = current_node.link
            count += 1

        return count

    def display(self) -> list[int]:
        if self.is_empty():
            return []

        container = []
        current_node = self.__tail.link

        while current_node is not self.__tail:
            container.append(current_node.data)
            current_node = current_node.link

        return container


def test_circular_linked_queue_enqueue():
    clq = CircularLinkedQueue()

    number_of_enqueue = 3

    for i in range(number_of_enqueue):
        clq.enqueue(i)

    assert clq.size() == number_of_enqueue


def test_circular_linked_queue_dequeue_after_enqueue():
    clq = CircularLinkedQueue()

    number_of_enqueue = 3
    first_element = 999999

    for i in range(number_of_enqueue):
        if i == 0:
            first_element = i
        clq.enqueue(i)

    head = clq.dequeue()

    assert first_element == head







