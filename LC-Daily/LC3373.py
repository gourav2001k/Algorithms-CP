# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/description

# Slightly Complex
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        n, m = len(edges1)+1, len(edges2)+1
        g1 = defaultdict(list)
        g2 = defaultdict(list)
        for a, b in edges1:
            g1[a].append(b)
            g1[b].append(a)

        for a, b in edges2:
            g2[a].append(b)
            g2[b].append(a)

        counts1 = [[0, 0] for i in range(n)]
        counts2 = [[0, 0] for i in range(m)]
        self.oddEvenCount(0, -1, counts1, g1)
        self.oddEvenCount(0, -1, counts2, g2)

        target1 = [[0, 0] for i in range(n)]
        target2 = [[0, 0] for i in range(m)]
        self.constructTarget(0, -1, counts1, target1, g1)
        self.constructTarget(0, -1, counts2, target2, g2)

        maxReach = 0
        for i in range(m):
            maxReach = max(maxReach, target2[i][0])

        out = [target1[i][1]+maxReach for i in range(n)]
        return out

    def oddEvenCount(self, root, par, counts, g):
        odd, even = 0, 1
        for cur in g[root]:
            if cur == par:
                continue
            a, b = self.oddEvenCount(cur, root, counts, g)
            odd += b
            even += a
        counts[root] = [odd, even]
        return odd, even

    def constructTarget(self, root, par, counts, target, g):
        odd, even = counts[root]
        if par != -1:
            x, y = target[par]
            x -= even
            y -= odd
            odd += y
            even += x
        target[root] = [odd, even]
        for cur in g[root]:
            if cur == par:
                continue
            self.constructTarget(cur, root, counts, target, g)


# Approach 2: Simplified using Bipartite
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        n, m = len(edges1)+1, len(edges2)+1
        g1 = defaultdict(list)
        g2 = defaultdict(list)
        for a, b in edges1:
            g1[a].append(b)
            g1[b].append(a)

        for a, b in edges2:
            g2[a].append(b)
            g2[b].append(a)

        colors1 = [0 for i in range(n)]
        colors2 = [0 for i in range(m)]
        odd, even = self.oddEvenCount(0, -1, 0, colors1, g1)
        maxReach = max(self.oddEvenCount(0, -1, 0, colors2, g2))

        out = [maxReach for i in range(n)]
        for i in range(n):
            if colors1[i]:
                out[i] += odd
            else:
                out[i] += even
        return out

    def oddEvenCount(self, root, par, color, colors, g):
        odd, even = 0, 1
        colors[root] = color
        for cur in g[root]:
            if cur == par:
                continue
            a, b = self.oddEvenCount(cur, root, color ^ 1, colors, g)
            odd += b
            even += a
        return odd, even
