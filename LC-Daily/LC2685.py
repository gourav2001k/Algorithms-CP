# https://leetcode.com/problems/count-the-number-of-complete-components/description/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        vis = [0 for i in range(n)]
        component = 0
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        def bfs(root):
            q = deque([root])
            vis[root] = component
            edgeCount, nodeCount = 0, 1
            while q:
                for _ in range(len(q)):
                    cur = q.popleft()
                    for x in g[cur]:
                        edgeCount += 1
                        if vis[x]:
                            continue
                        vis[x] = component
                        nodeCount += 1
                        q.append(x)
            return edgeCount//2, nodeCount

        def nC2(x):
            return (x*(x-1))//2

        out = 0
        for i in range(n):
            if vis[i]:
                continue
            component += 1
            edges, nodes = bfs(i)
            if nodes < 3:
                out += 1
            elif nC2(nodes) == edges:
                out += 1

        return out
