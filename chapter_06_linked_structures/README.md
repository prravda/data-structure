# Linked data structure

---

## Description
### Before comparing with array
- `array` 의 특징을 다시 한 번 되돌아보자
  - 연속된 메모리 공간에 존재한다.
  - `index` 를 통해 원하는 element 에 `O(1)` time complexity 로 접근이 가능하다.
  - element 를 담을 수 있는 `size` 는 한정되어 있다.
### Linked structure
- `linked structure`, 즉 연결된 자료형은 array 와는 다르다.
  - 먼저, 메모리의 연속된 공간에 존재한다는 보장이 존재하지 않는다.
  - 그리고, 원하는 element 에 index 를 통해 바로 접근할 수 없으며, 해당 연산엔 `O(n)` 만큼의 time complexity 가 필요하다.
    - 왜냐면, `(data, link)-(data-link)...` 형식으로 연결된 구조이기 때문에 link 를 통해서 순차적으로 다음 node(element) 에 접근해야 하기 때문이다.
  - 계속해서 node 를 이어나가면 되기 때문에 `size` 로 부터 자유롭고, 필요에 따라 그 크기를 동적으로 늘리고 줄일 수 있다.
```python
from typing import Optional, Any


class Node:
    def __init__(self, elem: Optional[int] = None, link: Optional["Node"] = None):
        self.data: Any = elem
        self.link: Node = link
```
- linked structure 의 구성에 사용할 `Node` 를 구현하자면 이렇게 할 수 있을 것이다. 

