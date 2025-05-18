# https://leetcode.com/problems/painting-a-grid-with-three-different-colors/description/

# Approach 1: Applying Tranforamation with a help of loop
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


# Approach 2: Transformation was binary exponentiated to speed up
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

        finalTransform = self.matrixExpo(transformation, n-1, mod)
        dp = self.dotProduct(dp, finalTransform, mod)

        out = 0
        for x in dp:
            out += x
            out %= mod
        return out

    def matrixExpo(self, mat: List[List[int]], power: int, mod: int) -> List[List[int]]:
        N = len(mat)
        res = [[1 if i == j else 0 for j in range(N)] for i in range(N)]

        while power > 0:
            if power & 1:
                res = self.matrixMultiply(res, mat, mod)
            mat = self.matrixMultiply(mat, mat, mod)
            power >>= 1
        return res

    def matrixMultiply(self, A: List[List[int]], B: List[List[int]], mod: int) -> List[List[int]]:
        N = len(A)
        result = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % mod
        return result

    def dotProduct(self, vec: List[int], mat: List[List[int]], mod: int) -> List[int]:
        N = len(vec)
        result = [0 for _ in range(N)]
        for j in range(N):
            for i in range(N):
                result[j] = (result[j] + vec[i] * mat[i][j]) % mod
        return result
