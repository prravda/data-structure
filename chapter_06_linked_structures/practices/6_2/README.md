# 6.2
## Required data members
- `size`
  - `pop` 이나 `push` 같이 element 의 갯수에 영향을 주는 연산이 일어날 때마다, 해당 data member 를 갱신해야 하기 때문에 필요하다.
## Required method
- `push`
  - 새롭게 생긴 method 는 아니지만, 새로운 element 가 들어온 경우 `size += 1` 을 해 주는 과정이 추가적으로 필요하다.
- `pop`
  - 마찬가지로 새롭게 생긴 method 는 아니지만, `top` 에 위치한 element 가 stack 에서 빠져나가는 경우 `size -= 1` 을 해 주는 과정이 추가적으로 필요하다.