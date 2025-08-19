# https://leetcode.com/problems/number-of-zero-filled-subarrays/description

class Solution:
    def zeroFilledSubarray(self, arr: List[int]) -> int:
        c, out = 0, 0
        for x in arr:
            if not x:
                c += 1
            else:
                out += (c*(c+1))//2
                c = 0
        out += (c*(c+1))//2
        return out
