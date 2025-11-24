# https://leetcode.com/problems/binary-prefix-divisible-by-5/description/

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        out, v = [], 0
        for x in nums:
            v <<= 1
            v += x
            if v % 5:
                out.append(False)
            else:
                out.append(True)
        return out
