# https://leetcode.com/problems/closest-equal-element-queries/description/

class Solution:
    def solveQueries(self, arr: List[int], queries: List[int]) -> List[int]:
        n = len(arr)
        count = defaultdict(list)
        for i in range(n):
            count[arr[i]].append(i)

        def findDis(x, y):
            if y < x:
                x, y = y, x
            return min(y-x, x-y+n)

        out = []
        for i in queries:
            v = arr[i]
            if len(count[v]) == 1:
                out.append(-1)
                continue
            x = bisect_left(count[v], i)
            l = (x-1) % len(count[v])
            r = (x+1) % len(count[v])
            k = min(findDis(i, count[v][l]), findDis(count[v][r], i))
            out.append(k)
        return out
