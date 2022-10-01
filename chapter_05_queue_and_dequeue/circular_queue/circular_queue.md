# Circular queue

# Queue

## Description

- `Queue` 는 삽입과 삭제가 분리 되어있음
    - 삽입은 `rear`, 삭제는 `front` 에서 처리한다
    - stack 이 `rear` 에서 삽입 / 삭제를 모두 처리하는 것과 다르다

## ADT

```python
class Queue:
	def __init__(self):
		self.storage = []

	def enqueue(self, x):
		self.storage.append(x)
	
	def dequeue(self, x):
		self.storage.pop(0)
	
	def peek(self):
		return self.storage[-1]

	def size(self):
		return len(self.storage)

	def clear():
		self.storage = []
```

## Queue in the real world

- 프린터와 컴퓨터 사이의 인쇄 작업 큐 (버퍼링)
- 비디오 스트리밍의 버퍼링
- Kafka 같은 MQ

---

# Lineal Queue

## Queue’s methods

- `enqueue()`: O(1)
    - 맨 뒤에  element 를 입력하는 것이기 때문에 해당 time complexity 가 나온다.
        - 물론 dynamic size array 의 경우 size / memory re-allocation 에 의해 almost `O(1)` 이라는 점.
- `dequeue()`: O(n)
    - 해당 행위는 0th index 의 element 를 제거하는 것인데, 가장 앞의 element 를 제거하고, 나머지 element 를 `index -—` 과정을 통해 재배치하기에 n-1 번의 연산, time complexity 가 O(n) 이 된다.

## Cons of (lineal) queue

- 위에 말 했듯 `dequeue` 과정에서 후단(`rear`)이 아닌 전단(`rear`)에서 element 를 제거하기 때문에, element re-allocation 과정으로 인하여 `O(n)` 만큼의 연산이 일어난다.

---

# Circular Queue as An Alternative

- 원형 큐(`circular queue`) 를 이용하면 [위에서 이야기하였던](https://www.notion.so/Chapter-05-Queue-and-Deque-dc5c0fa288a141f8a1ea9e95c54e2564) 문제를 해결할 수 있다, 단 trade-off 이지만.
    - constraint 는 바로 queue 의 size 가 고정되어야 한다는 것이다.
- 이해하는 데 사용한 추가적인 [reference](https://www.geeksforgeeks.org/circular-queue-set-1-introduction-array-implementation/) 또한 첨부해본다.

## Key points of circular queue

![how circular queue works, geeksforgeeks](./assets/0-example-of-circular-queue.png)

how circular queue works, geeksforgeeks

- 해당 자료구조의 핵심은 `rear` 와 `front` 를 표기하는 index 가 움직인다는 것이다.
- 그렇게 index 관리를 해 준다면, 일반적인 queue 의 경우 enqueue 를 했을 때 re-allocation 과정을 거쳐 `O(n)` 의 연산이 발생하는 것과 달리, `O(1)` 의 연산으로 enqueue 작업을 마무리 할 수 있다.

## Example of circular queue - python3

```python
# Custom error using for overflow
class OverFlowException(Exception):
    def __str__(self) -> str:
        return "circular_queue is full"

# Custom error using for underflow
class UnderFlowException(Exception):
    def __str__(self) -> str:
        return "circular_queue is empty"
```

```python
class CircularQueue:
    def __init__(self, size: int = 8):
        self.__limit = size
        self.__storage = [None for _ in range(self.__limit)]
        self.__front = 0
        self.__rear = 0

    def __str__(self) -> str:
        self.display()
        return f"circular_queue: {self.__storage}\nfront: {self.__front}\nrear: {self.__rear}\nlength: {self.get_size()}\n\n"

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
        # check whether the circular_queue is full or not
        if self.is_full():
            raise OverFlowException()

        # manage index - rear
        self.__rear = (self.__rear + 1) % self.__limit
        self.__storage[self.__rear] = element

    def dequeue(self):
        # check whether the circular_queue is empty
        if self.is_empty():
            raise UnderFlowException()

        # manage index - front
        self.__front = (self.__front + 1) % self.__limit

        # assign an variable
        # and save the circular_queue's updated self.__front's element
        temp = self.__storage[self.__front]

        # and re-assign the element by location with None
        self.__storage[self.__front] = None

        # return the variable before stored
        return temp

    def peek(self):
        # return front-most element
        # because it is a circular_queue
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
```

책에서 나온 circular queue 같은 경우, front 는 무조건 비워둔다. 그래서 queue 의 size 가 8인 경우, 실질적으로 담을 수 있는 element 의 갯수는 7개라는 이야기이다. 

## Key points of circular queue

- index management
    - front / rear 의 index 가 시계방향으로 도는 걸 처리하는 경우이다.
- order
    - index management → element management 순서대로 진행한다.

## What is happened?

### enqueue

- queue 가 포화(full) 상태면 enqueue 를 할 수 없으니, `is_full()` method 를 이용하여 queue 의 포화상태를 검사한다.
    - 포화상태인 경우 포화상태라 해당 작업이 불가능하다는 에러를 `raise` 한다.
    - 포화상태가 아닌 경우, 하술할 작업들을 순서대로 진행한다.
- rear 위치에 element 를 삽입하는 과정이니, 현재 rear 가 아닌 다음 rear 로 rear 를 조정해준다.
    - 그러나, rear 가 계속 더해져서 out of index (overflow) 가 나는 경우를 방지하기 위해, `limit` 을 이용한 modulo calculation (나머지 연산)으로 index 를 특정 범위 내에서 순회하도록 처리해준다.
- 그 다음, 그렇게 변경된 rear 의 값을 rear 에 재 할당 해준다.
- 그리고, 그 변경된 rear 의 index 에 enqueue 하고자 하는 element 를 넣는다 (index 를 통해 접근하기 때문에, time complexity 는 `O(1)` 이다)

코드로 보면 다음과 같다. 

```python
def enqueue(self, element):
        # check whether the circular_queue is full or not
        if self.is_full():
            raise OverFlowException()

        # manage index - rear
        self.__rear = (self.__rear + 1) % self.__limit
        self.__storage[self.__rear] = element
```

`self.__rear = (self.__rear + 1) % self.__limit` 작업은 만약 `limit` 이 8이라 가장 마지막 index 가 7인데 rear + 1 이 8이 나오는 경우, `% limit` 을 통해서 0부터 다시 시작하게끔 만들어준다는 의미이다. 

### is_full

queue 의 포화 상태를 먼저 자연언어로 정의한다면 

- 위의 다음 rear 로 접근하는 연산을 진행한다
- 해당 rear 가 front 와 같아진다

이다. 

즉, 비어있는 상태로 유지시켜야 하는 front 까지도 채워버리는 경우라고 정의할 수 있다. 

코드로 정의하면 

```python
def is_full(self) -> bool:
    return self.__front == (self.__rear + 1) % self.__limit
```

다음과 같이 현재 queue 가 포화상태인지의 여부를 확인하고, 반환할 수 있다. 

### dequeue

- queue 구조는 FIFO 이기에, front 에 있는 element 가 먼저 빠져나가는 방식이다.
- 그러나 manipulation 이전의 front 는 현재 비어있는 곳을 가리키고 있다.
- 그래서
    - front index manipulation 을 진행한다
    - 변수 하나를 선언한다
        - 해당 변수에 새로운 front index 에 있는 element 를 할당한다
    - 새로운 front index 에 있던 변수를 삭제해준다
        - 삭제라는 행위는 상황에 따라 달라질 수 있다.
            - `delete` 를 사용할 수도 있다.
            - `None` 으로 비어있는 공간을 표기하는 경우, `None` 을 재 할당 할 수도 있다.
    
    와 같은 과정을 진행하여 dequeue 를 수행할 수 있을 것이다. 
    
- front index manipulation 또한 rear index manipulation 과 같은 방식으로 진행한다.
    - out of index 가 나는 상황을 방지하기 위해서, modulo 연산을 사용해준다.
    - 코드로 보면, `self.__front = (self.__front + 1) % self.__limit`

코드로 정리하면, 다음과 같다.

```python
def dequeue(self):
        # check whether the circular_queue is empty
        if self.is_empty():
            raise UnderFlowException()

        # manage index - front
        self.__front = (self.__front + 1) % self.__limit

        # assign an variable
        # and save the circular_queue's updated self.__front's element
        temp = self.__storage[self.__front]

        # and re-assign the element by location with None
        self.__storage[self.__front] = None

        # return the variable before stored
        return temp
```

### is_empty

- queue 가 비어있다는 상황에 대한 정의를 자연어로 하자면, “front 와 rear 가 같은 상황” 이라고 할 수 있다.
    - 왜냐면, 계속해서 front 에 있던 element 를 반환하고, 제거하면서 front 를 조작하다가 rear (queue 의 element 가 담긴 가장 마지막 index) 까지 갔다는 건, element 가 담긴 index 마저도 비어있단 뜻이기 때문이다.

코드로 정의하자면 다음과 같다. 

```python
def is_empty(self) -> bool:
    return self.__front == self.__rear
```

### display

- front 부터 rear 까지를 출력하면 되지만, 여기서 고려해야 할 점은 해당 circular queue 의 index management 방식이다.
    - 그래서, front 가 rear 보다 더 큰 (위치로 치면, 더 뒤에 위치하는) 현상이 발생할 수 있다.
    - 머릿속에서 떠오르는 일반적인 상황이라면 front 는 rear 보다 앞에 있어야 한다, 예시를 들자면
        - `[ X, X, front, O, O, rear ]` 와 같다
    - 그러나 위에 말한 상황의 예시를 들자면,
        - `[ O, O, rear, X, X, front ]` 와 같다
- 그래서 경우의 수를 두 개로 나누어서 출력해주어야 한다.
    - `front > rear` 인 경우
    - 그렇지 않은 경우
- front > rear 인 경우
    - `front + 1` 부터 배열의 끝까지 + 배열의 처음부터 `rear` 까지 를 합쳐서 출력해 주어야 한다.
        - `front + 1` 을 한 경우는, front 는 비어있는 공간이기 때문이다.
    - 코드로 나타내자면, `return self.__storage[self.__front + 1:] + self.__storage[:self.__rear + 1]` 이다.
        - 여기서 배열의 처음부터 rear 까지를 나타내는 배열을 표기할 때 `self.__storage[:self.__rear + 1]` 라고 나타낸 이유는, python 의 list slicing 을 표기하는 `list[n:m]` 의 경우 list 의 `n`번째 index 부터 `m - 1` 번째 index 까지 를 반환하기 때문이다.
- front < rear 인 경우 (즉, 위의 경우가 아닌 경우)
    - `front + 1` 부터 `rear` 까지 를 반환한다.
    - 코드로 나타내자면, `return self.__storage[front + 1 : rear + 1]` 이다.

이 두 개를 합친 display method 의 python 코드는 다음과 같다.

```python
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
```

이렇게 cyclic queue 를 만들어 보았다. 장점은 enqueue, dequeue 과정의 time complexity 가 전부 `O(1)` 이라는 점이지만, 단점은 queue 의 size 가 한정되어 있다는 점이다. `no silver bullet`