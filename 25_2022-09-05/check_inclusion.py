class Solution:
    def __init__(self):
        self.original_stats = dict()

    def is_permutation(self, original: str, permutation: str):

        if len(list(self.original_stats)) == 0:
            for c in original:
                if c in self.original_stats.keys():
                    self.original_stats[c] += 1
                else:
                    self.original_stats[c] = 1

        permutation_stats = dict()

        for c in permutation:
            if c in permutation_stats.keys():
                permutation_stats[c] += 1
            else:
                permutation_stats[c] = 1

        for i in self.original_stats.keys():
            if i in permutation_stats.keys():
                if permutation_stats[i] == self.original_stats[i]:
                    continue
                else:
                    return False
            else:
                return False

        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        slices = []

        for i in range((len(s2) - len(s1)) + 1):
            slices.append(s2[i:i + len(s1)])

        for element in slices:
            if self.is_permutation(s1, element):
                return True

        return False

