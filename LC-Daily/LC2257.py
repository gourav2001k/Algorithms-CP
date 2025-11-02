# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/description/

class Solution:
    def countUnguarded(self, n: int, m: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        gCol = [[] for i in range(m)]
        wCol = [[] for i in range(m)]
        gRow = [[] for i in range(n)]
        wRow = [[] for i in range(n)]
        forbidden = set()
        for i, j in guards:
            gCol[j].append(i)
            gRow[i].append(j)
            forbidden.add((i, j))

        for i, j in walls:
            wCol[j].append(i)
            wRow[i].append(j)
            forbidden.add((i, j))

        def sortInner(mat):
            for row in mat:
                row.sort()

        sortInner(gCol)
        sortInner(wCol)
        sortInner(gRow)
        sortInner(wRow)

        out = 0

        for i in range(n):
            for j in range(m):
                if (i, j) in forbidden:
                    continue
                # row Right
                rowRG = bisect_right(gRow[i], j)
                rowRW = bisect_right(wRow[i], j)
                if not (not rowRG < len(gRow[i]) or
                        (rowRW < len(wRow[i]) and wRow[i][rowRW] < gRow[i][rowRG])):
                    continue
                # row Left
                rowLG = bisect_left(gRow[i], j)
                rowLW = bisect_left(wRow[i], j)
                if not (not rowLG or
                        (rowLW and wRow[i][rowLW-1] > gRow[i][rowLG-1])):
                    continue

                # col Right
                colRG = bisect_right(gCol[j], i)
                colRW = bisect_right(wCol[j], i)
                if not (not colRG < len(gCol[j]) or
                        (colRW < len(wCol[j]) and wCol[j][colRW] < gCol[j][colRG])):
                    continue
                # col Left
                colLG = bisect_left(gCol[j], i)
                colLW = bisect_left(wCol[j], i)
                if not (not colLG or
                        (colLW and wCol[j][colLW-1] > gCol[j][colLG-1])):
                    continue
                out += 1

        return out
