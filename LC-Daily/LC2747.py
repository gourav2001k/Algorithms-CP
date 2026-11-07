class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        l, qs = len(logs), len(queries)
        logs.sort(key=lambda x: x[1])
        queries = list(sorted(enumerate(queries), key=lambda x: x[1]))

        p, q = 0, 0
        count = Counter()
        out = [0 for i in range(qs)]
        for i, qq in queries:
            while q < l and logs[q][1] <= qq:
                count[logs[q][0]] += 1
                q += 1
            while p < l and logs[p][1] < qq-x:
                count[logs[p][0]] -= 1
                if not count[logs[p][0]]:
                    del count[logs[p][0]]
                p += 1
            out[i] = n-len(count)
        return out
