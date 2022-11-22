from typing import Optional


class HeapTreeRefactored:
    def __init__(self):
        self.heap = [0]

    def size(self) -> int:
        return len(self.heap) - 1

    def is_empty(self) -> bool:
        return self.size() == 0

    def get_left_child(self, n: int) -> Optional[int]:
        """
        get the left child node of nth order node

        :param n: order of the node
        :return: left child node
        """
        if n * 2 <= self.size():
            return self.heap[n * 2]

    def get_right_child(self, n: int) -> Optional[int]:
        """
        get the right child node of nth order node

        :param n: order of the node
        :return: right child node
        """
        if n * 2 + 1 <= self.size():
            return self.heap[n * 2 + 1]

    def get_parent(self, n: int) -> int:
        """
        get the parent node of nth order node

        :param n: order of the node
        :return: parent node
        """
        return self.heap[n // 2]

    def get_element(self) -> list[int]:
        """
        return all elements of this heap except the 0 indexed element

        :return: list of the node
        """
        return self.heap[1:]

    def insert(self, key: int) -> None:
        """
        insert the key into the heap's appropriate location

        :param key: key of the node will be inserted
        :return: None
        """
        # 0. insert the key into the last element
        self.heap.append(key)
        # 1. declare a variable 'idx' for traversing the heap
        idx = self.size()
        # 2. up-heap till...
        #    - the index be the root's
        #    - the key is larger or same with its parent's key
        while idx != 1 and key > self.get_parent(idx):
            self.heap[idx] = self.get_parent(idx)
            idx = idx // 2

        self.heap[idx] = key

    def delete(self) -> Optional[int]:
        """
        delete the root and re-arrange the heap's elements

        :return: the root of the heap
        """
        parent = 1
        child = 2

        if not self.is_empty():
            heap_root = self.heap[parent]
            heap_last = self.heap[self.size()]

            while child <= self.size():
                if child < self.size() and self.get_left_child(parent) < self.get_right_child(parent):
                    child += 1
                if heap_last >= self.heap[child]:
                    break
                self.heap[parent] = self.heap[child]
                parent = child
                child *= 2

            self.heap[parent] = heap_last
            self.heap.pop(-1)

            return heap_root

