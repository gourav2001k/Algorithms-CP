# https://leetcode.com/problems/count-number-of-balanced-permutations/description/

class Solution:
    def countBalancedPermutations(self, s: str) -> int:
        n = len(s)
        k, mod = 0, 10**9+7
        arr = []
        for x in s:
            k += int(x)
            arr.append(int(x))
        freq = Counter(arr)
        if k & 1:
            return 0
        k >>= 1
        even = n >> 1

        # normal 2D subset sum count doesn't work because, we have to make sure
        # sequence length should be exactly even length or odd length
        # 2D subset sum count doesn't care about sequence length
        dp = [[[-1 for x in range(k+1)]for y in range(even+1)]
              for z in range(n+1)]

        def solve(pos, taken, s):
            if dp[pos][taken][s] != -1:
                return dp[pos][taken][s]
            if s == 0 and taken == 0:
                return 1
            if pos == n or taken < 0 or s < 0:
                return 0
            out = solve(pos+1, taken, s)+solve(pos+1, taken-1, s-arr[pos])
            dp[pos][taken][s] = out % mod
            return dp[pos][taken][s]

        out = solve(0, even, k)
        fact = [1 for i in range(n+1)]
        for i in range(1, n+1):
            fact[i] *= fact[i-1]*i
            fact[i] %= mod

        out *= fact[n >> 1]*fact[n-(n >> 1)]
        out %= mod
        # we should handle repitions of odd and even case independently
        # but since we are any ways multiplying the odd and even length permutation
        # so we computing it together
        for i in freq:
            out *= pow(fact[freq[i]], mod-2, mod)
            out %= mod

        return out
