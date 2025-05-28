# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/description/

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n, m = len(edges1)+1, len(edges2)+1
        g1 = defaultdict(list)
        g2 = defaultdict(list)
        for a, b in edges1:
            g1[a].append(b)
            g1[b].append(a)

        for a, b in edges2:
            g2[a].append(b)
            g2[b].append(a)

        reachMax = 0
        if k:
            for src in range(m):
                reachMax = max(reachMax, self.countReachable(src, -1, k-1, g2))

        out = [0 for i in range(n)]
        for src in range(n):
            out[src] = self.countReachable(src, -1, k, g1)+reachMax

        return out

    def countReachable(self, src, par, depth, g):
        out = 1
        if not depth:
            return out
        for child in g[src]:
            if par == child:
                continue
            out += self.countReachable(child, src, depth-1, g)
        return out
