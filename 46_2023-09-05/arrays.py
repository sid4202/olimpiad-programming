def merge(arr1, arr2):
    merge_result = set(arr1)
    for num in arr2:
        if num not in merge_result:
            merge_result.add(num)

    return merge_result


def solve():
    n = int(input())

    arrays = []
    for i in range(n):
        arr = list(map(int, input().split()))
        arrays.append(set(arr[1::]))

    if n == 1:
        return 0

    # print(arrays)

    incorrect_merge = []
    for i in range(n):
        incorrect_merge = merge(incorrect_merge, arrays[i])

    max_length = len(incorrect_merge)
    max_correct_len = 0

    for i in range(1, 51):
        correct_merge = []
        for array in arrays:
            if i in array:
                continue

            correct_merge.extend(array)

        if len(set(correct_merge)) == max_length:
            continue

        max_correct_len = max(max_correct_len, len(set(correct_merge)))

    return max_correct_len


t = int(input())
for _ in range(t):
    print(solve())