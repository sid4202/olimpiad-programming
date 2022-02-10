class Solution(object):
    def __init__(self):
        self.cache = {}

    def fill_cache(self, i, cost):
        if i <= 1:
            return 0
        if i not in self.cache:
            self.cache[i] = min(cost[i - 1] + self.fill_cache(i - 1, cost), cost[i - 2] + self.fill_cache(i - 2, cost))
            return self.cache[i]

    def minCostClimbingStairs(self, cost):
        return self.fill_cache(len(cost), cost)
