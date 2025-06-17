# https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/submissions

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        N = 10**5+1
        if k == n-1:
            return m
        if m == 1 and k != n-1:
            return 0
        mod = 10**9+7
        fact = [1 for i in range(N)]
        for i in range(1, N):
            fact[i] *= fact[i-1]*i
            fact[i] %= mod
        out = m*self.nCr(n-1, k, fact)
        out *= pow(m-1, n-1-k, mod)
        return out % mod

    def nCr(self, n, r, fact):
        mod = 10**9+7
        num = fact[n]
        dino = (fact[n-r]*fact[r]) % mod
        dinoInv = pow(dino, mod-2, mod)
        return (num*dinoInv) % mod
