# https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/description/

class Solution:
    def minElement(self, arr: List[int]) -> int:
        out = arr[0]
        for x in arr:
            out = min(self.compress(x), out)
        return out

    def compress(self, x):
        a = 0
        while x:
            a += x % 10
            x //= 10
        return a
