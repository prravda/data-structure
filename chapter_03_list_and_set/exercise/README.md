# Chapter 3: List and Set

# 3.1. 리스트와 집합의 공통점과 차이점을 설명하여라

## 공통점

- 특정한 목적을 위해 만들어진 자료의 구조이다.

## 차이점

- list 는 중복을 허용하는 반면, set 은 중복을 허용하지 않는다.
- list 는 index 를 통한 access 가 가능하지만, set 은 불가능하다.

---

# 3.2.

공백 상태의 리스트가 있다. 다음 연산을 차례로 수행한 후에 리스트의 내용을 순서대로 적어라

```python
insert(0, 10) # [10]
insert(1, 20) # [10, 20]
insert(0, 30) # [30, 20]
insert(2, 40) # [30, 20, 40]
insert(size(), 50) # [30, 20, 40, 50]
```

---

# 3.3.

앞의 결과에서 다음 연산을 차례로 수행한 후에 리스트의 내용을 순서대로 적어라

```python
insert(1, 60) # [30, 60, 40, 50]
replace(2, 70) # [30, 60, 70, 50]
delete(2) # [30, 60, 50]
```

---

# 3.4.

3.3. 절에서 구현한 리스트는 임의의 위치에 항목의 삽입과 삭제가 가능하다. 우리는 이 리스트의 후단만을 사용해 삽입과 삭제 연산을 하려고 한다. 

이 때, 삭제 연산의 시간 복잡도는 항상 O(1) 이지만, 삽입 연산의 시간 복잡도는 “대부분의 경우” O(1) 이다. 그 이유를 설명하라. 

list 의 size 가 다 차는 경우, 

- list 의 size 를 두 배로 늘린 새로운 list 를 만든다
- 해당 list 에 기존 list 에 존재하던 element 들을 올옮긴다

라는 작업들을 수행해야 한다. 

물론, 여유공간이 생긴 이후의 insertion 은 `O(1)` 이지만, 여유공간이 없는 상황에서는 상술한 reallocation 이 일어나기 때문에 exactly `O(1)` 은 아니다. 

---

# 3.5.

파이썬 리스트 내의 항목들 중에서 가장 큰 항목을 찾아 반환하는 함수를 작성하라.

```python
def find_largest(l: list[int]) -> int:
    largest = 0
    for e in l:
        if e > largest:
            largest = e
    return largest
```

---

# 3.6.

파이썬 리스트 내의 항목들 중에서 가장 작은 항목과 큰 항목을 모두 찾아 한꺼번에 반환하는 함수를 작성하라. 

* 두 값의 반환을 위해 튜플을 사용할 수 있다. 

```python
def find_largest_and_smallest(l: list[int]) -> tuple[int, int]:
    largest = 0
    smallest = 99999

    for e in l:
        if e > largest:
            largest = e
            continue
        if e < smallest:
            smallest = e
            continue

    return largest, smallest
```

---

# 3.7.

두 개의 리스트를 입력 받아 두 리스트에 동일한 항목이 있으면 `True` 를, 없으면 `False` 를 반환하는 함수를 작성하여라.

```python
def find_duplication(list_one: list[int], list_two: list[int]) -> bool:
    for i in list_one:
        for j in list_two:
            if i == j:
                return True
    return False
```

---

# 3.8.

항목이 오름차순으로 정렬된 두 개의 리스트를 받아 하나로 병합하는 함수를 작성하라. 

* 단, 병합된 리스트의 모든 항목도 정렬되어 있어야 한다.

```python
"""
# reference: https://www.geeksforgeeks.org/merge-two-sorted-arrays/
"""
def merge_and_sort(ordered_list_one: list[int], ordered_list_two: list[int]) -> list[int]:
    merged_list = [None for i in range(len(ordered_list_one) + len(ordered_list_two))]

    i = 0
    j = 0
    k = 0

    while i < len(ordered_list_one) and j < len(ordered_list_two):
        if ordered_list_one[i] < ordered_list_two[j]:
            merged_list[k] = ordered_list_one[i]
            k += 1
            i += 1
        else:
            merged_list[k] = ordered_list_two[j]
            k += 1
            j += 1

    while i < len(ordered_list_one):
        merged_list[k] = ordered_list_one[i]
        k += 1
        i += 1

    while j < len(ordered_list_two):
        merged_list[k] = ordered_list_two[j]
        k += 1
        j += 1

    return merged_list
```