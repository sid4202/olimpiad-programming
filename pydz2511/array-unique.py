def array_unique(arr):
    set_arr = set(arr)
    return len(set_arr)


arr = list(map(int, input().split(" ")))
print(array_unique(arr))