# https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/description/

class Solution:
    def minBitwiseArray(self, arr: List[int]) -> List[int]:
        out = []
        for x in arr:
            l = self.countLeadingBits(x)-1
            if l < 0:
                out.append(l)
            else:
                out.append(x-(1 << l))
        return out

    def countLeadingBits(self, x):
        out = 0
        while x & 1:
            out += 1
            x >>= 1
        return out
