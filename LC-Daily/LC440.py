# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/description/?``

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        out = 1
        k -= 1
        while k:
            count = 0
            l, r = out, out+1
            while l <= n:
                count += min(n+1, r)-l
                l, r = l*10, r*10
            if k >= count:
                out += 1
                k -= count
            else:
                out *= 10
                k -= 1
        return out
