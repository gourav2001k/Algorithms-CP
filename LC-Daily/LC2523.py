# https://leetcode.com/problems/closest-prime-numbers-in-range/

class Solution:
    def __init__(self):
        N = 10**6+1
        sieve = [i for i in range(N)]
        self.prime = []
        for i in range(2, N):
            if sieve[i] != i:
                continue
            self.prime.append(i)
            for j in range(i*i, N, i):
                if sieve[j] != j:
                    continue
                sieve[j] = i

    def closestPrimes(self, left: int, right: int) -> List[int]:
        a, b = -1, -1
        idx = bisect_right(self.prime, left)
        if idx-1 >= 0 and self.prime[idx-1] == left:
            idx -= 1
        while idx+1 < len(self.prime) and self.prime[idx+1] <= right:
            if a == -1:
                a, b = self.prime[idx], self.prime[idx+1]
            elif self.prime[idx+1]-self.prime[idx] < b-a:
                a, b = self.prime[idx], self.prime[idx+1]
            idx += 1
        return a, b
