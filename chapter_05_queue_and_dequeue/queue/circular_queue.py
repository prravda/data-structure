from typing import Any


class OverFlowException(Exception):
    def __str__(self) -> str:
        return "queue is full"


class UnderFlowException(Exception):
    def __str__(self) -> str:
        return "queue is empty"


class CircularQueue:
    def __init__(self, size: int = 8):
        self._limit: int = size
        self._storage: list[Any] = [None for _ in range(self._limit)]
        self._front: int = 0
        self._rear: int = 0

    def __str__(self) -> str:
        return f"0-circular-queue_handson: {self._storage}\nordered_by_index: {self.display()}\nfront: {self._front}\nrear: {self._rear}" \
               f"\nlength: {self.get_size()}\n\n"

    def get_size(self) -> int:
        # it returns a current length
        # not limit
        return (self._rear - self._front + self._limit) % self._limit

    def is_empty(self) -> bool:
        return self._front == self._rear

    def is_full(self) -> bool:
        return self._front == (self._rear + 1) % self._limit

    def enqueue(self, element: Any) -> None:
        # check whether the queue is full or not
        if self.is_full():
            raise OverFlowException()

        # manage index - rear
        self._rear = (self._rear + 1) % self._limit
        self._storage[self._rear] = element

    def dequeue(self) -> Any:
        # check whether the queue is empty
        if self.is_empty():
            raise UnderFlowException()

        # manage index - front
        self._front = (self._front + 1) % self._limit

        # assign an variable
        # and save the queue's updated self._front's element
        temp = self._storage[self._front]

        # and re-assign the element by location with None
        self._storage[self._front] = None

        # return the variable before stored
        return temp

    def peek(self):
        # return front-most element
        # because it is a queue
        return self._storage[(self._front + 1) % self._limit]

    def display(self) -> list:
        if self._rear > self._front:
            # in this case, just print
            # from next element of front to rear
            return self._storage[self._front + 1: self._rear + 1]

        # if front is larger than rear,
        # merge two list into one and print
        # - from rear to last
        # - from first to front
        return self._storage[self._front + 1:] + self._storage[:self._rear + 1]


q = CircularQueue(8)

print("---enqueue---\n\n")
for i in range(7):
    q.enqueue(i)
    print(q)

print("---dequeue---\n\n")
for _ in range(3):
    q.dequeue()
    print(q)

print("---enqueue---\n\n")
for i in range(3):
    q.enqueue(i)
    print(q)
