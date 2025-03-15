# https://leetcode.com/problems/modify-graph-edge-weights/description/

class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], s: int, d: int, t: int) -> List[List[int]]:
        e = len(edges)
        g = defaultdict(list)
        for i in range(e):
            a, b, w = edges[i]
            g[a].append((b, i))
            g[b].append((a, i))

        MAX = 10**12
        dist = [[MAX, MAX]for i in range(n)]
        dist[s] = [0, 0]

        def dijkstra(adjust, itr):
            pq = [(0, s)]
            while pq:
                c, cur = heappop(pq)
                if c > dist[cur][itr]:
                    continue
                for child, idx in g[cur]:
                    w = edges[idx][2]
                    if w == -1:
                        w = 1
                    if itr and edges[idx][2] == -1 and dist[child][0]-dist[cur][1]+adj > 1:
                        edges[idx][2] = w = dist[child][0]-dist[cur][1]+adj
                    if dist[child][itr] <= c+w:
                        continue
                    dist[child][itr] = c+w
                    heappush(pq, (dist[child][itr], child))

        dijkstra(0, 0)
        if dist[d][0] > t:
            return []
        adj = t-dist[d][0]
        dijkstra(adj, 1)
        if dist[d][1] < t:
            return []
        for i in range(e):
            if edges[i][2] == -1:
                edges[i][2] = 1
        return edges
