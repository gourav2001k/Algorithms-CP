# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/description/

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)

        vis = [0 for i in range(n)]

        def dfsCycle(root):
            vis[root] = 1
            for cur in g[root]:
                if vis[cur] == 1:
                    return 1
                if vis[cur]:
                    continue
                if dfsCycle(cur):
                    return 1
            vis[root] = 2
            return 0

        for i in range(n):
            if vis[i]:
                continue
            if dfsCycle(i):
                return -1

        ans = dict()

        def solve(root):
            if root in ans:
                return ans[root]
            count = [0 for i in range(26)]
            for cur in g[root]:
                x = solve(cur)
                for i in range(26):
                    count[i] = max(count[i], x[i])
            count[ord(colors[root])-97] += 1
            ans[root] = count
            return count

        out = 0
        for x in range(n):
            out = max(out, max(solve(x)))
        return out
