# TODO: implement priority circular_queue
class PriorityQueue:
    def __init__(self):
        self.items = []

    def __str__(self):
        return f"queue: {self.items}"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    # TODO: something is wrong
    def find_max_index(self):
        if self.is_empty():
            return None

        highest_index = 0

        for i in range(self.size()):
            if self.items[i] > self.items[highest_index]:
                highest_index = i

        return highest_index

    def dequeue(self):
        index = self.find_max_index()
        print(index)
        return self.items.pop()

    def peek(self):
        return self.items[self.find_max_index()]


# test
# def test_priority_queue():
#     q = PriorityQueue()
#     q.enqueue(34)
#     q.enqueue(18)
#     q.enqueue(27)
#     q.enqueue(45)
#     q.enqueue(15)
#
#     print(q)
#
#     pool = []
#     while q.is_empty():
#         pool.append(q.dequeue())
#
#     expect_result = [45, 34, 27, 18, 15]
#
#     assert pool == expect_result