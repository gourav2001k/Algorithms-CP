# https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/description/

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        par = [i for i in range(n)]
        rank = [0 for i in range(n)]

        def findPar(x):
            if par[x] != x:
                par[x] = findPar(par[x])
            return par[x]

        def union(a, b):
            x, y = findPar(a), findPar(b)
            if x == y:
                return
            if rank[x] < rank[y]:
                x, y = y, x
                a, b = b, a
            par[y] = x
            rank[x] += 1

        for a, b, w in edges:
            union(a, b)

        for i in range(n):
            findPar(i)

        cost = [(1 << 32)-1 for i in range(n)]
        for a, b, w in edges:
            cost[par[a]] &= w

        out = []
        for a, b in query:
            if par[a] != par[b]:
                out.append(-1)
            else:
                out.append(cost[par[a]])

        return out
