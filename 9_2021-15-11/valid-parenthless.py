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
        return self.stack[-1]

    def size(self):
        return len(self.stack)


def string_check(s):
    brackets = {
        "(": ")",
        "[": ']',
        '{': '}'
    }
    opened = Stack()
    for c in s:
        if c in brackets:
            opened.push(c)
        else:

            top_bracket = opened.pop()
            if not top_bracket or brackets[top_bracket] != c:
                return False
    return opened.size() == 0


s = input()
print(string_check(s))
