class Solution(object):
    def isAnagram(self, s, t):
        stack = list(s)
        for c in t:
            if c in stack:
                stack.pop(stack.index(c))

        if stack == []:
            return True
        else:
            return False
