from chapter_05_queue_and_dequeue.circular_queue.circular_queue import *


class CircularDequeue(CircularQueue):
    def __init__(self, size):
        super().__init__(size)

    # cover up the circular circular_queue's method
    # into the circular dequeue
    def add_rear(self, element) -> None:
        self.enqueue(element)

    def delete_front(self) -> Any:
        return self.dequeue()

    def get_front(self) -> Any:
        return self.peek()

    # add front's index management strategy is
    # reverse of circular_queue
    # so, first -1 to front and add the limit,
    # second, modulo calculation to this value
    # and the front is empty,
    # so set element to the front index before manipulation
    def add_front(self, element: Any) -> None:
        # before do this, check whether this dequeue is full or not
        if self.is_full():
            raise OverFlowException

        # if the dequeue is not full,
        # go to the next processes
        self._storage[self._front] = element
        self._front = (self._front - 1 + self._limit) % self._limit

    def delete_rear(self) -> Any:
        # before do this, check whether this dequeue is empty
        if self.is_empty():
            raise UnderFlowException

        # if the dequeue is not empty
        # go to the next processes
        temp = self._storage[self._rear]
        # assign None as a mark of empty index
        self._storage[self._rear] = None
        # index management
        self._rear = (self._rear - 1 + self._limit) % self._limit
        # return stored value
        return temp

    def get_rear(self) -> Any:
        return self._storage[self._rear]


# test
def test_circular_dequeue_add_front():
    dq = CircularDequeue(10)
    # test add_front
    test_number_one = 3
    for i in range(0, test_number_one):
        dq.add_front(i)

    assert dq.get_size() == test_number_one


def test_circular_dequeue_delete_front():
    dq = CircularDequeue(10)
    test_number_one = 3
    temp_storage_for_compare = []
    for i in range(0, test_number_one):
        temp_storage_for_compare.append(i)
        dq.add_front(i)

    test_number_two: int = 2
    temp_storage: list[Any] = []
    for i in range(0, test_number_two):
        temp_storage.append(dq.delete_front())

    assert temp_storage == temp_storage_for_compare[::-1][:test_number_two]
