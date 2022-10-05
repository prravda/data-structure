from typing import Optional, Any


class Node:
    def __init__(self, elem: Optional[int] = None, link: Optional["Node"] = None):
        self.data: Any = elem
        self.link: Optional["Node"] = link
