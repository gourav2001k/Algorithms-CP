# https://leetcode.com/problems/find-the-original-typed-string-i/description/

class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        l, out = 1, 1
        for i in range(1, n):
            if word[i] != word[i-1]:
                out += l-1
                l = 1
            else:
                l += 1
        out += l-1
        return out
