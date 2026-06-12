# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/description

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges)+1
        g = defaultdict(set)
        for u, v in edges:
            u -= 1
            v -= 1
            g[u].add(v)
            g[v].add(u)

        par = [-1 for i in range(n)]
        depth = [0 for i in range(n)]

        def dfs(root, parent):
            for cur in g[root]:
                if cur == parent:
                    continue
                par[cur] = root
                depth[cur] = depth[root]+1
                dfs(cur, root)
        dfs(0, -1)

        lca_par = [[-1 for i in range(20)]for j in range(n)]
        for j in range(n):
            lca_par[j][0] = par[j]
        for i in range(1, 20):
            for j in range(n):
                if lca_par[j][i-1] != -1:
                    lca_par[j][i] = lca_par[lca_par[j][i-1]][i-1]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            for i in range(20, -1, -1):
                if depth[u]-(1 << i) >= depth[v]:
                    u = lca_par[u][i]
            if u == v:
                return u
            for i in range(19, -1, -1):
                if lca_par[u][i] != lca_par[v][i]:
                    u = lca_par[u][i]
                    v = lca_par[v][i]
            return lca_par[u][0]

        mod = 10**9+7
        dp = [(0, 0), (1, 1)]
        for i in range(2, n):
            s = (dp[i-1][0]+dp[i-1][1]) % mod
            dp.append((s, s))

        out = []
        for u, v in queries:
            u -= 1
            v -= 1
            lca_node = lca(u, v)
            dist = depth[u]+depth[v]-2*depth[lca_node]
            out.append(dp[dist][0])

        return out
