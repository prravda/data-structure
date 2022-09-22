# Stack ADT
class CustomStack:
    def __init__(self):
        self.stack = []

    def is_empty(self): return len(self.stack) == 0

    def size(self): return len(self.stack)

    def clear(self): self.stack = []


