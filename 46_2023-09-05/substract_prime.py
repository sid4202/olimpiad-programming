import math


class Solution:
    def is_prime(self, n):
        for i in range(2, int(math.sqrt(n))):
            if n % i == 0:
                return False

        return True

    def is_sorted(self, arr):
        if len(arr) == 0 or len(arr) == 1:
            return True

        for i in range(1, len(arr)):

            if arr[i - 1] > arr[i]:
                return False

        return True

    def primeSubOperation(self, nums):  # -> bool:
        if self.is_sorted(nums):
            return True

        for i in range(len(nums) - 2, 0, -1):
            print(nums)
            diff = abs(nums[i + 1] - nums[i])
            if self.is_prime(diff):
                nums[i] -= diff
            else:
                while not self.is_prime(diff) and diff > 0:
                    diff -= 1

            if nums[i] - diff <= 0:
                return False

        print(nums)
        return True


sol = Solution()

print(sol.primeSubOperation([5, 8, 3]))
