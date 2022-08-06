from collections import deque


########################
# deque data structure
class deque_:
    def __init__(self):
        self.deq = deque()

    def add(self, val):
        self.deq.appendleft(val)

    def pop(self):
        return self.deq.pop()

    def size(self):
        return len(self.deq)
