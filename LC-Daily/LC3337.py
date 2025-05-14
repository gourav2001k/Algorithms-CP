# https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/description/

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        N, MOD = 26, 10**9+7

        count = [0 for i in range(N)]
        for i in s:
            count[ord(i)-97] += 1

        transformationMat = [[0 for i in range(N)]for j in range(N)]
        for i in range(N):
            j = (i+1) % 26
            while nums[i]:
                transformationMat[i][j] += 1
                j = (j+1) % 26
                nums[i] -= 1

        finalTransform = self.matrixExpo(transformationMat, t, MOD)
        freq = self.dotProduct(count, finalTransform, MOD)

        out = 0
        for x in freq:
            out += x
            out %= MOD
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
