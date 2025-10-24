# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/description

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = list(s)
        while len(s) > 2:
            nS = []
            for i in range(1, len(s)):
                nS.append(str((int(s[i])+int(s[i-1])) % 10))
            s = nS
        return s[0] == s[1]
