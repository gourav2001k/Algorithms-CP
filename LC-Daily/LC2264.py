# https://leetcode.com/problems/largest-3-same-digit-number-in-string/description

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n, m = len(num), ''
        for i in range(3, n+1):
            if num[i-3:i] == num[i-1]*3:
                m = max(m, num[i-1])
        return m*3
