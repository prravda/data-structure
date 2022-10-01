class OverFlowException(Exception):
    def __str__(self) -> str:
        return "Queue is full"


class UnderFlowException(Exception):
    def __str__(self) -> str:
        return "Queue is empty"


class CircularQueue:
    def __init__(self, size: int = 8):
        self.__limit = size
        self.__storage = [None for _ in range(self.__limit)]
        self.__front = 0
        self.__rear = 0

    def __str__(self) -> str:
        self.display()
        return f"queue: {self.__storage}\nfront: {self.__front}\nrear: {self.__rear}\nlength: {self.get_size()}\n\n"

    def get_front(self) -> int:
        return self.__front

    def get_rear(self) -> int:
        return self.__rear

    def get_size(self) -> int:
        # it returns a current length
        # not limit
        return (self.__rear - self.__front + self.__limit) % self.__limit

    def is_empty(self) -> bool:
        return self.__front == self.__rear

    def is_full(self) -> bool:
        return self.__front == (self.__rear + 1) % self.__limit

    def enqueue(self, element):
        # check whether the queue is full or not
        if self.is_full():
            raise OverFlowException()

        # manage index - rear
        self.__rear = (self.__rear + 1) % self.__limit
        self.__storage[self.__rear] = element

    def dequeue(self):
        # check whether the queue is empty
        if self.is_empty():
            raise UnderFlowException()

        # manage index - front
        self.__front = (self.__front + 1) % self.__limit

        # assign an variable
        # and save the queue's updated self.__front's element
        temp = self.__storage[self.__front]

        # and re-assign the element by location with None
        self.__storage[self.__front] = None

        # return the variable before stored
        return temp

    def peek(self):
        # return front-most element
        # because it is a queue
        return self.__storage[(self.__front + 1) % self.__limit]

    def display(self) -> list:
        if self.__rear > self.__front:
            # in this case, just print
            # from next element of front to rear
            print(self.__storage[self.__front + 1: self.__rear + 1])
            return

        # if front is larger than rear,
        # merge two list into one and print
        # - from rear to last
        # - from first to front
        print(self.__storage[self.__front + 1:] + self.__storage[:self.__rear + 1])
        return


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
