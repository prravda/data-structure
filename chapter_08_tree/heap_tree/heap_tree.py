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
        # 0. insert the data at the last of heap
        self.heap.append(data)
        
        # 1. rebalancing - using up-heap till fulfill the condition of heap
        # 1-1. get the index of the last node
        i = self.size()

        # 1-2. up-heap till the data is larger than it's current parent
        while i != 1 and data > self.get_parent(i):
            # 1-3. update the i'th value 
            self.heap[i] = self.get_parent(i)
