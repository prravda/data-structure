from typing import Optional


class Node:
    def __init__(self, elem: Optional[int] = None, link: Optional["Node"] = None):
        self.data = elem
        self.link = link
