# https://leetcode.com/problems/range-product-queries-of-powers/description/

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        x, mod = 1, 10**9+7
        pre = [1]
        while x <= n:
            if x & n:
                pre.append(x)
            x <<= 1

        for i in range(1, len(pre)):
            pre[i] *= pre[i-1]
            pre[i] %= mod

        out = []
        for a, b in queries:
            out.append((pre[b+1]*pow(pre[a], mod-2, mod)) % mod)
        return out
