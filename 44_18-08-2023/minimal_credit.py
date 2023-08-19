class Solution():
    def __init__(self):
        self.field = []

    def fill_the_field(self):
        n = int(input())

        for i in range(n):
            line = list(map(int, input().split()))
            self.field.append(line)

    def is_enough_money(self, n):
        self.field[0][0] = n
        dp = [[0 for j in range(len(self.field[0]) + 1)] for i in range(len(self.field) + 1)]
        for i in range(1, len(self.field) + 1):
            for j in range(1, len(self.field[0]) + 1):
                current_price = self.field[i - 1][j - 1]
                possible_prices = []
                if dp[i - 1][j] != -1:
                    possible_prices.append(dp[i - 1][j])
                if dp[i][j - 1] != -1:
                    possible_prices.append(dp[i][j - 1])

                if len(possible_prices) == 0:
                    return False

                dp[i][j] = max(possible_prices) + current_price
                if dp[i][j] < 0:
                    dp[i][j] = -1

        if dp[len(dp) - 1][len(dp[0]) - 1] != -1:
            return True

    def minimal_credit(self):
        l = 0
        r = 10 ** 9

        while True:
            n = (l + r) // 2
            answer = self.is_enough_money(n)
            if answer and not self.is_enough_money(n - 1):
                return n

            if answer:
                r = n - 1
            else:
                l = n + 1
                

sol = Solution()
sol.fill_the_field()
print(sol.minimal_credit())
