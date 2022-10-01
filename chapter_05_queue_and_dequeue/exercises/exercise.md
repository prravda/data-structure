# 5.1
- 1

---

# 5.2
- 40, 50

---

# 5.3
- queue 의 크기가 고정된다는 제약 조건이 존재한다.

---

# 5.4
- 7
  - `MAX_QSIZE` 가 12이고, front 가 rear 보다 큰 상황이다.
  - 이 경우, 
    - `front + 1` index 부터 `MAX_QSIZE - 1` index 까지
    - `0` index 부터 `rear` index 까지가 element 가 들어있는 상황이라고 할수 있다.
  - 따라서, `((12 - 1) - (7 + 1) + 1) + (2 + 1)` 개, 7개의 element 가 현재 circular queue 에 들어있다고 할 수 있다.

---

# 5.5
- 2
  - `MAX_QSIZE` 가 8이고, front 가 rear 보다 작은 상황이다.
    - 이 경우,
      - `front + 1` index 부터 `rear` index 까지가 element 가 들어있는 상황이라고 할 수 있다.
    - 따라서, `5 - (3 + 1) + 1` 개의 element, 2개의 element 가 현재 circular queue 에 들어있다고 할 수 있다.

---

# 5.6
- 3
  - 다른 구현 기준으론 달라질 수 있겠지만, `front` 를 비어있는 공간으로 간주하는 해당 구현을 기준으로 한다면 front == rear 라고 할 수 있다.

---

# 5.7
- 4
  - `front == (rear + 1) % MAX_QSIZE` 를 통해 circular queue 의 포화상태 여부를 확인할 수 있다.

---

# 5.8
- A 추가
  - `[_, B, C, A, _]`
  - `front`: 0, `rear`: 3
- D 추가
  - `[_, B, C, A, D]`
  - `front`: 0, `rear`: 4
- 삭제
  - `[_, _, C, A, D]`
  - `front`: 1, `rear`: 4
  - return value: B
- E 추가
  - `[E, _, C, A, D]`
  - `front`: 1, `rear`: 0
- 삭제
  - `[E, _, _, A, D]`
  - `front`: 2, `rear`: 0
  - return value: C

---

# 5.9
- (1)
  - `[_, 1, _, _, _]`
  - `front`: 0, `rear`: 1
- (2)
  - `[_, 1, 2, _, _]`
  - `front`: 0, `rear`: 2
- (3)
  - `[_, 1, 2, 3, _]`
  - `front`: 0, `rear`: 3
- (4)
  - `[_, _, 2, 3, _]`
  - `front`: 1, `rear`: 3
  - return value: 1
- (5)
  - `[_, _, 2, 3, 4]`
  - `front`: 1, `rear`: 4

---

# 5.10
- 1, 3

---

# 5.11
- 4, 6

---

# 5.12
- 3, 7

---

# 5.13
```python
def front_to_clockwise(front: int, queue_limit: int) -> int:
    return (front + 1) % queue_limit

def front_to_counter_clockwise(front: int, queue_limit: int) -> int:
    return (front - 1 + queue_limit) % queue_limit
```

# 5.14
- 1

---

# 5.15
- `[3, 6, 9, 12, 15, 18]`
- `[_, _, _, _, 15, 18]`
  - `for i in range(20):`의 경우, i 는 0 이상 20 미만의 범위를 나타내기에 i % 4 == 0 인 경우는 4, 8, 12, 그리고 16, 총 4번만 이뤄진다.

---

# 5.16
- `[4]`
- `[4, 8]`
- `[4, 8, 9]`
- `[5, 4, 8, 9]`
- `[5, 4, 8, 9]` 
  - getRear() 는 dequeue 의 element 에 영향을 주지 않음
- `[4, 8, 9]`
- `[4, 8]`
- `[7, 4, 8]`
- `[7, 4, 8]`
  - getFront() 는 dequeue 의 element 에 영향을 주지 않음
- `[7, 4, 8, 6]`
- `[4, 8, 6]`
- `[8, 6]`

---

# 5.17
```python
while not D.is_empty():
    Q.enqueue(D.delete_rear())

while not Q.is_empty():
    D.add_front(Q.dequeue())
```

---

# 5.18
```python
while not D.is_empty():
  S.append(D.delete_front())

while not S.is_empty():
  D.add_front(S.pop())
```

---

# 5.19
- integer type 의 element 가 곧 priority 인 해당 교재의 구현 방식으로 구현된 priority queue 라는 가정 하에,
  - `55, 39, 28, 23, 14` 순으로 출력된다.

---

# 5.20
- lineal data structure 의 정의는
  - index 를 통해 sequential 하게 정렬되어야 한다
  - index 를 통해 접근이 가능해야 한다
  이다.
- 그러나, priority queue 는 index 와는 별도의 priority 가 근간이 되기에, lineal data structure 라고 할 수 없다.
