# summery

# Time complexity

## description

자료구조와 알고리즘에서 흔히 말 하는 `time complexity` 란, time complexity 를 측정하는 방법 중에서도 `Big O Notation` 을 말한다. 

## how to calculate

이 Big O Notation 을 계산하는 방법을 절차적으로 나타내면 아래와 같다

- 어떤 알고리즘이 작업을 완료하기까지 연산 횟수를 구한다
- 연산 횟수의 최고차항을 구한다
    - 최고차항 앞에 상수가 붙어있다면 그 상수를 제한다

## example

예시로 들자면 다음과 같다

```python
def sum_with_recursion(till: int) -> int:
	if till == 1: 
		return 1
	if till > 1: 
		return till + sum_with_recursion(till - 1)
```

재귀(`recursion`) 을 통해서 어떤 숫자(`till`)까지의 합을 구하는 함수인 `sum_with_recursion` 을 정의했다. 만약 till 이 10 이라면, 해당 함수가 호출된 call stack 엔 

```python

call_stack = [ 
	sum_with_recursion(1),
	sum_with_recursion(2),
	sum_with_recursion(3),
	...
	sum_with_recursion(8),
	sum_with_recursion(9),
	sum_with_recursion(10),
]
```

이렇게 10개의 함수가 쌓일 것이며, till 이 n 이라면 n 번만큼 함수가 쌓일 것이다. 

즉 연산을 하는 데 n 번의 연산을 하기에, `O(n)` 이라고 표기할 수 있다. 

## definition of Big O notation

Big O notation 을 도출하는 과정을 기계적인 공식처럼 기술하였으나, 이는 수학적 정의를 통해 도출해 낸 결과물이며 그 정의는 아래와 같다.

```
두 개의 함수 f(n) 과 g(n) 이 주어졌을 때, 모든 n > n0 에 대하여 
|f(n)| <= c*|g(n)| 을 만족하는 상수 c 와 n0 가 존재한다면, 
f(n) == O(g(n)) 이다. 
```

만약 어떤 함수 `f(x)` 가 `3*n^2 + 2*n + 4` 이고, `g(x)` 가 `n^2` 인 경우,  `|f(n)| ≤ c*|g(n)|` 을 만족하는 `(C, n0)` 의 순서쌍이 존재하는가?

- 일단 `(6, 1)` 이라는 순서쌍이 존재한다.
    - 해당 값을 대입하면 f(1) == 6 이고, 6*g(1) == 6 이기에 해당 조건을 만족한다.
- 그러므로, `3*n^2 + 2*n + 4` 는 `O(n^2)` 이라고 말할 수 있다.

그리고 여기서 n 이 매우 커지게 된다면, `f(n) ≤ c*|g(n)|`  이 성립하게 되니, Big(O) 는 해당 함수의 상한을 개략적으로 나타내는 함수라고 볼 수 있다. 

## a list of common Big(O) notation

* log 의 밑(base)은 2이다.

| Big O notation | Eng | Kor |
| --- | --- | --- |
| O(1) | constant | 상수형 |
| O(logn) | logarithmic | 로그형 |
| O(n) | lineal | 선형 |
| O(n*logn) | log-lineal | 선형로그형 |
| O(n^k) | polynomial | N차형 |
| O(k^n) | exponential | 지수형 |
| O(n!) | factorial | 팩토리얼형 |