# https://leetcode.com/problems/path-existence-queries-in-a-graph-i/

class Solution:
    def pathExistenceQueries(self, n: int, arr: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        par = [i for i in range(n)]
        rank = [0 for i in range(n)]

        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]

        def union(a, b):
            x, y = find(a), find(b)
            if x == y:
                return
            if rank[x] < rank[y]:
                y, x = x, y
            par[y] = x
            rank[x] += 1

        for i in range(1, n):
            if arr[i]-arr[i-1] > maxDiff:
                continue
            union(i, i-1)

        out = []
        for a, b in queries:
            find(a), find(b)
            out.append(par[a] == par[b])
        return out
