# https://leetcode.com/problems/increment-submatrices-by-one/description

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        pre = [[0 for i in range(n+1)]for j in range(n+1)]
        for x1, y1, x2, y2 in queries:
            pre[x1][y1] += 1
            pre[x2+1][y2+1] += 1
            pre[x1][y2+1] -= 1
            pre[x2+1][y1] -= 1

        for i in range(n):
            pre[0][i+1] += pre[0][i]
            pre[i+1][0] += pre[i][0]

        for i in range(n):
            for j in range(n):
                pre[i+1][j+1] += pre[i+1][j]+pre[i][j+1]-pre[i][j]
            pre[i].pop()
        pre.pop()
        return pre
