# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        loc = [-1, -1, -1]
        out = 0
        for i in range(n):
            loc[ord(s[i])-97] = i
            out += min(loc)+1
        return out
