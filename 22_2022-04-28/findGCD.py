class Solution(object):
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def findGCD(self, nums):
        minimum = min(nums)

        maximum = max(nums)

        return self.gcd(minimum, maximum)

