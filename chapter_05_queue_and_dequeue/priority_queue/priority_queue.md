# Priority Queue
## Description
- queue 구조 중 사실상 가장 일반적인(general) queue 구조이다.
  - 왜냐면, 우선순위를 어떻게 정하느냐에 따라 무엇으로든(stack, queue) 사용이 가능하기 때문이다.
- OS scheduling, Network traffic control 등의 분야에서 사용된다.
  - [OS(CPU) scheduling 을 설명한 문서](https://www.geeksforgeeks.org/cpu-scheduling-in-operating-systems/) 인데, 여기서 나오는 [priority scheduling](https://www.geeksforgeeks.org/cpu-scheduling-in-operating-systems/#ps)이 바로 그것이다.
- 가장 좋은 방법은 `heap tree` 를 이용하는 것이지만, 일단은 이번 장에선 python 에 내장된 list object 를 통해 구현한다.
  - 구현 방법은 아주 간단한데, 입력은 그냥 append method 를 통해서 받되, 반환을 할 땐 loop 을 돌면서 priority 가 높은 element 를 찾는 식이다.
    - 이 경우 n 개의 element 가 priority queue 에 존재한다고 가정할 때, 
    - `pop`(return the highest priority element) 연산은
      - 가장 높은 priority 를 찾는데 n번의 연산
      - 해당 element 를 반환한 뒤, list element re-arrangement 를 하는 데 최대 n-1 번의 연산
      
      총 `2n-1` 번의 연산을 해야 하기 때문에, time complexity 는 `O(n)` 이다.
    - 반면 `append` 는 rear 에 넣어 주기만 하는 것이고, circular queue 구조가 아니라 dynamic 하게 크기를 조정하는 과정이 있기 때문에 `approximately O(1)` 이라고 할 수 있다.
- 여담으로 heap tree 를 통해 구현하는 경우 삽입/삭제 연산은 둘 다 `O(logN)` 으로, 지금의 O(n) 보다 더욱 적은 연산을 하게 만들 수 있다.

## Code
```python
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
```