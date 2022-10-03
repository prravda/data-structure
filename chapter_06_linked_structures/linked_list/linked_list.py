from typing import Optional, Any
from chapter_06_linked_structures.node import Node


class LinkedList:
    def __init__(self):
        self.__head: Optional[Node] = None

    # basic methods definition
    def is_empty(self):
        return self.__head is None

    def clear(self):
        self.__head = None

    def size(self) -> int:
        size_of_list = 0
        current_node = self.__head

        while current_node is not None:
            size_of_list += 1
            current_node = current_node.link

        return size_of_list

    def display(self):
        container = []
        current_node = self.__head

        while current_node is not None:
            container.append(current_node.data)
            current_node = current_node.link

    # linkedlist-specific methods definition
    def get_node(self, position: int) -> Optional[Node]:
        if position < 0:
            return None

        counter = position
        current_node = self.__head

        # using while loop with two condition
        # - counter is larger than 0
        # - current_node is not None
        # for cover this case:
        #   if position is larger than the back-most node's
        #   stop the counting
        while counter > 0 and current_node is not None:
            counter -= 1
            current_node = current_node.link

        return current_node

    def get_entry(self, position: int) -> Any:
        node = self.get_node(position)

        if not node:
            return None
        return node.data

    def replace(self, position: int, data: Any) -> None:
        target = self.get_node(position)
        target.data = data

    def find(self, value_to_find: int):
        current_node = self.__head

        while current_node is not None:
            if current_node.data == value_to_find:
                return current_node

        return None

    def insert(self, position: int, data: Any) -> None:
        node_before_insert = self.get_node(position - 1)

        # if there is no node in position 'th index
        # insert this node at front most
        if node_before_insert is None:
            self.__head = Node(data, self.__head)

        else:
            # if there is node
            # - make a node with data argument
            #   and a link of node_before_insert
            node_to_insert = Node(data, node_before_insert.link)
            # after do this, assign #1
            # into the node_before_insert.link
            node_before_insert.link = node_to_insert

    def delete(self, position) -> None:
        node_before_deletion = self.get_node(position - 1)

        if node_before_deletion is None:
            if self.__head is not None:
                self.__head = self.__head.link

        elif node_before_deletion.link is not None:
            node_before_deletion.link = node_before_deletion.link.link

    # practice 6.2
    # implement merge
    # update itself
    def merge(self, another_linked_list: 'LinkedList') -> None:
        current_size = self.size()
        current_size_another_list = another_linked_list.size()

        while not another_linked_list.is_empty():
            current_node_from_another = another_linked_list.get_node(0)
            self.insert(current_size, current_node_from_another.data)
            current_size += 1

            another_linked_list.delete(current_size_another_list)
            current_size_another_list -= 1


def test_linked_list_insertion():
    linked_list = LinkedList()
    index_to_allocate = 0
    data_to_allocate = 10
    linked_list.insert(index_to_allocate, data_to_allocate)

    linked_list.get_entry(index_to_allocate) == data_to_allocate


def test_linked_list_deletion():
    linked_list = LinkedList()
    number_of_allocation = 5
    for i in range(0, number_of_allocation):
        linked_list.insert(i, i)

    linked_list.delete(number_of_allocation - 1)

    linked_list.size() != number_of_allocation


def test_linked_list_replacement():
    linked_list = LinkedList()
    index_to_allocate = 0
    number_to_allocate = 10
    number_to_re_allocate = 20

    linked_list.insert(index_to_allocate, number_to_allocate)
    linked_list.replace(index_to_allocate, number_to_re_allocate)

    assert linked_list.get_entry(index_to_allocate) != number_to_allocate


def test_linked_list_merge():
    # create a list
    linked_list = LinkedList()
    number_of_insertion = 3

    for i in range(number_of_insertion):
        linked_list.insert(i, i)

    size_before_merge = linked_list.size()

    # create list which will be merged into #1
    linked_list_to_merge = LinkedList()

    for i in range(number_of_insertion):
        linked_list_to_merge.insert(i, i+1)

    # merge
    linked_list.merge(linked_list_to_merge)

    size_after_merge = linked_list.size()

    # compare the size of list before and after merging
    assert size_before_merge != size_after_merge





