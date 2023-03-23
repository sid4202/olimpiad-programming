from math import factorial


def get_permutations_count(n: int):
    return factorial(n) - factorial(n - 1)


n = int(input())
print(get_permutations_count(n))
