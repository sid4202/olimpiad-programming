class Solution(object):
    def isAnagram(self, s, t):
        dict = {}

        for c in s:
            if c in dict.keys():
                dict[c] += 1
            else:
                dict[c] = 1

        for c in t:
            if c in dict.keys():
                dict[c] -= 1
            else:
                return False

        for key in dict:
            if dict[key] != 0:
                return False

        return True
