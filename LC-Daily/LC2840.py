# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)
        even1, odd1 = Counter(), Counter()
        even2, odd2 = Counter(), Counter()
        for i in range(n):
            if i & 1:
                even1[s1[i]] += 1
                even2[s2[i]] += 1
            else:
                odd1[s1[i]] += 1
                odd2[s2[i]] += 1

        if even1 != even2:
            return False
        if odd1 != odd2:
            return False
        return True
