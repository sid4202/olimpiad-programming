class Solution(object):
    def numIdenticalPairs(self, nums):
        my_dict = dict()
        for i in nums:
            my_dict[i] = nums.index(i)
        print(my_dict)
        count_of_pairs = 0
        for i in range(len(my_dict)-1):
            print(nums[i]," ",nums[i+1])
            if my_dict[my_dict.keys()[i+1]] - my_dict[my_dict.keys()[i]] != 1:
                count_of_pairs += 1

        return count_of_pairs


arr = [1,2,2,3,3,5,6]
sol = Solution()
print(sol.numIdenticalPairs(arr))