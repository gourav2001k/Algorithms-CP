# https://leetcode.com/problems/count-covered-buildings/description/

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        xMaps = defaultdict(list)
        yMaps = defaultdict(list)
        for a, b in buildings:
            xMaps[a].append(b)
            yMaps[b].append(a)

        for x in xMaps:
            xMaps[x].sort()
        for y in yMaps:
            yMaps[y].sort()

        out = 0
        for a, b in buildings:
            x = bisect_left(xMaps[a], b)
            y = bisect_left(yMaps[b], a)
            if x <= 0 or x+1 >= len(xMaps[a]):
                continue
            if y <= 0 or y+1 >= len(yMaps[b]):
                continue
            out += 1
        return out
