# https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/description

class Solution:
    def minOperations(self, arr: List[int]) -> int:
        n = len(arr)
        c = arr.count(1)
        if c:
            return n-c
        out = 10**6
        for i in range(n):
            g = arr[i]
            j = i
            while j < n and g != 1:
                g = gcd(g, arr[j])
                j += 1
            if g == 1:
                out = min(j-i+n-2, out)
        if out == 10**6:
            return -1
        return out
