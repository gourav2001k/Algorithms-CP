# https://leetcode.com/problems/four-divisors/description/

class Solution:
    def sumFourDivisors(self, arr: List[int]) -> int:
        N = 10**5+1
        seive = [i for i in range(N)]
        for i in range(2, N):
            if seive[i] != i:
                continue
            for j in range(i*i, N, i):
                if seive[j] != j:
                    continue
                seive[j] = i

        out = 0
        for x in arr:
            factors = set({x})
            while x > 1:
                factors.add(seive[x])
                x //= seive[x]
                factors.add(x)
            if len(factors) == 4:
                out += sum(factors)
        return out
