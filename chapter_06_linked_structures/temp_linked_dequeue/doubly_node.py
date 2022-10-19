from typing import Optional


class DoublyNode:
  def __init__(
    self,
    data: int,
    prev: Optional['DoublyNode'] = None,
    next: Optional['DoublyNode'] = None,
  ):
    self.data = data
    self.prev = prev
    self.next = next