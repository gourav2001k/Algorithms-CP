# https://leetcode.com/problems/minimum-hamming-distance-after-swap-operations/description/

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        par = [i for i in range(n)]
        rank = [0 for i in range(n)]

        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]

        def union(x, y):
            a, b = find(x), find(y)
            if a == b:
                return
            if rank[a] < rank[b]:
                a, b = b, a
            par[b] = a
            rank[a] += 1

        for x, y in allowedSwaps:
            union(x, y)

        groups = defaultdict(Counter)
        for i in range(n):
            groups[find(i)][source[i]] += 1

        out = 0
        for i in range(n):
            if groups[find(i)][target[i]] <= 0:
                out += 1
            else:
                groups[find(i)][target[i]] -= 1
        return out
