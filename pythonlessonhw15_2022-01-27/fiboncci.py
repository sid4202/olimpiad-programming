class Solution(object):
    def __init__(self):
        self.cached_fibonaccis = {
            0:0,
            1:1,
            2:1
        }
    def fib(self, n):
        if n in self.cached_fibonaccis:
            return self.cached_fibonaccis[n]
        if n == 1 or n == 2:
            return 1

        n_fibonacci = self.fib(n - 1) + self.fib(n - 2)

        self.cached_fibonaccis[n] = n_fibonacci

        return n_fibonacci