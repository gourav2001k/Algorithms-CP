# leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/

class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)
        ones, out = 0, 0
        for i in range(n-1):
            if s[i] == '0':
                continue
            ones += 1
            if s[i+1] == '0':
                out += ones
        return out
