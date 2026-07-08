# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        arr = list(map(int, list(s)))

        cur, mod = 0, 10**9+7
        pre = [0 for i in range(n+1)]
        zeros = [0 for i in range(n+1)]
        v = [0 for i in range(n+1)]
        for i in range(n):
            pre[i+1] = pre[i]+arr[i]
            zeros[i+1] = zeros[i]
            if not arr[i]:
                zeros[i+1] += 1
            else:
                cur = (cur*10+arr[i]) % mod
            v[i+1] = cur

        out = []
        for p, q in queries:
            s = pre[q+1]-pre[p]
            ones = q+1-p-(zeros[q+1]-zeros[p])
            k = (v[q+1]-(v[p]*pow(10, ones, mod))) % mod
            out.append(s*k % mod)
        return out
