class Solution(object):
    def len_of_subarray(self, nums, number):
        first_index_of_most_frequent_element = 0

        for i in range(len(nums)):
            if nums[i] == number:
                first_index_of_most_frequent_element = i
                break

        last_index_of_most_frequent_element = 0

        for i in range(len(nums)):
            if nums[i] == number:
                last_index_of_most_frequent_element = i

        answer = last_index_of_most_frequent_element - first_index_of_most_frequent_element
        return answer + 1

    def findShortestSubArray(self, nums):
        dict = {}

        for num in nums:
            if num in dict.keys():
                dict[num] += 1
            else:
                dict[num] = 1

        biggest_frequency = max(dict.values())
        values = list(dict.values())
        biggest_frequency_pos = values.index(biggest_frequency)

        keys = list(dict.keys())
        max_frequent_element = keys[biggest_frequency_pos]

        most_frequent_numbers = []
        maximum_frequency = max(values)
        for i in range(len(values)):
            if values[i] == maximum_frequency:
                most_frequent_numbers.append(keys[i])
        results = []
        for i in most_frequent_numbers:
            results.append(self.len_of_subarray(nums, i))
        result = min(results)

        return result
