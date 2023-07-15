def greatest_integer_divisor(n):
    for i in range(n - 1, 1, -1):
        if n % i == 0:
            return i


def is_prime(n):
    for i in range(n - 1, 1, -1):
        if n % i == 0:
            return False
    return True


def solve(numbers):
    result = []
    for number in numbers:
        if is_prime(number):
            result.append(number)
        else:
            smallest_prime_divisor = number
            answer = 0
            while not is_prime(smallest_prime_divisor):
                diff = smallest_prime_divisor // greatest_integer_divisor(smallest_prime_divisor)
                smallest_prime_divisor = greatest_integer_divisor(smallest_prime_divisor)

                answer += diff
            answer += smallest_prime_divisor
            result.append(answer)
    return result


t = int(input())
numbers = list(map(int, input().split()))
print(*solve(numbers))
