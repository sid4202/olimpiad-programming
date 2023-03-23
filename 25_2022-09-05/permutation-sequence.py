import math

class Solution(object):
    def getPermutation(self, n: int, k: int):
        answer = []
        pos_in_stuck = 0
        stuck = 0
        possible_numbers = []
        for i in range(1, n+1):
            possible_numbers.append(str(i))
        print(possible_numbers)

        while n - 1 >= 0:
            index = ((k - 1) // (math.factorial(n - 1))) + 1
            print("n:", n, "k:", k, "index:", index-1)
            answer.append(possible_numbers[index-1])
            stuck = (k // math.factorial(n-1)) * math.factorial(n-1)
            print(stuck)
            pos_in_stuck = k - stuck
            possible_numbers.remove(possible_numbers[index-1])
            k = pos_in_stuck

            print(answer)
            n -= 1

        return "".join(answer)


sol = Solution()
print(sol.getPermutation(5, 67))
