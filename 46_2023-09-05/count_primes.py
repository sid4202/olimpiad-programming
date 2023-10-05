import math

class Solution:
    def is_prime(self, n):
        for i in range(2, int(math.sqrt(n))):
            if n % i == 0:
                return False

        return True


    def countPrimes(self, n: int) -> int:
        prime_map = [True for i in range(n)]

        for i in range(n):
            if i == 0 or i == 1:
                prime_map[i] = False
                continue

            if self.is_prime(i):
                if i * i <= n - 1:
                    for j in range(i * i, n, i):
                        prime_map[j] = False

        return prime_map.count(True)


sol1 = Solution()

print(sol1.countPrimes(1))