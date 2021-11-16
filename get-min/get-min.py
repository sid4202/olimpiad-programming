class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val):
        if self.min is None:
            self.min = val
        elif val < self.min:
            self.min = val
        self.stack.append(val)

    def pop(self):
        if len(self.stack) == 0:
            return None

        self.stack.pop()

        if len(self.stack) != 0:
            self.min = min(self.stack)
        else:
            self.min = None

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min


minStack = MinStack()
minStack.push(-2)
print(minStack.stack)
minStack.push(0)
print(minStack.stack)
minStack.push(-3)
print(minStack.stack)
res = minStack.getMin()
print(res)
minStack.pop()
print(minStack.stack)
minStack.top()
minStack.getMin()

