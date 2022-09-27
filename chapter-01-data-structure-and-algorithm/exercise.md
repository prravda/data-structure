TODO: 1.7 부터 마저 풀기

---

# 1.1
- 1, 2, 4, 5

# 1.2
```python
class Bag:
    def __init__(self):
        self.storage = []
    
    def contains(self, e):
        return e in self.storage
    
    def insert(self, e):
        self.storage.append(e)
        
    def remove(self, e):
        self.storage.remove(e)
        
    def count(self):
        return len(self.storage)

class CountingBag(Bag):        
    def number_of_item(self, item):
        count_of_item = 0
        for i in self.storage:
            if i == item:
                count_of_item += 1
        
        return count_of_item
        
```

# 1.3
- `Time(hours, minutes, seconds)`
  - Time 이라는 ADT 를 만들기 위해서는, `hours`, `minutes`, 그리고 `seconds` 가 필요하다.
- `hours()`, `minutes()`, `seconds()`
  - Time 이라는 data type 의 `hours`, `minutes`, 그리고 `seconds` 를 반환한다.
- `diffSeconds(otherTime: Time)`
  - 다른 Time 을 argument 로 받아 해당 Time 과 다른 Time 의 시차를 계산한다
- `isAm()`, `isPM()`
  - 오후인지 오전인지를 알려준다
- `isSame(otherTime: Time)`
  - 다른 시간과 시/분/초 가 같은지 여부를 검사한다
- `toString()`
  - 시/분/초 등의 정해진 format 의 `string` 으로 Time data type 에 대한 정보를 표현한다.
  
# 1.4
1. `O(n^2)`
2. `O(n^3)`
3. `O(n^3)`
4. `O(2^n)`
5. `O(3^n)`

# 1.5
## Definition of Big O notation
`f(x)` 가 `30*n + 4` 이고 `g(x)` 가 `n`이 라고 할 때, 임의의 n > n0 에 대하여 `|f(x)| <= c*|g(x)|` 를 만족하게 만드는 `c` 와 `n0` 가 존재하면 `f(n) == O(g(n))` 이다.
## Prove
해당 조건을 만족하는 `(C, n0)` 순서쌍인 `(34, 1)` 이 존재하기 때문에, `f(x)` 는 `O(n)` 이다.

# 1.6
- `O(1)`
- `O(logn)`
- `O(n)`
- `O(nlogn)`
- `O(n^2)`
- `O(n^3)`
- `O(2^n)`
- `O(n!)`