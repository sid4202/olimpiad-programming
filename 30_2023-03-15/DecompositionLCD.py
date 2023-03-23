import math


def gcd_array(arr):
    if not arr:
        return 0
    result = arr[0]
    for i in range(1, len(arr)):
        result = math.gcd(result, arr[i])

    return result


class SqrtDecomposition:
    def __init__(self):
        self.a = []
        self.b = []
        self.len_of_slice = 0

    def build(self, arr):
        len_of_slice = int(pow(len(arr), 0.5))
        self.a = arr
        self.len_of_slice = len_of_slice
        for i in range(0, len(self.a), len_of_slice):
            self.b.append(gcd_array(self.a[i:i + len_of_slice + 1]))

    def query(self, start, stop):
        print(self.b)
        start -= 1
        stop -= 1

        b_start = math.ceil(start / self.len_of_slice)
        if stop != len(self.a) - 1:
            b_stop = (stop + 1) // self.len_of_slice - 1
        else:
            b_stop = len(self.b) - 1

        if b_stop < b_start:
            answer = 0
        else:
            answer = gcd_array(self.b[b_start:b_stop + 1])
        counted_a_start = b_start * self.len_of_slice
        counted_a_stop = self.len_of_slice * (b_stop + 1) - 1
        print(self.a[counted_a_stop + 1: stop + 1])
        stop_gcd = gcd_array(self.a[counted_a_stop + 1: stop + 1])

        start_gcd = gcd_array(self.a[start:counted_a_start])
        print([answer, start_gcd, stop_gcd])
        answer = gcd_array([answer, start_gcd, stop_gcd])

        return answer



service = SqrtDecomposition()
service.build([7, 8, 4, 6, 12])

print(service.query(2, 5))
print(service.query(1, 2))
print(service.query(4, 5))
print(service.query(2, 3))