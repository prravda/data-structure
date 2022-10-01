# Dequeue
## Description
- `Dequeue`, 덱이라고 읽는 해당 자료구조는 `Double-ended` + `Queue` 의 약어로, 양쪽을 다 사용할 수 있는 형태의 queue 라고 할 수 있다.
  - 즉, 이름처럼 `front`, `rear` 양쪽에서 `append` 와 `pop` 이 가능하다는 이야기이다.
- 그래서 해당 수업에서는 dequeue 를 구현할 때, 이전에 만들었던 circular queue 를 기반으로 구현한다.

## Abstract data type
### In natural langauge
- FIFO 형태의 data type 인 queue 에
  - front 에 append
  - rear 에 pop
  
  이 추가적으로 가능해야 한다.
### In code
```python
class CircularDequeue(CircularQueue):
    def __init__(self, size):
        super().__init__(size)
    #...skip the redundant parts
    
    # add an element to front side
    def add_front(self, element: Any) -> None:
    
    # remove element from rear side
    def delete_rear(self):
```

## Implementation /w Python
### Before getting started
- 유의할 점이 있다면, (circular)queue 와 다르게 index 가 반시계방향으로 돌아간다는 점이다. 
  - front, rear 전부!
- 그리고 본래는 비어있던 공간인 front 에 할당을 하는 작업이다 보니, queue 와는 달리 
  - index manipulation
  - assignment into storage
  
  순의 과정을 거치게 된다.

### Code
```python
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
```

### Code description
```python
self._front = (self._front + 1) % self._limit 
```
- 시계방향으로 돌았을 때의 index 를 관리하는 코드는 이런 식이었다. 
- index 를 1씩 움직여 주는데, 그게 limit 을 넘어가는 경우를 handling 하기 위해서 modulo 연산으로 처리를 해 주었다.

```python
self._front = (self._front - 1 + self._limit) % self._limit
```
- 반면, 반시계방향으로 도는 index 를 관리하는 코드는 다음과 같다.
- index 를 -1 씩 움직여 주는데, 그게 underflow 가 날 수도 있으니 `limit` 을 더하고, 그 값에 modulo 연산으로 처리를 해 주었다.
```python
def add_front(self, element: Any) -> None:
    # before add an element, 
    # check whether the queue is full or not
    if self.is_full():
        raise OverFlowException
    # assign a element to this updated index
    self._storage[self._front] = element
    # index management
    self._front = (self._front - 1 + self._limit) % self._limit
```
- `add_front` 의 처리 방식, 그 중에서 순서 또한 circular queue 와 다르다.
  - 왜냐면, circular queue 같은 경우 `add_rear` 를 하는 경우엔 그 다음 rear 에 채워주어야 하기에 index 를 먼저 움직여 주어야 했다.
  - 그러나, circular dequeue 은 `add_front` 를 하는 경우 `front` 라는 index 가 이미 비어있는 index 이기 때문에
    - element 를 먼저 해당 index 에 할당
    - index 를 반시계 방향으로 조정
    
    의 순서, 즉, queue 의 순서와 반대가 된 것이다.
```python
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
```
- `delete_rear` 의 처리방식도 위와 같은 이유로 circular queue 의 순서와 반대가 된다.