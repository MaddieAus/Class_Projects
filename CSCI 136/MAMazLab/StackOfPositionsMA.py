# Madison Austin
# CSCI 136 5/2/25
# QueueOfPositions

class StackOfPositions:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack underflow")
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack underflow")
        return self.stack[-1]

    def size(self):
        return len(self.stack)
