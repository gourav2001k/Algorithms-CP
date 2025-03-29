# https://leetcode.com/problems/apply-operations-to-maximize-score/description/

class Solution:
    def maximumScore(self, arr: List[int], k: int) -> int:
        n, MOD = len(arr), 10**9+7
        N = 10**5+1  # sieve construction
        sieve = [i for i in range(N)]
        for i in range(2, N):
            if sieve[i] != i:
                continue
            for j in range(i*i, N, i):
                if sieve[j] == j:
                    sieve[j] = i

        primeScores = [0 for i in range(n)]
        for i in range(n):
            cur = arr[i]
            s = set()
            while cur > 1:
                s.add(sieve[cur])
                cur //= sieve[cur]
            primeScores[i] += len(s)

        maxPq, stack = [], []
        nextL2R = [n for i in range(n)]  # next strictly larger index to Right
        for i in range(n-1, -1, -1):
            heappush(maxPq, (-arr[i], i))
            while stack and primeScores[stack[-1]] <= primeScores[i]:
                stack.pop()
            if stack:
                nextL2R[i] = stack[-1]
            stack.append(i)

        stack = []
        nextL2L = [-1 for i in range(n)]  # next larger index to left
        for i in range(n):
            while stack and primeScores[stack[-1]] < primeScores[i]:
                stack.pop()
            if stack:
                nextL2L[i] = stack[-1]
            stack.append(i)

        out = 1
        while k and maxPq:
            cur, idx = heappop(maxPq)
            count = min((nextL2R[idx]-idx)*(idx-nextL2L[idx]), k)
            out *= pow(-cur, count, MOD)
            out %= MOD
            k -= count

        return out
