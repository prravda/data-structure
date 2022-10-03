from chapter_06_linked_structures.node import Node
from typing import Any, Optional


class LinkedStack:
    def __init__(self):
        # when the LinkedStack class is just created
        # the property '_top' assigned None as default
        self._top: Optional[Node] = None

    def __str__(self):
        print(self.display())

    def is_emtpy(self) -> None:
        return self._top is None

    def clear(self) -> None:
        self._top = None

    def push(self, element) -> None:
        # 1. Create a node with element argument
        # 2. Set #1's link property as (current) _top property
        #    of this LinkedStack
        new_node = Node(element, self._top)
        # 3. Set #2 as current LinkedStack's _top property
        self._top = new_node

    def pop(self) -> Any:
        # Before run this method,
        # check whether this linked stack is empty or not
        if not self.is_emtpy():
            # 0. Basically, the pop method
            #    should return the _top element
            # 1. So create a temporary variable (like 'next__top')
            # 2. Set current _top(self._top) into #1
            next__top = self._top
            # 3. Set #2's link property into current _top(self._top)
            self._top = next__top.link
            # 4. return #2's data as a result
            return next__top.data

    def peek(self) -> Any:
        if not self.is_emtpy():
            # Just return the _top's data
            return self._top.data

    # the reference of code size() in this book
    def size(self) -> int:
        # 0-0. Declare a variable 'size_of_stack'
        #      to hold the size of this LinkedStack
        #      and assign 0 as an initial value of it
        size_of_stack = 0
        # 0-1. Declare a variable current_node
        #      to using for iteration which checks
        #      whether current node is None or not
        current_node = self._top

        # 1. iterate with while condition
        #    till current_node is None
        while current_node is not None:
            # 2. plus 1 into size_of_stack
            size_of_stack += 1
            # 3. re-assign the current_node's link
            #    into the variable current_node
            current_node = current_node.link

        return size_of_stack

    def display(self) -> list[Any]:
        container = []
        current = self._top

        while current is not None:
            current = current.link
            container.append(current.data)

        return current


# test
def test_linked_stack_push_and_pop():
    linked_stack = LinkedStack()
    elements = [0, 1, 2, 3]

    for e in elements:
        linked_stack.push(e)

    last_data = linked_stack.pop()

    assert last_data == elements[-1]


def test_linked_stack_push_and_peek():
    linked_stack = LinkedStack()
    elements = [0, 1, 2, 3]

    for e in elements:
        linked_stack.push(e)

    last_data = linked_stack.peek()

    assert last_data == elements[-1]
    assert linked_stack.size() == len(elements)


def test_linked_stack_size():
    linked_stack = LinkedStack()
    elements = [0, 1, 2, 3]

    for e in elements:
        linked_stack.push(e)

    assert linked_stack.size() == len(elements)
