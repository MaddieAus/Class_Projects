# Madison Austin
# CSCI 136 5/2/25
# QueueOfPositions

class QueueOfPositions:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue underflow")
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)
