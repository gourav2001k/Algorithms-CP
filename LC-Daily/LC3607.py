# https://leetcode.com/problems/power-grid-maintenance/description/

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        par = [i for i in range(c+1)]

        def findPar(x):
            if par[x] != x:
                par[x] = findPar(par[x])
            return par[x]

        def union(x, y):
            a, b = findPar(x), findPar(y)
            if a == b:
                return
            if a > b:
                b, a = a, b
            par[b] = a

        for a, b in connections:
            union(a, b)

        parHeap = defaultdict(list)
        for x in range(1, c+1):
            heappush(parHeap[findPar(x)], x)

        out = []
        offline = set()
        for t, x in queries:
            if t == 1:
                if x not in offline:
                    out.append(x)
                    continue
                p = findPar(x)
                while parHeap[p] and parHeap[p][0] in offline:
                    heappop(parHeap[p])
                if parHeap[p]:
                    out.append(parHeap[p][0])
                else:
                    out.append(-1)
            else:
                offline.add(x)

        return out
