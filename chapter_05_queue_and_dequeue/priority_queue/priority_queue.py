class PriorityQueue:
    def __init__(self):
        self._items = []

    def __str__(self):
        return f"queue: {self._items}"

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def clear(self):
        self._items = []

    def enqueue(self, item):
        self._items.append(item)

    def find_max_index(self):
        if self.is_empty():
            return None

        highest_index = 0

        for i in range(self.size()):
            if self._items[i] > self._items[highest_index]:
                highest_index = i

        return highest_index

    def dequeue(self):
        return self._items.pop(self.find_max_index())

    def peek(self):
        return self._items[self.find_max_index()]


# test
def test_priority_queue_priority_check():
    pq = PriorityQueue()

    pq.enqueue(30)
    pq.enqueue(10)
    pq.enqueue(20)

    assert pq.find_max_index() == 0


def test_priority_queue_find_most_prior_element():
    pq = PriorityQueue()

    pq.enqueue(10)
    pq.enqueue(20)
    pq.enqueue(30)

    assert pq.peek() == 30


def test_priority_queue_integration():
    q = PriorityQueue()

    q.enqueue(34)
    q.enqueue(18)
    q.enqueue(27)
    q.enqueue(45)
    q.enqueue(15)

    pool = []
    while not q.is_empty():
        element = q.dequeue()
        pool.append(element)

    expect_result = [45, 34, 27, 18, 15]

    assert pool == expect_result
