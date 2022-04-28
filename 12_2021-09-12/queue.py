class Queue:
    def __init__(self):
        self.queue = []

    def front(self):
        return self.queue[-1]

    def back(self):
        return self.queue[0]

    def pop(self):
        self.queue.pop()

    def push(self, element):
        self.queue.append(element)

    def empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
