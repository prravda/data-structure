from typing import Optional, List


class MaxHeap:
    def __init__(self) -> None:
        self.heap = []
        # invalid the 0th index
        self.heap.append(0)

    def size(self) -> int:
        return len(self.heap) - 1

    def is_empty(self) -> bool:
        return self.size() == 0

    def get_parent(self, current_index: int) -> Optional[int]:
        parent_index = current_index // 2
        return self.heap[parent_index]

    def get_left_child(self, current_index: int) -> Optional[int]:
        left_child_index = current_index * 2

        if left_child_index > self.size():
            return None

        return self.heap[left_child_index]

    def get_right_child(self, current_index: int) -> Optional[int]:
        right_child_index = current_index * 2 + 1

        if right_child_index > self.size():
            return None

        return self.heap[right_child_index]

    def display(self) -> List[int]:
        return self.heap[1:]

    def insert(self, data: int) -> None:
        # 0. append data into the last of heap
        self.heap.append(data)

        # 1. create a variable idx to traverse the heap and
        #    init it as the last index of heap
        idx = self.size()

        # 2. run up-heap (because this is max-heap)
        #    till fulfill the (max) heap property
        #    - the index finally be the index of the root node
        #    - the key of the parent node is larger or same with the n
        while idx != 1 and self.get_parent(idx) < data:
            # - assign the parent`s key into current node
            self.heap[idx] = self.get_parent(idx)
            # - then, go up to its parent node
            idx = idx // 2

        # if the up-heap proces is done, assign the data into the
        # appropriate location
        self.heap[idx] = data

    def delete(self):
        parent = 1
        child = 2

        if not self.is_empty():
            heap_root = self.heap[1]
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
