from typing import Optional


class BinarySearchTreeNode:
    def __init__(
            self,
            key: int,
            value: Optional[int] = None,
            left: Optional['BinarySearchTreeNode'] = None,
            right: Optional['BinarySearchTreeNode'] = None,
    ):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
