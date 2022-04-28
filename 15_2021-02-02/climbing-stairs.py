class Solution(object):
    def __init__(self):
        self.stairs = {1:1, 2:2}
    def climbStairs(self, n):
        if n in self.stairs:
            return self.stairs[n]
        if n == 2:
            return 2
        if n == 1:
            return 1
        n_stair = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.stairs[n] = n_stair
        return self.stairs[n]