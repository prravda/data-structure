# List /w linked structure - LinkedList

- 이제 `top` 부분에서만 push / pop 을 통해 element manipulation 이 가능한 stack 이 아닌, n’th element 에 접근 / 삽입 / 삭제 가 가능한 list 를 linked structure 로 만들어보자.

# Define ADT(Abstract Data Type)

- 위에 적은 기능들을 더 명확하게 적어보자면 다음과 같다

```python
class LinkedList:
	# ...
	def get_node(self, position: int) -> Optional[Node]:
		# return the node at position'th element
	
	def get_entry(self, position: int) -> Optional[Any]:
		# return the data of the node at position'th element

	def replace(self, position: int, data: Any) -> None:
		# replace the data of the node at position'th element
		# into 'data' argument

	def find(self, value_to_find: Any) -> Optional[Node]:
		# find a node which contains value_to_find argument
		# as a data of the node

	def insert(self, position: int, data: Any) -> None:
		# insert a node with data into position'th element

	def delete(self, position: int) -> Optional[Node]:
		# delete the position'th node
```

## Detailed description

- 일반적인 array structure 와는 다르게, linked list 에서는 node 를 통해 element 를 접근/탐색/관리 한다.
    - 그래서, argument 로 들어오는 `position` ’th node 를 찾기 위한 `get_node` 등의 method 가 필요한데, 상술 하였듯 index 를 통해 접근하는 방식이 아닌, 원하는 node 를 찾을 때까지 연결된 node 들을 link 를 통해 순회하여야 하기 때문에 time complexity 는 `O(n)` 이 된다.

# Method implementation

```python
from typing import Optional, Any
from chapter_06_linked_structures.node import Node

class LinkedList:
    def __init__(self):
        self.__head: Optional[Node] = None

    # basic methods definition
    def is_empty(self):
        return self.__head is None

    def clear(self):
        self.__head = None

    def size(self) -> int:
        size_of_list = 0
        current_node = self.__head

        while current_node is not None:
            size_of_list += 1
            current_node = current_node.link

        return size_of_list

    def display(self):
        container = []
        current_node = self.__head

        while current_node is not None:
            container.append(current_node.data)
            current_node = current_node.link

    # linkedlist-specific methods definition
    def get_node(self, position: int) -> Optional[Node]:
        if position < 0:
            return None

        counter = position
        current_node = self.__head

        # using while loop with two condition
        # - counter is larger than 0
        # - current_node is not None
        # for cover this case:
        #   if position is larger than the back-most node's
        #   stop the counting
        while counter > 0 and current_node is not None:
            counter -= 1
            current_node = current_node.link

        return current_node

    def get_entry(self, position: int) -> Any:
        node = self.get_node(position)

        if not node:
            return None
        return node.data

    def replace(self, position: int, data: Any) -> None:
        target = self.get_node(position)
        target.data = data

    def find(self, value_to_find: int):
        current_node = self.__head

        while current_node is not None:
            if current_node.data == value_to_find:
                return current_node

        return None

    def insert(self, position: int, data: Any) -> None:
        node_before_insert = self.get_node(position - 1)

        # if there is no node in position 'th index
        # insert this node at front most
        if node_before_insert is None:
            self.__head = Node(data, self.__head)

        else:
            # if there is node
            # - make a node with data argument
            #   and a link of node_before_insert
            node_to_insert = Node(data, node_before_insert.link)
            # after do this, assign #1
            # into the node_before_insert.link
            node_before_insert.link = node_to_insert

    def delete(self, position: int) -> None:
        node_before_deletion = self.get_node(position - 1)

        if node_before_deletion is None:
            if self.__head is not None:
                self.__head = self.__head.link

        elif node_before_deletion.link is not None:
            node_before_deletion.link = node_before_deletion.link.link

    # practice 6.2
    # implement merge
    # update itself
    def merge(self, another_linked_list: 'LinkedList') -> None:
        current_size = self.size()
        current_size_another_list = another_linked_list.size()

        while not another_linked_list.is_empty():
            current_node_from_another = another_linked_list.get_node(0)
            self.insert(current_size, current_node_from_another.data)
            current_size += 1

            another_linked_list.delete(current_size_another_list)
            current_size_another_list -= 1

# test
def test_linked_list_insertion():
    linked_list = LinkedList()
    index_to_allocate = 0
    data_to_allocate = 10
    linked_list.insert(index_to_allocate, data_to_allocate)

    linked_list.get_entry(index_to_allocate) == data_to_allocate

def test_linked_list_deletion():
    linked_list = LinkedList()
    number_of_allocation = 5
    for i in range(0, number_of_allocation):
        linked_list.insert(i, i)

    linked_list.delete(number_of_allocation - 1)

    linked_list.size() != number_of_allocation

def test_linked_list_replacement():
    linked_list = LinkedList()
    index_to_allocate = 0
    number_to_allocate = 10
    number_to_re_allocate = 20

    linked_list.insert(index_to_allocate, number_to_allocate)
    linked_list.replace(index_to_allocate, number_to_re_allocate)

    assert linked_list.get_entry(index_to_allocate) != number_to_allocate

def test_linked_list_merge():
    # create a list
    linked_list = LinkedList()
    number_of_insertion = 3

    for i in range(number_of_insertion):
        linked_list.insert(i, i)

    size_before_merge = linked_list.size()

    # create list which will be merged into #1
    linked_list_to_merge = LinkedList()

    for i in range(number_of_insertion):
        linked_list_to_merge.insert(i, i+1)

    # merge
    linked_list.merge(linked_list_to_merge)

    size_after_merge = linked_list.size()

    # compare the size of list before and after merging
    assert size_before_merge != size_after_merge
```

## get_node

```python
def get_node(self, position: int) -> Optional[Node]:
		if position < 0:
		    return None
		
		counter = position
		current_node = self.__head
		
		# using while loop with two condition
		# - counter is larger than 0
		# - current_node is not None
		# for cover this case:
		#   if position is larger than the back-most node's
		#   stop the counting
		while counter > 0 and current_node is not None:
		    counter -= 1
		    current_node = current_node.link
		
		return current_node
```

### Description

- 먼저, 0보다 작은 index 가 들어올 수 있기에 이 경우를 cover 하기 위하여 가장 위에 `if position < 0` 이라는 조건을 걸었고, 해당 경우를 만족하는 경우 탐색을 진행하는 게 아닌 `None` 을 반환하도록 처리하였다.
- `position` 번째에 있는 node 를 구하는 `get_node` method 를 구현하였다.
    - 탐색하고자 하는 위치인 position 이 out of range 인 경우를 대비하여, while loop 에 `current_node is not None` 이라는 조건을 추가하였다.
    - 그리고, position 만큼의 이동을 확인하기 위해 해당 값을 `counter` 라는 variable 을 선언 후 할당하고, 그 값을 decrement 하다가 0 이하가 되면 멈출 수 있게 `counter > 0` 이라는 조건을 추가하였다.

### Time complexity

- time complexity 는 결국 존재하는 node 를 다 순회하는 과정을 거쳐야 하기 때문에, `O(n)` 이다.

## insert

```python
def insert(self, position: int, data: Any) -> None:
      node_before_insert = self.get_node(position - 1)

      # if there is no node in position 'th index
      # insert this node at front most
      if node_before_insert is None:
          self.__head = Node(data, self.__head)

      else:
          # if there is node
          # - make a node with data argument
          #   and a link of node_before_insert
          node_to_insert = Node(data, node_before_insert.link)
          # after do this, assign #1
          # into the node_before_insert.link
          node_before_insert.link = node_to_insert
```

### Description

- `position` 번째 위치에 `data` 를 값으로 하는 node 를 생성하는 method 이다.
- 기본적으로 position 번째 위치에 삽입을 하는 과정을 거쳐야 하기 때문에 `position - 1` 번째 node 에 먼저 접근을 해야 한다.
    - 그래서 이 과정에서 방금 구현했던 `get_node` 를 사용하고, argument 로 `position - 1` 을 넣어준다.
- `node_before_insert` 라는 변수를 선언 후,  이렇게 찾은, ‘삽입하고자 하는 position 직전의 node’ 를 할당해준다.
    - 만약 `node_before_insert` 가 out of range 등의 issue 로 존재하지 않는 경우(`None`), 그냥 맨 앞에(`head`) 값을 넣어준다.
    - 그러나 해당 값이 잘 존재하는 경우엔
        - 새로운 node 를 만드는데, data 로는 argument 로 받은 data 를, link 로는 `node_before_insert` 의 link, 즉 그 뒤의 node 들의 위치를 담은 link 를 넣어준다.
        - 그리고 그렇게 만든 node 를, `node_before_insert` 의 link 라는 property 에 할당해준다.

### Time complexity

- time complexity 는 결국 `get_node(position - 1)` 이라는 과정에서 O(n) 번 만큼의 연산을 하기에 `O(n)` 이다.

## delete

```python
def delete(self, position) -> None:
		node_before_deletion = self.get_node(position - 1)
		
		if node_before_deletion is None:
		    if self.__head is not None:
		        self.__head = self.__head.link
		
		elif node_before_deletion.link is not None:
		    node_before_deletion.link = node_before_deletion.link.link
```

### Description

- 해당 method 는 다른 자료형(stack, queue)의 삭제 및 반환을 하는 method 가 아니라, 그냥 삭제만 하는 method 이다.
- 마찬가지로, 삭제하고자 하는 position 직전의 node 를 `get_node(position - 1)` 을 통해 찾는다.
- `node_before_deletion` 이라는 변수를 선언,  위의 과정에서 찾은 결과를 할당한다.
    - 만약 해당 값이 존재하지 않으면(`is None`), `self.__head`, 그러니까 가장 마지막에 위치한 node 또한 존재하는지 존재하지 않는지를 `self.__head is not None` 으로 확인한다.
        - 존재한다면, `self.__head = self.__head.link` 와 같이 가장 마지막에 위치한 node 를 제거해준다.
    - 해당 값이 존재한다면, 삭제하고자 하는 node 또한 존재하는지 (`is not None`) 를 `node_before_deletion.link` 를 통해 검사해준다.
        - 삭제하고자 하는 node 가 존재한다면, 위의 head 에서 진행한 것과 비슷하게 `node_before_deletion.link = node_before_deletion.link.link` 로 처리하여 삭제하고자 하는 node 의 다음 node 주소를 삭제하고자 하는 node 이전의 node 의 link 에 할당, 삭제하고자 하는 node 를 삭제해준다.

### time complexity

- time complexity 는 결국 `get_node(position - 1)` 이라는 과정에서 O(n) 번 만큼의 연산을 하기에 `O(n)` 이다.

## merge

```python
def merge(self, another_linked_list: 'LinkedList') -> None:
		current_size = self.size()
		current_size_another_list = another_linked_list.size()
		
		while not another_linked_list.is_empty():
		    current_node_from_another = another_linked_list.get_node(0)
		    self.insert(current_size, current_node_from_another.data)
		    current_size += 1
		
		    another_linked_list.delete(current_size_another_list)
		    current_size_another_list -= 1
```

### Description

- 원래 처음 제시한 ADT 에서 존재하지 않았던 method 이지만, 뒷부분에서 제안해봐서 만들어보게 된 method 이다.
- 해당 method 의 역할은 parameter 로 또 다른 `LinkedList` 가 들어왔을 때, 해당 LinkedList 의 element 들을 기존 LinkedList 에 병합(merge)을 하는 것이다.
- index 가 없는 상황이기에, `size()` method 를 통해 가장 마지막 element 의 위치를 계산하고, 그걸 decrement 하는 방식으로 접근하여 연산을 최대한 줄여보았다.
- size 는 총 두 개가 필요하다.
    - 하나는 원래 linked list 의 size인데, 마지막 element 다음 위치에 삽입을 해야하기 때문이다.
    - 하나는 merge 가 되어지는 (be merged) linked list 의 size 인데, 해당 위치에 접근하여 node 를 가져오고, 가져온 뒤엔 delete 를 해야 하기 때문이다.
- 해야 하는 일을 자연언어 pseudo code 로 정의하자면,
    - 병합하고자 하는 linked list 가 빌 때 까지 아래와 같은 작업을 수행한다.
        - 병합하고자 하는 linked list 의 마지막 element 를 가져온다
        - 해당 element 를 기존 linked list 의 마지막 element 에 삽입한다
        - 병합하고자 하는 linked list 의 마지막 element 를 삭제한다
    
    이다.
    
- 그 코드를 옮긴 것이 `while loop` 과 그 안의 과정들이다.

### Time complexity

- time complexity 는 `O(n^2)` 인데, 왜냐면 while loop 을 도는 와중에 n번 연산이 일어나고, 그 와중에 element traverse 를 하는 `get_node` 가 내부적으로 진행되기 때문에 n번 연산이 일어나기 때문이다.