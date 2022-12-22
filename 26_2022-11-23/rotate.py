class Solution:
    def getRotationSum(nums: List[int]):
        sum = 0
        for i in range(len(nums)):
            sum += i * nums[i]
        return sum

    def maxRotateFunction(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        len_nums = len(nums)
        max_element_pos = len_nums - 1
        previous_rotation = self.getRotationSum(nums)
        max_rotation = previous_rotation
        max_element_pos -= 1


        while max_element_pos >= 0:
            current_rotation = previous_rotation + sum(nums) - (len(nums) * nums[max_element_pos])

            if current_rotation > max_rotation:
                max_rotation = current_rotation

            previous_rotation = current_rotation
            max_element_pos -= 1

        return max_rotation
