# TODO: Error handling
class List:
    def __init__(self):
        self.storage = []

    def get(self, index):
        return self.storage[index]

    def insert(self, index, element):
        return self.storage.insert(index, element)

    def remove(self):
        if len(self.storage) != 0:
            self.storage.remove(len(self.storage) - 1)

    def remove_at(self, index):
        self.storage.remove(index)

    def replace(self, index, element):
        self.storage[index] = element

    def size(self):
        return len(self.storage)

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        for element in self.storage:
            if element is None:
                return False
        return True


listInstance = List()

listInstance.insert(0, 'a')
listInstance.insert(1, 'b')
listInstance.insert(2, 'c')
listInstance.insert(3, None)

print(listInstance.is_full())