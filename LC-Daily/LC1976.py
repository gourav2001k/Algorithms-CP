# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        e = len(roads)
        g = defaultdict(list)
        for i in range(e):
            u, v, w = roads[i]
            g[u].append((v, i))
            g[v].append((u, i))

        MAX, MOD = 10**18, 10**9+7
        dist = [MAX for i in range(n)]
        pathCount = [0 for i in range(n)]
        dist[0], pathCount[0] = 0, 1
        pq = [(0, 0)]
        while pq:
            cost, cur = heappop(pq)
            if dist[cur] < cost:
                continue
            for x, i in g[cur]:
                if dist[cur]+roads[i][2] > dist[x]:
                    continue
                if dist[cur]+roads[i][2] == dist[x]:
                    pathCount[x] += pathCount[cur]
                    pathCount[x] %= MOD
                else:
                    dist[x] = dist[cur]+roads[i][2]
                    heappush(pq, (dist[x], x))
                    pathCount[x] = pathCount[cur]
        return pathCount[n-1]
