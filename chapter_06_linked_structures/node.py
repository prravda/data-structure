from typing import Optional, Any


class Node:
    def __init__(self, data: int, link: Optional["Node"] = None):
        self.data: int = data
        self.link: Optional["Node"] = link
