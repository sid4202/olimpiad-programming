class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) == 0:
            return None

        return self.stack.pop()

    def top(self):
        if len(self.stack) == 0:
            return None
        
        return self.stack[-1]

    def size(self):
        return len(self.stack)


class Solution(object):
    def validateStackSequences(self, pushed, popped):
        stack = Stack()
        i = 0
        j = 0
        while i < len(pushed):
            stack.push(pushed[i])
            while j < len(popped) and stack.top() == popped[j]:
                stack.pop()
                j += 1
            i += 1

        return len(stack.stack) == 0
