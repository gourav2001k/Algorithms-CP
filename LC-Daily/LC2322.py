# https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/description/

class Solution:
    def minimumScore(self, nodes: List[int], edges: List[List[int]]) -> int:
        n = len(nodes)
        g = defaultdict(set)
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)

        par = [-1 for i in range(n)]
        xors = [0 for i in range(n)]

        def calXor(root, p):
            par[root] = p
            xors[root] ^= nodes[root]
            for cur in g[root]:
                if cur == p:
                    continue
                xors[root] ^= calXor(cur, root)
            return xors[root]

        # consider 0 as root
        total = calXor(0, -1)
        binaryLifting = BinaryLiftingLCA(n, par, g)

        out = 10**9
        for i in range(n-1):
            for j in range(i+1, n-1):
                x1, y1 = edges[i]
                if par[x1] != y1:
                    x1, y1 = y1, x1
                x2, y2 = edges[j]
                if par[x2] != y2:
                    x2, y2 = y2, x2
                a = xors[x1]
                b = xors[x2]
                c = total
                p = binaryLifting.lca(x1, x2)
                if p == x1:
                    c ^= a
                    a ^= b
                elif p == x2:
                    c ^= b
                    b ^= a
                else:
                    c ^= a ^ b
                out = min(max(a, b, c)-min(a, b, c), out)
        return out


class BinaryLiftingLCA:
    def __init__(self, n, par, graph):
        self.n = n
        self.LOG = math.ceil(math.log2(n)) + 1
        self.up = [[-1] * self.LOG for _ in range(n)]
        self.depth = [0] * n
        self.graph = graph

        root = par.index(-1)
        self.dfs(root, -1)

    def dfs(self, node, parent):
        self.up[node][0] = parent
        for j in range(1, self.LOG):
            if self.up[node][j - 1] != -1:
                self.up[node][j] = self.up[self.up[node][j - 1]][j - 1]

        for neighbor in self.graph[node]:
            if neighbor != parent:
                self.depth[neighbor] = self.depth[node] + 1
                self.dfs(neighbor, node)

    def lift(self, node, k):
        for i in range(self.LOG):
            if k & (1 << i):
                node = self.up[node][i]
                if node == -1:
                    break
        return node

    def lca(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u

        u = self.lift(u, self.depth[u] - self.depth[v])

        if u == v:
            return u

        for i in reversed(range(self.LOG)):
            if self.up[u][i] != -1 and self.up[u][i] != self.up[v][i]:
                u = self.up[u][i]
                v = self.up[v][i]

        return self.up[u][0]
