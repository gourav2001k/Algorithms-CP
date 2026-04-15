# https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/description/

class Solution:
    def xorAfterQueries(self, arr: List[int], queries: List[List[int]]) -> int:
        mod = 10**9+7
        n = len(arr)
        b = int(n**0.5)  # block size

        kData = defaultdict(list)
        for l, r, k, v in queries:
            if k >= b:
                for i in range(l, r+1, k):
                    arr[i] *= v
                    arr[i] %= mod
            else:
                kData[k].append((l, r, v))

        for k in kData:
            diff = [1 for i in range(n+b)]
            for l, r, v in kData[k]:
                diff[l] = (diff[l]*v) % mod
                R = ((r-l)//k+1)*k+l
                diff[R] = (diff[R]*pow(v, mod-2, mod)) % mod
            for i in range(k, n):
                diff[i] *= diff[i-k]
                diff[i] %= mod

            for i in range(n):
                arr[i] *= diff[i]
                arr[i] %= mod

        out = 0
        for x in arr:
            out ^= x
        return out
