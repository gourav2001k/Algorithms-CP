# https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/

from typing import List


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        edges.sort(key=lambda x: -x[2])

        def find(x, par):
            if x != par[x]:
                par[x] = find(par[x], par)
            return par[x]

        def union(x, y, par, rank):
            a, b = find(x, par), find(y, par)
            if a == b:
                return
            if rank[a] > rank[b]:
                a, b = b, a
            par[a] = b
            rank[b] += 1

        def check(x):
            rem = k
            par = [i for i in range(n)]
            rank = [0 for i in range(n)]
            for u, v, s, must in edges:
                if not must:
                    continue
                if find(u, par) == find(v, par):
                    return False
                union(u, v, par, rank)

            for u, v, s, must in edges:
                if must:
                    continue
                if find(u, par) == find(v, par):
                    continue
                union(u, v, par, rank)
                if s >= x:
                    continue
                if 2*s < x:
                    rem = -1
                rem -= 1

            pp = find(0, par)
            for u in range(n):
                if find(u, par) != pp:
                    return False
            return rem >= 0

        r = 2*10**5
        for u, v, s, must in edges:
            if not must:
                continue
            r = min(r, s)

        l, r = -1, r+1
        while l+1 < r:
            m = (l+r) >> 1
            if check(m):
                l = m
            else:
                r = m

        return l
