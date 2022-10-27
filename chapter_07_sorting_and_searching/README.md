# Selection sort

# Definition

- 가장 작은 element 를 ‘선택(`selection`)’ 하여 이동시키는 sorting 이다.

# Strategy

- 정렬된 부분 / 정렬되지 않은 부분을 구분한다.
    - 별도의 list 를 사용하거나, 아니면 같은 list 안에서 index 를 통해 구분하거나, 둘 중 하나의 방식을 사용한다.
    - 여기서는 후자를 사용한다.
- 정렬되지 않은 부분에서 가장 작은 수를 찾은 뒤, 정렬된 부분의 맨 뒤로 이동시킨다.

# Pseudo code

- 0번째 element 부터 n - 1 번째 element 까지 loop 을 돈다
    - `i` 라는 index 를 사용하여 접근하도록 하자.
- 그리고 상술한  loop 안에서 추가로 i 부터 n 번째 element 까지 loop 을 돈다. (이하 inner loop)
    - `j` 라는 index 를 사용하여 접근하도록 하자.
- i 는 정렬이 된 영역의 끝이라고 간주하고, inner loop 에서 찾은 최소값의 element index 와 element swap 을 한다.
    - 그리고 i 라는 값이 increment 하게 늘어나는 만큼 최소값일수록 정렬된 영역의 앞으로 당겨지는 구조이다.

# Time complexity

- N 개의 element 가 있는 경우
    - Outer loop: 0번째에서 N-1 번 → 총 N-1번
    - Inner loop: i번째에서 N번 → 총 N-i 번
    
    연산이 이뤄진다.
    
- Inner loop 의 횟수가 1개씩 줄어들긴 하지만, 절반 등으로 주는 게 아니라 1씩 decremental 하게 감소하는 것이니, time complexity 는 `O(N)` 이라고 할 수 있겠다.

# Code

```python
def selection_sort(unsorted_list: list[int]) -> list[int]:
    # copy the input for preventing the mutation of input
    copied_input = [i for i in unsorted_list]
    length = len(copied_input)

    # outer loop:
    # - iterate elements from 0 to just before of last-most
    # - regard this zone as ordered zone
    for i in range(length - 1):
        # set the i (index) as the ordered zone's last element
        idx_of_min = i
        # inner loop:
        # - iterate elements from i to last-most
        # - regard this zone as unordered zone
        for j in range(i, length):
            # renew the minimum value's index with loop
            if copied_input[j] < copied_input[idx_of_min]:
                idx_of_min = j
        # swap the minimum value's index and ordered zone's last element's index
        copied_input[i], copied_input[idx_of_min] = copied_input[idx_of_min], copied_input[i]

    # return the sorted list
    return copied_input
```

# Testing

```python
from unittest import TestCase
from chapter_07_sorting_and_searching.selection_sort import selection_sort

class TestOfInsertionSort(TestCase):

    def test_selection_sort(self):
        unordered_list = [5, 2, 1, 8, 3, 6]
        sorted_list = selection_sort(unordered_list)

        self.assertEqual(sorted(unordered_list), sorted_list)
```