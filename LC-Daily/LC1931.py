# https://leetcode.com/problems/painting-a-grid-with-three-different-colors/description/

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        # first contruct all possible sequence of m length following the criteria
        # using that will will init dp which will represent combination ending with color
        unq, mod = [], 10**9+7

        def rec(idx=0, seq=[]):
            if idx == m:
                unq.append(tuple(seq))
                return
            if not seq or seq[idx-1] != 0:
                seq.append(0)
                rec(idx+1, seq)
                seq.pop()
            if not seq or seq[idx-1] != 1:
                seq.append(1)
                rec(idx+1, seq)
                seq.pop()
            if not seq or seq[idx-1] != 2:
                seq.append(2)
                rec(idx+1, seq)
                seq.pop()
        rec()
        l = len(unq)

        transformation = [[0 for i in range(l)]for j in range(l)]
        for i in range(l):
            for j in range(l):
                for k in range(m):
                    if unq[i][k] == unq[j][k]:
                        break
                else:
                    transformation[i][j] = 1

        dp = [1 for i in range(l)]
        for _ in range(1, n):
            nDp = [0 for i in range(l)]
            for i in range(l):
                for j in range(l):
                    if transformation[i][j]:
                        nDp[j] += dp[i]
                        nDp[j] %= mod
            dp = nDp

        out = 0
        for x in dp:
            out += x
            out %= mod
        return out
