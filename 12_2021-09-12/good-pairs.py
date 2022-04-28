class Solution(object):
    def pair_count(self, n):
        if n == 2:
            return 1
        elif n == 3:
            return 3
        else:
            return (n * (n - 1)) // 2

    def numIdenticalPairs(self, nums):
        keys = list(map(nums.count, nums))
        count_of_elements = {}
        number_of_good_pairs = 0

        for i in range(len(nums)):
            count_of_elements[nums[i]] = keys[i]

        print(count_of_elements)
        for value in count_of_elements.values():

            if value > 1:
                number_of_good_pairs += self.pair_count(value)

        return number_of_good_pairs


arr = [1, 1, 1, 1]
sol1 = Solution()
print(sol1.numIdenticalPairs(arr))
