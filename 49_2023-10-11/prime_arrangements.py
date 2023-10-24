import math


class Solution:
    def countPrimes(self, n: int) -> int:
        prime_map = [True for i in range(n)]

        if n == 0 or n == 1:
            return 0

        primes = n - 2

        for i in range(n):
            if i == 0 or i == 1:
                prime_map[i] = False
                continue

            if prime_map[i]:
                if i * i <= n - 1:
                    for j in range(i * i, n, i):
                        if prime_map[j]:
                            prime_map[j] = False
                            primes -= 1

        return primes

    def numPrimeArrangements(self, n: int) -> int:
        return
