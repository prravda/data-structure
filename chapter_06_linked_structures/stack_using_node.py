# TODO: 그림을 그려가면서 이해 해보기

from typing import Optional
from node import Node


class LinkedStack:
    def __init__(self):
        self.top: Optional[Node] = None

    def is_empty(self):
        return self.top is None

    def clear(self):
        self.top = None

    def push(self, item):
        temp = Node(item, self.top)
        self.top = temp

    def pop(self):
        temp = self.top
        self.top = temp.link
        return temp.val

    def peek(self):
        return self.top.val

    def size(self):
        current_node = self.top
        size_of_stack = 0

        while current_node is not None:
            size_of_stack += 1
            current_node = current_node.link

        return size_of_stack
