import math


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
            self.b.append(sum(self.a[i:i + len_of_slice]))

    def query(self, start, stop):
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
            answer = sum(self.b[b_start:b_stop + 1])
        counted_a_start = b_start * self.len_of_slice
        counted_a_stop = self.len_of_slice * (b_stop + 1) - 1
        answer += sum(self.a[counted_a_stop + 1: stop + 1]) + sum(self.a[start:counted_a_start])

        return answer


service = SqrtDecomposition()
service.build([7, 8, 4, 6, 12, 3, 10, 23])

print(service.query(5, 7)) #25
print(service.query(3, 8)) #58
print(service.query(1, 3)) #19
