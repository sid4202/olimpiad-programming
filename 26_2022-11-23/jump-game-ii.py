class Solution:
    def jump(self, nums: List[int]) -> int:
        jump_count = {
            0:0
        }
        for i in range(len(nums)):
            for c in range(0, nums[i] + 1):
                print(jump_count)
                if i + c not in jump_count.keys():
                    jump_count[i + c] = jump_count[i] + 1

        print(jump_count)


