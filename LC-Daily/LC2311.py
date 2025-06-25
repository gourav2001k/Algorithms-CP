class Solution:
    def longestSubsequence(self, a: str, k: int) -> int:
        n = len(a)
        out, s = 0, 0
        for i in range(n-1, -1, -1):
            if a[i] == '0':
                out += 1
            elif s+(1 << out) <= k:
                s += 1 << out
                out += 1
        return out
