from typing import Optional


# set node's next link to next node
class Node:
    def __init__(self, val: Optional[int] = None, link: Optional["Node"] = None):
        self.val = val
        self.link = link


# singly linked list
singly_linked_list = Node(1)
singly_linked_list.link = Node(2)
singly_linked_list.link.link = Node(3)

# circular linked list
circular_linked_list = Node(1)
circular_linked_list.link = Node(2)
circular_linked_list.link.link = Node(3)
circular_linked_list.link.link.link = circular_linked_list

# TODO: implement doubly linked list with inheriting the Node class
